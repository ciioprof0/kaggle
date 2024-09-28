# %% [code]
"""
Utility script for dynamically loading files from a specified input directory.

This script supports loading CSV, JSON, SQLite, and ZIP archive files from Kaggle's input directory.
It provides a modular framework for future expansion to other file types. The script dynamically
assigns loaded files to variables based on their file names, with specific handling for DataFrames
(appending '_df' to CSV file variable names) and dictionary files (appending '_dict' to JSON file variable names).

Supported file types and loaders:
1. CSV files (.csv) -> pandas DataFrame (filename_df)
2. JSON files (.json) -> Python dictionary (filename_dict)
3. SQLite database files (.sqlite) -> sqlite3 Connection object
4. ZIP files (.zip) -> Extracts files to the current directory or specified extraction directory

Functions:
    load_csv(filepath: str) -> pd.DataFrame:
        Loads a CSV file into a pandas DataFrame.
    
    load_json(filepath: str) -> dict:
        Loads a JSON file into a Python dictionary.
    
    load_sqlite(filepath: str) -> sqlite3.Connection:
        Loads an SQLite database file into a sqlite3 Connection object.
    
    load_zip(filepath: str, extract_dir: Optional[str] = None) -> None:
        Extracts the contents of a ZIP file into the current directory or a specified directory.
    
    load_file(filepath: str) -> Any:
        Dynamically loads a file based on its extension using a registered loader function.
        Returns the loaded data, or None if the file type is unsupported.
    
    load_input_data(input_dir: str = '/kaggle/input') -> None:
        Walks through the input directory and dynamically loads all files using their respective
        loaders. Files are loaded into variables based on their names:
        - CSV files are loaded into pandas DataFrames with '_df' appended to the variable name.
        - JSON files are loaded into Python dictionaries using the file name as the variable name.
        - SQLite files are loaded as sqlite3 Connection objects.
        - ZIP files are extracted but not stored in a variable (can be expanded in the future).

        Args:
            input_dir (str, optional): The directory to search for files. Defaults to '/kaggle/input'.

        Example:
            After calling `load_input_data()`, you can access loaded data directly:
            - A CSV file `/kaggle/input/example.csv` is accessible as `example_df`.
            - A JSON file `/kaggle/input/data.json` is accessible as `data`.
            - An SQLite file `/kaggle/input/database.sqlite` is accessible as `database`.
            - ZIP files are extracted automatically but not assigned to variables.
        
        Notes:
            - This script uses `globals()` to dynamically assign variables in the global scope.
            - Support for additional file types can be added by writing a loader function and
              registering it in the `file_loaders` dictionary.
"""


import os
import pandas as pd
import json
import sqlite3
import zipfile
from typing import Any, Callable, Optional


def load_csv(filepath: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(filepath)


def load_json(filepath: str) -> dict:
    """Load a JSON file into a dictionary."""
    with open(filepath, 'r') as file:
        return json.load(file)


def load_sqlite(filepath: str) -> sqlite3.Connection:
    """Load an SQLite database file into a sqlite3 connection."""
    return sqlite3.connect(filepath)


def load_zip(filepath: str, extract_dir: Optional[str] = None) -> str:
    """
    Extract a ZIP file to a given directory or the current directory and return the extraction directory.
    
    :param filepath: Path to the ZIP file.
    :param extract_dir: Directory to extract the contents. If None, extracts to the current directory.
    :return: The directory where the contents are extracted.
    """
    if extract_dir is None:
        extract_dir = os.path.splitext(filepath)[0]  # Extract to a folder named after the ZIP file
    
    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    return extract_dir


# Dictionary that maps file extensions to their corresponding loader functions
file_loaders: dict[str, Callable[[str], Any]] = {
    '.csv': load_csv,
    '.json': load_json,
    '.sqlite': load_sqlite,
    '.zip': load_zip,
    # Add more loaders here for other file types
}


def load_file(filepath: str) -> Any:
    """
    Dynamically load a file based on its extension using a registered loader function.
    If the file type is not supported, returns None.
    
    :param filepath: Path to the file to load.
    :return: The loaded data, or None if the file type is unsupported.
    """
    ext = os.path.splitext(filepath)[1]  # Get file extension
    loader = file_loaders.get(ext)
    
    if loader:
        return loader(filepath)
    else:
        print(f"Unsupported file type: {ext}")
        return None


def load_input_data(input_dir: str = '/kaggle/input', scope: dict = None) -> None:
    """
    Walk through the input directory and load files into separate variables in the provided scope.
    Appends '_df' to DataFrame variables for CSV files and '_dict' to dictionary variables for JSON files.
    If a ZIP archive is encountered, it is extracted, and the files inside are processed recursively.
    
    :param input_dir: The base directory where input files are located.
    :param scope: The dictionary representing the calling scope (e.g., globals() or locals()).
    """
    if scope is None:
        scope = globals()  # Default to the global scope

    for dirname, _, filenames in os.walk(input_dir):
        for filename in filenames:
            filepath = os.path.join(dirname, filename)
            data = None
            
            # Handle ZIP files by extracting and processing their contents recursively
            if filename.endswith('.zip'):
                extract_dir = load_zip(filepath)  # Extract the ZIP file
                load_input_data(extract_dir, scope)  # Recursively process extracted files
                
            else:
                data = load_file(filepath)  # Process regular files (CSV, JSON, etc.)
            
            if data is not None:
                # Create a variable name from the file name (without extension)
                file_key = os.path.splitext(filename)[0]
                
                # If the file is a DataFrame, append '_df' to the variable name
                if isinstance(data, pd.DataFrame):
                    file_key += '_df'
                
                # If the file is a Dictionary (JSON), append '_dict' to the variable name
                elif isinstance(data, dict):
                    file_key += '_dict'
                
                # Inject the variable into the provided scope (global or local)
                scope[file_key] = data
                print(f"Loaded '{file_key}' as a {type(data).__name__} from {filename}")

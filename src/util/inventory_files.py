# %% [code]
import os

def inventory_files(parent_dir='/kaggle', max_files=5, max_depth=2):
    """
    Walk through Kaggle directories starting from the parent directory and print up to max_files per directory.
    Optionally restrict the depth of the directory tree traversal with max_depth.

    This function inventories directories and files, specifically identifying utility scripts 
    in subdirectories under '/kaggle/usr/lib/'. Utility scripts are listed as subdirectory names, 
    while other files are listed as "Filename".

    Args:
        parent_dir (str): The base directory to start the walk from. Defaults to '/kaggle'.
        max_files (int): The maximum number of files to display per directory. Defaults to 5.
        max_depth (int): The maximum depth to walk into the directory structure. Defaults to 2.

    Example Usage:
        # Call this utility script to inventory files in the notebook environment:
        from walk_directories import walk_directories
        walk_directories(parent_dir='/kaggle', max_files=5, max_depth=3)

    The function will output the structure of directories and files within the specified depth, 
    differentiating between utility scripts in '/kaggle/usr/lib/' and regular files in other directories.

    Output Example:
        # Walking directory: /kaggle
        Directory: /kaggle
        Directory: /kaggle/lib
        Directory: /kaggle/usr/lib
          Utility Scripts: util_script1
          Utility Scripts: util_script2
        Directory: /kaggle/input
          Filename: /kaggle/input/sample_data.csv
    """
    
    print(f"\n# Walking directory: {parent_dir}")
    parent_dir_depth = parent_dir.rstrip(os.sep).count(os.sep)

    # Walk the directory tree starting from the parent directory
    for root, dirs, files in os.walk(parent_dir):
        # Calculate current directory depth
        current_depth = root.count(os.sep) - parent_dir_depth
        
        # Stop if the current depth exceeds max_depth
        if max_depth is not None and current_depth > max_depth:
            continue
        
        # Handle /kaggle/usr/lib/ directories as utility scripts
        if root == '/kaggle/usr/lib':  # Detect utility script subdirectories
            print(f"Directory: {root}")
            for subdir in dirs[:max_files]:  # Limit to the first max_files utility scripts
                print(f"  Utility Scripts: {subdir}")
        else:
            print(f"Directory: {root}")
            
            # Limit to the first max_files files in each directory
            for filename in files[:max_files]:
                print(f"  Filename: {os.path.join(root, filename)}")
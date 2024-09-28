# src/

The `src/` directory contains the main source code for the project. As the core of the application, this directory will grow and evolve as students develop their skills, ranging from writing simple functions to implementing advanced architectures such as object-oriented programming (OOP), modular designs, and even complex patterns like hexagonal architecture.

## Purpose

The `src/` directory is where the application's codebase resides. It is structured to support both small-scale projects and more complex, modular systems. As students advance, this directory will serve as the foundation for organizing their code in a maintainable, scalable way.

## Usage Examples

### Beginner Level

- **Single Script Applications**: For beginners, the `src/` directory may simply contain a few Python or C/C++ files, each performing a specific task.
  - **Example**: A standalone Python script for performing basic data analysis or a C program for handling file input/output.

### Intermediate Level

- **Object-Oriented Programming (OOP)**: As students progress, they will start organizing their code using OOP principles, defining classes and methods that encapsulate functionality.
  - **Example**: A Python project that uses classes to define different entities, such as data parsers or model objects, to handle more complex tasks.

- **Multiple Modules**: Intermediate students will learn how to break down their application into multiple modules, making their code more modular and reusable.
  - **Example**: A project with separate modules for data preprocessing, model training, and result evaluation, all organized into different files or subdirectories within `src/`.

### Advanced Level

- **Hexagonal Architecture**: At an advanced level, students may adopt more sophisticated design patterns like hexagonal (or "ports and adapters") architecture. This approach separates core business logic from external dependencies (e.g., databases, APIs), making the system easier to maintain and test.
  - **Example**: An application structured with layers, including core logic in one directory and interfaces for external systems (e.g., file storage, web APIs) in another.

- **Domain-Driven Design (DDD)**: Students may also learn to implement DDD, where subdomains of an application are broken down into smaller, manageable pieces. These can be organized into subdirectories within `src/`, each handling a specific part of the system.
  - **Example**: Separate directories for user management, data processing, and reporting, each with its own domain logic and interfaces.

## Structure

As the project grows in complexity, you can introduce subdirectories within `src/` to manage different aspects of the application:

```plaintext
src/
├── main.py             # Entry point for simple projects
├── utils.py            # Utility functions for general use
├── models/             # Models for data representation or machine learning
├── services/           # Business logic and service layer
├── adapters/           # Interfaces for external systems (APIs, databases)
├── config.py           # Configuration settings for the application
└── README.md           # This readme file
```

### Suggested Subdirectories

- **`models/`**: Store data models or machine learning models that represent the core entities in the system.
- **`services/`**: Contain the business logic and service layer, handling application-specific tasks like data processing, model training, or inference.
- **`adapters/`**: Organize external interfaces, such as APIs or database connections, in line with principles from hexagonal architecture.
- **`utils/`**: Include utility scripts or functions that are reused across the application but don't belong in the core logic.

## Guidelines

- **Code Organization**: As the project evolves, ensure that your code is organized logically into subdirectories, each responsible for a specific concern (e.g., models, services, adapters).
- **Modularity**: Write code in a modular fashion so that different parts of the application can be reused or updated independently.
- **Maintainability**: Follow clean coding practices such as using descriptive variable names, writing clear comments, and adhering to PEP 8 (for Python) or other coding standards relevant to the language you're using.

## Best Practices

- **Single Responsibility Principle**: Each file, class, or function should have a single responsibility, making it easier to test and maintain.
- **Testability**: Keep your code organized and modular to make unit testing easier. Advanced students will eventually learn how to write tests for different components of the system.
- **Version Control**: As your project grows, make sure to version control your code, using meaningful commit messages and adhering to Git best practices.

## Example Progression

Here’s how the `src/` directory may evolve over time:

1. **Single Script**:
   ```plaintext
   src/
   └── main.py        # A single Python script handling all functionality
   ```

2. **OOP and Modular Design**:
   ```plaintext
   src/
   ├── main.py        # Entry point, orchestrating functionality
   ├── utils.py       # Utility functions
   └── data_loader.py # Class for loading and preprocessing data
   ```

3. **Hexagonal Architecture**:
   ```plaintext
   src/
   ├── core/          # Core business logic
   │   ├── models/    # Domain models
   │   └── services/  # Application services
   ├── adapters/      # Interfaces for external systems
   └── config.py      # Configuration settings
   ```

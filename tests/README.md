# tests/

The `tests/` directory is dedicated to storing all test-related code for ensuring the correctness and reliability of your project. Tests are divided into three categories: **unit tests**, **integration tests**, and **end-to-end (e2e) tests**. Testing is a crucial part of software development, helping to identify bugs early and ensure that the code behaves as expected under various conditions.

## Purpose

The `tests/` directory helps organize different types of tests to verify the functionality of individual components, their integration, and the overall application. This directory is essential for students learning how to write and run automated tests to ensure code quality, maintainability, and robustness.

### Subdirectories

```plaintext
tests/
├── unit/          # Unit tests for individual functions or classes
├── integration/   # Integration tests for multiple components working together
├── e2e/           # End-to-end tests to validate the entire system
└── README.md      # This readme file
```

- **`unit/`**: Contains tests for individual functions or classes to ensure that each component behaves as expected in isolation.
- **`integration/`**: Contains tests for verifying that different parts of the system work together correctly.
- **`e2e/`**: Contains end-to-end tests that simulate real-world usage scenarios, validating the entire application workflow from start to finish.

## Testing Tools

### Python

For Python-based projects, we will use the following tools:

- **`pytest`**: A powerful testing framework that simplifies writing tests for Python code.
- **`coverage.py`**: A tool that measures code coverage, providing insights into how much of your code is covered by tests.

### C/C++

For C/C++ projects, there are several testing frameworks available:

- **`Google Test` (gtest)**: A popular C++ testing framework that supports writing unit and integration tests.
- **`gcov`**: A tool for measuring code coverage in C/C++ projects. It works alongside `gcc` and provides detailed coverage reports.

### NASM (x86/64 Assembly)

Testing assembly code is more challenging, but it can still be accomplished:

- **Custom Test Harness**: For NASM, it's common to write custom test harnesses in C or assembly that execute the assembly code and verify the results.
- **Debuggers**: Tools like `gdb` (GNU Debugger) can help test and debug assembly code, checking the state of registers and memory to ensure correctness.

## Test Coverage

**Code coverage** is a metric that shows how much of your code is exercised by tests. Measuring coverage is essential to ensure that your tests adequately verify the critical parts of your application. The goal is to achieve as close to 100% coverage as possible, but focus on covering the most important and risk-prone areas of your code.

### Coverage for Python

In Python, we will use `coverage.py` to measure how much of the code is covered by tests. To run tests and generate a coverage report, use the following commands:

```bash
# Run tests with coverage
pytest --cov=src tests/

# Generate an HTML coverage report
coverage html
```

### Coverage for C/C++

For C/C++ projects, you can use `gcov` to measure coverage. This involves compiling your project with coverage information enabled:

```bash
# Compile with coverage flags
gcc -fprofile-arcs -ftest-coverage -o main src/main.c

# Run your program and generate coverage data
./main

# Generate a coverage report
gcov main.c
```

### Testing and Coverage for NASM

Assembly testing is more manual, but you can integrate simple tests by writing C or assembly programs that invoke your assembly code and check results. Coverage tools like `gcov` do not natively support assembly, so debugging tools and manual checking will be needed.

## Instructor-Provided vs. Student-Written Tests

### Beginner Students

For less experienced students, **instructors will likely provide a set of pre-written tests** to help guide the learning process. These tests will focus on verifying the correct behavior of student code without requiring students to write their own tests. This allows beginners to focus on writing the functionality rather than learning the complexities of test writing.

- **Example**: Instructors might provide unit tests for simple Python functions or C programs, verifying correct inputs and outputs.

### Advanced Students

As students gain experience, they will be expected to **write their own tests** for their code. Advanced students should be able to write comprehensive unit, integration, and end-to-end tests for their projects. Writing tests is a critical skill in professional software development, and students will need to demonstrate an understanding of how to verify their own code.

- **Example**: Advanced students might write unit tests for each class in a Python project, integration tests for interacting modules, and e2e tests that simulate the full workflow of the application.

## Example Workflow for Running Tests

1. **Run Unit Tests**:
   ```bash
   pytest tests/unit/
   ```

2. **Run Integration Tests**:
   ```bash
   pytest tests/integration/
   ```

3. **Run All Tests with Coverage**:
   ```bash
   pytest --cov=src tests/
   ```

4. **View Coverage Report**:
   ```bash
   coverage html
   # Open the generated 'htmlcov/index.html' file in a browser
   ```

## Best Practices

- **Test Early and Often**: Ensure that tests are run regularly as part of the development process. The earlier you catch bugs, the easier they are to fix.
- **Aim for High Coverage**: Strive for high test coverage, but remember that quality is more important than quantity. Focus on testing critical code paths.
- **Automate Testing**: Advanced students should integrate their tests with Continuous Integration (CI) systems (like GitHub Actions) to automatically run tests whenever code is pushed.
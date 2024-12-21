# Testing Guidelines for EcoCode

This document provides guidelines for testing EcoCode, including setup instructions, test execution, and best practices for contributing to the test suite.

## Test Setup

### Prerequisites

1. Ensure you have Python 3.8 or higher installed.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install additional test dependencies:

   ```bash
   pip install pytest coverage
   ```

4. Navigate to the `src/tests` directory to access the test suite.

## Running Tests

### Unit Tests

Run all unit tests in the project:

```bash
pytest
```

### Test Coverage

Generate a test coverage report:

```bash
coverage run -m pytest
coverage report -m
```

### Specific Tests

Run a specific test file:

```bash
pytest src/tests/test_dynamic_profiler.py
```

Run a specific test case:

```bash
pytest src/tests/test_dynamic_profiler.py::test_function_name
```

### Debugging Tests

Use verbose mode for more detailed output:

```bash
pytest -v
```

## Test Structure

- **Unit Tests**: Located in `src/tests/`. Each module in `src/ecocode/` has a corresponding test file (e.g., `test_dynamic_profiler.py`).
- **Integration Tests**: Located alongside unit tests and test the interaction between modules.
- **Example Scripts**: Found in the `examples/` directory for end-to-end testing.

## Writing Tests

Follow these steps to write new tests:

1. Add a new test function in the appropriate file (e.g., `test_your_module.py`).
2. Use descriptive names for test functions.
3. Use the `pytest` framework for assertions:
   ```python
   def test_example():
       result = some_function()
       assert result == expected_output
   ```
4. Add comments to explain the purpose of each test.

## Best Practices

- Write tests for all new features and bug fixes.
- Aim for high test coverage (80%+).
- Keep tests modular and independent.
- Use mocks to isolate tests from external dependencies.

## Troubleshooting

If tests fail:

1. Check the error messages in the output.
2. Verify that all dependencies are installed.
3. Ensure you are using the correct Python version.
4. Debug by adding print statements or using a debugger (e.g., `pdb`).

## Reporting Issues

If you encounter issues while running tests, please:

1. Open an issue on the [https://github.com/xploit13/ecocode](https://github.com/xploit13/ecocode).
2. Provide details about the error, including logs and steps to reproduce.

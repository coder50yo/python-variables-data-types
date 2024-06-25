# Variables and Data Types Python Project

This project demonstrates the use of different variables and data types in Python. It covers basic types such as integers, floats, strings, booleans, lists, tuples, dictionaries, sets, and NoneType.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setting Up the Project](#setting-up-the-project)
- [Running the Script](#running-the-script)
- [Running the Tests](#running-the-tests)
- [Explanation of the Code](#explanation-of-the-code)
- [Using `.gitignore`](#using-gitignore)
- [Additional Resources](#additional-resources)

## Prerequisites

- [Python](https://www.python.org/downloads/) installed on your system
- [Git](https://git-scm.com/downloads) installed on your system

## Project Structure

The project has the following structure:

```
variables-data-types/
│
├── .gitignore
├── variables.py
├── test_variables.py
└── README.md
```

- `variables.py`: Contains examples of variables and data types in Python.
- `test_variables.py`: Contains unit tests for the variables and data types.
- `.gitignore`: Specifies files and directories to ignore in the Git repository.
- `README.md`: Provides information on setting up and running the project.

## Setting Up the Project

1. **Clone the Repository**

   First, clone the repository to your local machine. Open your terminal and run the following command:

   ```sh
   git clone https://github.com/coder50yo/python-variables-data-types.git
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```sh
   cd variables-data-types
   ```

## Running the Script

To run the script, execute the following command in your terminal:

```sh
python3 variables.py
```

The script will print out examples of different variables and data types in Python.

## Running the Tests

To run the unit tests, execute the following command in your terminal:

```sh
python3 -m unittest test_variables.py
```

You should see output indicating that all tests passed.

## Explanation of the Code

### `variables.py`

The `variables.py` script demonstrates the use of various data types in Python. It includes examples of:
- Integer
- Float
- String
- Boolean
- List
- Tuple
- Dictionary
- Set
- NoneType

### `test_variables.py`

The `test_variables.py` script contains unit tests for each variable type defined in `variables.py`. It uses the `unittest` framework to ensure that each variable is of the correct type and has the expected value.

## Using `.gitignore`

The `.gitignore` file specifies files and directories that Git should ignore. Common entries include:
- `__pycache__/`: Python's bytecode cache directory
- `*.pyc`: Compiled Python files
- `venv/`, `env/`: Virtual environment directories

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Git Official Documentation](https://git-scm.com/doc)
- [unittest Documentation](https://docs.python.org/3/library/unittest.html)
# Student Report Package

## Project Overview

A Python package that reads student marks from a CSV file, calculates student performance statistics, and displays a formatted report.

## Project Structure

```text
student-report/
├── src/
│   └── student_report/
│       ├── __init__.py
│       ├── main.py
│       ├── loader.py
│       ├── analysis.py
│       └── formatting.py
├── tests/
│   └── test_analysis.py
├── students.csv
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.11 or later
- No external dependencies required.

## How to Run

Open PowerShell in the project root and run:

```powershell
$env:PYTHONPATH = "src"
python -m student_report.main
```

## How to Run Tests

```powershell
python tests/test_analysis.py
```

The tests use plain Python `assert` statements without an external testing framework.

## Absolute Imports

This project uses absolute imports, such as:

```python
from student_report.loader import load_students
```

Absolute imports clearly identify where a module comes from. They make the code easier to understand and maintain because the complete package path is visible. Relative imports use dots to refer to modules within the same package, but can be less clear when learning or navigating a larger project. Absolute imports also make the intended module location explicit.

## Circular Import Experiment

To understand circular imports, I deliberately added:

```python
# loader.py
from student_report.analysis import calculate_average

# analysis.py
from student_report.loader import load_students
```

This caused the following error:

```text
ImportError: cannot import name 'load_students' from partially initialized module 'student_report.loader' (most likely due to a circular import)
```

### Why did it happen?

The loader module imported the analysis module, while the analysis module tried to import the loader module again. Python was still initializing the loader module when the second import happened. Therefore, `load_students` was not yet available.

### How was it fixed?

I removed the unnecessary imports between these two modules. The `main.py` module coordinates the loader, analysis, and formatting modules. This keeps responsibilities separate and prevents circular dependencies.

## Written Answers

### 1. What does `if __name__ == '__main__'` do and why is it needed?

In Python, `__name__` is a special variable that identifies how a module is being used. When a Python file runs directly, its value becomes `__main__`. When the file is imported into another module, its value becomes the module's name. The condition `if __name__ == '__main__':` ensures that the code inside it runs only when the file is executed as the main program. It prevents the main function from running automatically when another file imports the module. This makes code reusable, easier to test, and helps avoid unwanted execution during imports.

### 2. How does Python decide where to find an imported module?

Python uses a search path called `sys.path` to locate imported modules. It first checks whether the module is already loaded in `sys.modules`. If not, Python's import system searches available locations, commonly including the script or current working directory, directories added through the `PYTHONPATH` environment variable, standard library locations, and installed package directories such as `site-packages`. When Python finds the requested module or package, it loads it and makes it available for use. In this project, setting `PYTHONPATH` to `src` allows Python to locate the `student_report` package.
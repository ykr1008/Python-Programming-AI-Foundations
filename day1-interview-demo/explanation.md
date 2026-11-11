When I start a new Python project, I first create a dedicated project directory and initialise a virtual environment using `python -m venv venv`. I activate the environment before installing any dependencies.

A virtual environment isolates the project's installed packages from other Python projects on my machine. For example, one project might require version 2 of a library while another needs version 3. Without isolation, installing or upgrading packages for one project could break the other.

After activation, I install the required packages using `python -m pip install requests rich`. I then generate a `requirements.txt` file using `python -m pip freeze`. This records the installed packages and their exact versions, helping other developers reproduce the dependency setup and reducing unexpected problems caused by version changes.

Next, I initialise a Git repository and add a `.gitignore` file to exclude the virtual environment, `__pycache__` directories, and compiled Python files. I commit the initial project configuration so the setup is tracked in version control.

Activation also modifies the current terminal's `PATH` by placing the virtual environment's executable directory first. Consequently, commands such as `python` and `pip` resolve to the environment's interpreter and packages. I verify this using `python -m pip --version` and `where.exe python`, comparing the results inside and outside the environment.

This approach keeps projects reproducible, isolated, and easier to maintain.
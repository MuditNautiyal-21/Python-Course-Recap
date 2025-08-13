'''
Virtual Environments:

A virtual environment is a self-contained directory that contains its own Python interpreter and libraries.

Now what this means?
This means that libraries installed in one virtual environment won't interfere with the libraries in the other.

One can install virtual environment using pip install virtualenv

Below are instructions to be executed in terminal of the IDE:
- After installation, to create a virtual environment, we can write "python -m venv environment_name" It will be created in the same dir.
- How to Activate: .\environment_name\Scripts\Activate.ps1
or just:
\environment_name\Scripts\activate


- If we need to install any package, we install using pip - pip install package_name, but they will be available throughout your system or programs.

 v1 - package 1 (pandas)
 v2 - package 2 (numpy)
 v3 - package (moviepy)

- Now some project uses a specific version of these packages and the other uses another one.

- We can separate the version installs.

- Now lets say you want to check all the installed packages in a virtual environment: "pip list" (This is only after the environment is activated).

- One can also upgrade the package using "pip install --upgrade packages_name"

- Uninstalling a package - "pip uninstall package_name"

- How to generate a requirements.txt file? - "pip freeze > requirements.txt": This will list the packages being used for a certain project or environment

- To deactivate the virtual environment: "deactivate"

- Lets say one has to install all the packages required for a certain project (given in requirements.txt file) in one go - "pip install -r requirements.txt"


Note: All these commands are to be processed (run) in the terminal of the IDE or wherever your project or code file is (but in a terminal) you can run it in the code file as well but that has a bit different method for each IDE.
'''
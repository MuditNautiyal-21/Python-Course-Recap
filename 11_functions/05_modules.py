# import helps pulling the already existing code encapsulated as a module into a new code.

'''
There are 2 types of modules in python:
- Built-in Modules.
- External Modules.

We can look for built-in modules of python on docs.python.org/3/py-modindex.html
The link url can change in the future depending on the version of python that is currently going on!
'''

import math
import os # Its not being used thats why its color is a bit faded. Thats how python tells us that there is something un-used.

import mymodule

print(math.sqrt(16))
mymodule.hello() # We called in our own module.

# External Modules: Can be installed using 'PIP' for example 'pip install requests

import requests

r = requests.get("https://www.google.com")

print(r.status_code)
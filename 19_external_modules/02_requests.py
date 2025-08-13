'''
Request:

Basic Understanding: It can be used to scrape or request data from an external source like web pages.

The requests library simplifies making HTTP requests. This is essentiall for interacting with web APIs which is an abreviation of Application Programming Interface.
'''

import requests

r = requests.get("https://api.github.com/users/MuditNautiyal-21")

# print(r.text)

with open("Mudit_Nautiyal.txt", "w") as f:
    f.write(r.text)

# This was an example of get request.
# You can also make a post request.

'''
Post request is a bit complicated than get request.

- In post request we have a URL and some data that is to be sent to that URL.
'''

# r = requests.post("https://httpbin.org/post", data = {key:Value}) # This is how you can make a post request. You need to get your data aligned.
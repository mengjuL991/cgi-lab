#!/usr/bin/env python3

import os
import json

#print out all env variables as plain text

#print('Content-Type: text/plain')
#print()
#print(os.environ)

#print env variables as json

#print('Content-Type: application/json')
#print()
#print(json.dumps(dict(os.environ), indent = 2))

#print query parameter data in html

print('Content-Type: text/html')
print()
#print(f"<p>QUERY_STRING = {os.environ['QUERY_STRING']}</p>")
print(f"<p>HTTP_USER_AGENT = {os.environ['HTTP_USER_AGENT']}</p>")

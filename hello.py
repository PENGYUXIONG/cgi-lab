#!/usr/bin/env python3

import os, json
import cgi, cgitb
from templates import login_page, _wrapper

cgitb.enable()
#print('Content-Type: application/json')
#print()
#print(json.dumps(dict(os.environ), indent= 2))


# print('Content-Type: text/html')
# print()
# print("""
# <!doctype html>
# <html>
# <body>
# <h1>Query</h1>
# """)

# print("<ul>")
# for para in os.environ['QUERY_STRING'].split('&'):
#     (name, value) = para.split('=')
#     print(f"<li><em>{name}</em> = {value}</li>")

# print("</ul>")

# print("""
# </body>
# </html>
# """)

# print('Content-Type: text/html')
# print()
# print("""
# <!doctype html>
# <html>
# <body>
# <h1>User browser</h1>
# """)

# print(f"<p> HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")

# print("""
# </body>
# </html>
# """)

print(login_page())
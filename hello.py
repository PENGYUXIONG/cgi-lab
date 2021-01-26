#!/usr/bin/env python3

import os, json
import cgi, cgitb
cgitb.enable()
#print('Content-Type: application/json')
#print()
#print(json.dumps(dict(os.environ), indent= 2))


print('Content-Type: application/html')

print("""
<!doctype html>
<html>
<body>
<h1>Hello<h1/>
</body>
</html>
    """
)

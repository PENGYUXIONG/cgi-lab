#!/usr/bin/env python3
import cgi
import cgitb
from templates import login_page, secret_page, after_login_incorrect
import os, json
import secret
from http.cookies import SimpleCookie

#question 4
print("Content-Type: text/html\n")
#print()

#print(os.environ)
print(json.dumps(dict(os.environ), indent= 2))
#print(login_page())
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

#question 5


form_ok = username == secret.username and password == secret.password
c = SimpleCookie(os.environ["HTTP_COOKIE"])
c_username = None
c_password = None
if c.get("username"):
    c_username = c.get("username").value
if c.get("password"):
    c_username = c.get("password").value

cookie_ok = c_username == secret.username and c_password == secret.c_password

if cookie_ok:
    username = c_username
    password = c_password

if form_ok:
    print("Set-Cookie: username= ", username)
    print("Set-Cookie: password= ", password)
#print()

#question6

if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username,password))
else:
    print(after_login_incorrect())
import os
execfile("config.py")
print content_type_charset
print
print
print open("./header.html").read()
form = cgi.FieldStorage()
infofile = open("./postinfo")
posts = []

#!/usr/bin/env python

execfile("header.py")
if "page" not in form:
    page = 5
else:
    page = int(form.getvalue('page'))*5
minpage = page - 5
counter = 0
entries = infofile.read().split("--------------------")
for entry in entries:
    entry = entry.split("\n")
    td = datetime.datetime.now() - datetime.datetime.strptime(entry[3], "%b %d %Y")
    timediff = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6
    if 0 < timediff:
        if page == 0:
            posts.append(entry)
        elif minpage <= counter < page:
            posts.append(entry)
        counter = counter + 1

execfile("display.py")
search = False
execfile("page.py")
execfile("footer.py")

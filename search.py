execfile("header.py")
if "q" not in form or form.getvalue('q') == "":
    execfile("index.py")
else:
    if "page" not in form:
        page = 5
    else:
        page = int(form.getvalue('page'))*5
    minpage = page - 5
    counter = 0
    prefix = "./p/"
    entries = infofile.read().split("--------------------")
    for entry in entries:
        entry = entry.split("\n")
        td = datetime.datetime.now() - datetime.datetime.strptime(entry[3], "%b %d %Y")
        timediff = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6
        if 0 < timediff:
                for e in entry:
                    if e.find(form.getvalue('q')) != -1:
                        if minpage <= counter < page:
                            posts.append(entry)
                        counter = counter + 1
                    elif e == entry[4]:
                        htmlfile = open(prefix + e, 'r')
                        html = htmlfile.read()
                        htmlfile.close()
                        if html.lower().find(form.getvalue('q').lower()) != -1:
                            if minpage <= counter < page:
                                posts.append(entry)
                            counter = counter + 1
    execfile("display.py")
    search = True
    execfile("page.py")
execfile("footer.py")

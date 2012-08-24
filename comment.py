#!/usr/bin/env python

execfile('config.py')

validPost = False
entries = infofile.read().split("--------------------")
for entry in entries:
    entry = entry.split("\n")
    if entry[4] == form.getvalue('Post') + ".html":
        validPost = True
if validPost == False:
    print "Status: 400 Bad Request\n\n"
else:
    ip = cgi.escape(os.environ["REMOTE_ADDR"])
    date = datetime.datetime.now().isoformat()
    comment = form.getvalue('comment').replace('"', "&quot;").replace('<', '&lt;').replace('>', '&gt;').replace("\n", "&#10;").replace("\r", "&#13;")
    author = form.getvalue('author').replace('"', "&quot;").replace('<', '&lt;').replace('>', '&gt;')
    post = form.getvalue('Post')
    approved = '0'
    if autoapproved:
        approved = '1'
    if not os.path.exists('commentlist.'+post):
        cmntfile = open('commentlist.'+post, 'w')
        cmntfile.write('--------------------' + "\n")
        cmntfile.close()
    commentfile = open('commentlist.'+post, 'a+')
    query = post + "\n" +  author + "\n" + date + "\n" + ip + "\n" + comment + "\n" + approved + "\n" + '--------------------'
    commentfile.write(query)
    commentfile.close()
    print "Status: 303 See Other"
    print "Location: "+url+"\n\n"

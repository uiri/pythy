#!/usr/bin/env python

execfile("header.py")
postnum = 0
minpostnum = 0
entries = infofile.read().split("--------------------")
for entry in entries:
    entry = entry.split("\n")
    td = datetime.datetime.now() - datetime.datetime.strptime(entry[3], "%b %d %Y")
    timediff = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6
    if timediff > 0:
        if form.getvalue('post') != None:
            if entry[4] == form.getvalue('post') + ".html":
                posts.append(entry)
                postnum = entries.index("\n".join(entry))
        elif form.getvalue('oldpost') != None:
            if entry[1].lower().replace(" ", "-") == form.getvalue('oldpost'):
                posts.append(entry)            
        elif len(posts) == 0:
            postnum = postnum + 1
    else:
        minpostnum = minpostnum + 1
if len(posts) == 0:
    print open("404.html").read()
else:
    execfile("display.py")
    postnav = ""
    if postnum > minpostnum:
        postnav += """<span class="newpost"><a href="""+url+"posts/" + entries[postnum-1].split("\n")[4].split(".")[0] + """/>&laquo; Next Post</a></span>"""
    if postnum < len(entries)-1:
        postnav += """                <span class="oldpost"><a href="""+url+"posts/" + entries[postnum+1].split("\n")[4].split(".")[0] + """/>Previous Post &raquo;</a></span>"""
    if iscommentingopen:
        commentpost = posts[0][4].split(".")[0]
        comments = []
        if os.path.isfile("commentlist."+commentpost):
            commentslistfile = open("commentlist."+commentpost).read().split("--------------------")
            for comment in commentslistfile:
                comments.append(comment.split("\n")[1:])
                if comments[-1] == []:
                    comments.pop()
                elif comments[-1][0] != commentpost:
                    comments.pop()
                elif comments[-1][3] in banlist or not bool(comments[-1][5]):
                    comments.pop()
        commentstext = ""
        if len(comments):
            if len(comments) == 1:
                respnum = "1 Response"
            else:
                respnum = str(len(comments)) + " Responses"
            commentstext += """<ul class="commentlist">"""
            for comment in comments:
                commentstext += open("comment.html").read().replace("{{author}}", comment[1]).replace("{{date}}", iso8601.parse_date(comment[2]).strftime('%b %d %Y at %H:%M')).replace("{{content}}", comment[4])
            commentstext += """</ul>"""
        else:
            respnum = "No Responses"
            commentstext = ""
        print open("post.html").read().replace("{{postnav}}", postnav).replace("{{respnum}}", respnum).replace("{{title}}", posts[0][1]).replace("{{comments}}", commentstext).replace("{{postto}}", commentpost)
execfile("footer.py")

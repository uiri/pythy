import cgi
import datetime
import time
import PyRSS2Gen

execfile("rssconf.py")
page = 10
minpage = 0
counter = 0
infofile = open("postinfo")
entries = infofile.read().split("--------------------")
infofile.close()
posts = []
for entry in entries:
    entry = entry.split("\n")
    td = datetime.datetime.now() - datetime.datetime.strptime(entry[3], "%b %d %Y")
    timediff = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6
    if 0 < timediff:
        if minpage <= counter < page:
            descriptfile = open("./p/" + entry[4], 'r')
            descript = descriptfile.read()
            descriptfile.close()
            e = PyRSS2Gen.RSSItem(
                title = entry[1],
                link = url + "posts/" + entry[4].split(".")[0] + "/",
                description = descript[0:300] + "...",
                guid = PyRSS2Gen.Guid(url + "posts/" + entry[4].split(".")[0] + "/"),
                pubDate = datetime.datetime.strptime(entry[3], "%b %d %Y")
                )
            posts.append(e)
        counter = counter + 1
rss = PyRSS2Gen.RSS2(
    xmltitle,
    url,
    xmldescription,
    lastBuildDate = datetime.datetime.utcnow(),

    items = posts
)
print "Content-type: text/xml;charset=UTF-8"
print 
print rss.to_xml()

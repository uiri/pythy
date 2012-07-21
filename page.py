page = page/5
newoldnav = ""
if page > 1:
    newerpage = page - 1
    if search == False:
        newpageurl =  url+"page/" + str(newerpage) + "/"
        newpagetext = "Newer Posts"
    else:
        newpageurl = url+"search.py?q=" + form.getvalue('q') + "&page=" + str(newerpage)
        newpagetext = "Previous Results"
    newoldnav += """          <span class="newpost"><a href="{{newpagelink}}">&laquo; {{newpagetext}}</a></span>""".replace("{{newpagelink}}", newpageurl).replace("{{newpagetext}}", newpagetext)
lastpage = counter/5 + 1
if counter%5 == 0:
    lastpage -= 1
if 0 < page < lastpage:
    olderpage = page + 1
    if search == False:
        oldpageurl = url+"page/"+ str(olderpage) + "/"
        oldpagetext = "Older Posts"
    else:
        oldpageurl = url+"search.py?q=" + form.getvalue('q') + "&page=" + str(olderpage)
        oldpagetext = "More Results"
    newoldnav += """          <span class="oldpost"><a href="{{oldpagelink}}">{{oldpagetext}} &raquo;</a></span>""".replace("{{oldpagelink}}", oldpageurl).replace("{{oldpagetext}}", oldpagetext)
pagination = ""
pagelink = open("pagelink.html").read()
for i in range(lastpage):
    j = i + 1
    if j != page:
        if search == False:
            if j == 1:
                pagination += pagelink.replace("{{url}}", url).replace("{{num}}", str(j))
            else:
                pagination += pagelink.replace("{{url}}", url+"page/"+str(j)+"/").replace("{{num}}", str(j))
        else:
            pagination += pagelink.replace("{{url}}", url+"search.py?q=" + form.getvalue('q') + "&page=" + str(j)).replace("{{num}}", str(j))
    else:
            pagination += str(j)
print open("page.html").read().replace("{{navlinks}}", newoldnav).replace("{{pagecontents}}", pagination)

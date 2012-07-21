for post in posts:
    td = datetime.datetime.now() - datetime.datetime.strptime(post[3], "%b %d %Y")
    timediff = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6
    try:
        textfile = open(prefix + post[4], 'r')
        text = textfile.read()
        textfile.close()
    except:
        text = post[4]
    postlink = post[4].split(".")[0]
    if post[2].lower() in authortoname:
        noticeauthor = authortoname[post[2].lower()]
    else:
        noticeauthor = post[2]
    if 0 < timediff:
        print open('display.html').read().replace("{{notice}}", notice.replace("{{noticeauthor}}", noticeauthor)).replace("{{text}}", text).replace("{{author}}", post[2]).replace("{{date}}", post[3]).replace("{{postlink}}", url+"posts/"+postlink).replace("{{posttitle}}", post[1])

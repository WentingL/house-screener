#decode
# "u" means unicode
#put code below in shell directly
#content
u"\u4eca\u665a\u624d\u5f00\u59cb\u9996\u64ad\uff0c\u64ad\u653e\u91cf\u90fd\u52301.4\u4ebf\u4e86\uff0c\u4e0d\u5f97\u4e0d\u670d\u9b3c\u5439\u706f\u7cfb\u5217\uff01\u60f3\u8d77\u4ece\u524d\u53ea\u80fd\u770b\u5c0f\u8bf4\uff0c\u77e5\u8db3\u5e38\u4e50\uff01\uff01\uff01"
#nick
u"\u82b1\u75f4\u6ce1\u9762\u7537\u2593\u304b\u2592"


import urllib.request
import http.cookiejar
import re
# number of the video
vid="1773930974"#be careful with the number, one number wrong may lead to inability of getting the right data
#the ID of the starting comment
comid="6296256343205128198"
url="http://coral.qq.com/article/"+vid+"/comment?commentid="+comid+"&reqnum=20"
headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
         "Accept-Encoding":"gb2312,utf-8",
         "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
         "Connection":"keep-alive",
         "referer":"qq.com"}
cjar=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
headall=[]
for key, value in headers.items():
    item=(key,value)
    headall.append(item)
opener.addheaders=headall
urllib.request.install_opener(opener)
# define craw in order to capture the comment webpage and return it
def craw(vid,comid):
    url="http://coral.qq.com/article/"+vid+"/comment?commentid="+comid+"&reqnum=20"
    data=urllib.request.urlopen(url).read().decode("utf-8")
    return data
idpat='"id":"(.*?)"'
userpat='"nick":"(.*?)",'
conpat='"content":"(.*?)",'
#first layer of loop, representing how many pages been captured
for i in range(1,2):
    print("-----------------")
    print("page "+str(i))
    data=craw(vid,comid)
    #second layer of loop, representing the result of each comment
    for j in range(0,20):
        idlist=re.compile(idpat,re.S).findall(data)
        contlist=re.compile(conpat,re.S).findall(data)
        userlist=re.compile(userpat,re.S).findall(data)
        print("Username: "+eval('u"'+userlist[j]+'"'))
        print("The content: "+eval('u"'+contlist[j]+'"'))
        print("\n")
    #change comid to the last id, so that the loop can go further down
    comid=idlist[19]

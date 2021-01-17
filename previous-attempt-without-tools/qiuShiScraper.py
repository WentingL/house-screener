# train of thoughts
# patterns between pages
# build page variables
# use for loop go through all the pages


import urllib.request
import re #regular expression

def getcontent(url,page):
    headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    #instill opener
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read().decode("utf-8")
    #build regular expression corresponding to the object
    userpat='<h2>(.*?)</h2>'
    #build regular expression corresponding to the content
    contentpat='<div class="content">(.*?)</div>'
    #compile - edit the key into regularexpression form
    #findall - find all the information by the regular expression
    #re.S - avoid influence of multiple lines
    #find all the object
    userlist=re.compile(userpat,re.S).findall(data)
    #find all the content
    contentlist=re.compile(contentpat,re.S).findall(data)
    x=1
    #for loop goes through all the content
    for content in contentlist:
        content=content.replace("/n","")
        #use the string as the var name and asign the string to a var
        name="content"+str(x)
        #assign the string to the var name by exec() function
        exec(name+'=content')
        x+=1
    y=1
    #for loop goes through all the object and output the corresponding content
    for user in userlist:
        name="content"+str(y)
        print("用户"+str(page)+str(y)+"是："+user)
        print("内容是：")
        exec("print("+name+")")
        print("/n")
        y+=1
#obtain multiple pages
for i in range(1,30):
    url="http://www.qiushibaike.com/8hr/page/"+str(i)
    getcontent(url,i)
    

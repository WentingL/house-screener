import urllib.request

file=urllib.request.urlopen("http://www.wiki.com")
data=file.read()
data=data.decode("utf-8","ignore")

#a test showing that some webs have protestions
#url="http://www.qiushibaike.com"
#file=urllib.request.urlopen(url)
#the webcrawler is rejected for not being a browser

#fool the security
url="http://www.quishibaike.com"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
#(key, value) #prentend to be a browser
opener=urllib.request.build_opener() #build the opener object
opener.addheaders=[headers] #add the headers into opener
data=opener.open(url).read().decode("utf-8") #read the website now
#print(data)
urllib.request.install_opener(opener) #make the opener valid in urllib too
data=urllib.request.urlopen(url).read().decode('utf-8')


#get request
url="http://www.baidu.com/s?wd="
key="网络爬虫"
key_code=urllib.request.quote(key)#code the characters in key
url_all=url+key_code #complete website link
req=urllib.request.Request(url_all) #request the website
data=urllib.request.urlopen(req).read()
fh=open("D:/UBC/test.html","wb")
fh.write(data)
fh.close()

#post
#post test address http://www.iqianyue.com/mypost/
import urllib.parse
url="http://www.iqianyue.com/mypost/"
postdata=urllib.parse.urlencode({"name":"ceo@iqianyue.com","pass":"aA123456"}).encode('utf-8')
req=urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
data=urllib.request.urlopen(req).read()
fhandle=open("D:/UBC/test2.html","wb")
fhandle.write(data)
fhandle.close()


url="https://ssc.adm.ubc.ca/sscportal/servlets/SRVSSCFramework?function=SessGradeRpt"
postdata=urllib.parse.urlencode({"username":"luowenti","password":"L&k15377932993"}).encode('utf-8')
req=urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
data=urllib.request.urlopen(req).read()
fhandle=open("D:/UBC/sscgrade.html","wb")
fhandle.write(data)
fhandle.close()

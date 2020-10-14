import urllib.request

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

print(data)

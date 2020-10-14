#import libraries for requesting the website, regular expression
import urllib.request
import re

# assign the url to url variable
url = "http://www.ratemyprofessors.com/ShowRatings.jsp?tid=1322913"

#pretend to be a browser
#assigning the infor of a browser to a header variable
header = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
#creat opener and assign header to the opener
opener = urllib.request.build_opener()
opener.addheaders = [header]
#instilling opener to urllib.request library
urllib.request.install_opener(opener)

#request data from the website
data = urllib.request.urlopen(url).read().decode("utf_8")

#build regular expression corresponding to the comment and date
contentpat = '<p class="commentsParagraph">(.*?)</p>'
datepat = '<div class="date">(.*?)</div>'

#find all content and date
contentlist = re.compile(contentpat,re.S).findall(data)
datelist = re.compile(datepat,re.S).findall(data)
datelist.pop() # the last item is irrelevant

#Use for loop to decode each comment and store them in list contentvessel
contentvessel = []
t = 0
for content in contentlist:
    content = content.replace("\r\n","")
    contentvessel.append(content)
    #print (contentvessel[t])
    #t+=1

#Use for loop to decode and print each date and print them with comment
x = 0
for date in datelist:
    print(date)
    print(contentvessel[x] + "\n")
    x+=1
    

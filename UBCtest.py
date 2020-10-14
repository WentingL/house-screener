import urllib.request as ur
import re

flag = 0
data1 = 0
data2 = 0
print("What is the subject?")
scode = input();
print("Which "+scode+" course?")
ccode = input()
print("Which section?")
cnum = input() + '$'

url1 = "https://courses.students.ubc.ca/cs/courseschedule?tname=subj-course&course="
url2 = "&campuscd=UBCO&dept="
url3 = "&pname=subjarea"
url = url1 + ccode + url2 + scode + url3
page = ur.urlopen(url)
data = str(page.read())

datapat = '<tr class=section[1,2]><td>(.*?)</a'
data1 = re.findall(datapat, data, flags=0)

statuspat= '^Full(.*?)' + cnum
for item in data1:
    data2 = re.search(statuspat, item)
    if data2:
        flag = 1

if flag:
    print("Yes, the section is full")
else:
    print("No, the section is not full")

"""
This is what we read from the website:

<tr class=section1>
<td>Full</td><td>
<a href=/cs/courseschedule?pname=subjarea&amp;tname=subj-section&amp;dept=COSC&amp;course=301&amp;section=L2D onmouseover="cancelHide=1; popup(); setColor(new Array(\'t2-11-4\',\'t2-12-4\',\'t2-13-4\',\'t2-14-4\'),\'7419\');" onmouseout="cancelHide=0;setTimeout(\'hideLayer()\',2000)">
COSC 301 L2D</a></td>
<td>Laboratory</td>
<td>2</td>

keywords:
class=section1
COSC 301 L2D
<td>Full</td>
"""
"""
f = data
file = open("E:/web crawler/Test/Output/COSC301.html","w")
file.truncate(0)
file.write(str(f))
file.close()
"""

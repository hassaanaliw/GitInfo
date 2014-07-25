from BeautifulSoup import  BeautifulSoup
import urllib
import re

r = urllib.urlopen("https://github.com/rg3/youtube-dl/issues").read()
author = 'rg3'
repo = 'youtube-dl'
soup = BeautifulSoup(r)

h = (str(soup.findAll("span",{'class':'list-group-item-number'})[0]))

valid = r'<span(.*?)>(.*)</span>'
num = (re.match(valid,h).group(2)).replace('#',"")

fin = urllib.urlopen("https://github.com/%s/%s/issues/%s" %(author,repo,num)).read()
title = BeautifulSoup(fin)
for d in title.findAll("title"):
    print(d.contents[0])

name = str(title.find("a",{'class':'author'}))
reg = r'<a.*?>(.*)</a>'
print(re.match(reg,name).group(1))
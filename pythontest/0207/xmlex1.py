'''
Created on 2020. 2. 7.

@author: GDJ-19
'''
from bs4 import BeautifulSoup
import urllib.request as req
import os.path
url=\
"http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

if not os.path.exists("forcast.xml") :
  #url의 내용을 forcast.xml 파일로 저장.  
    req.urlretrieve(url, "forcast.xml")
#forecast.xml 파일을 읽어 xml 값에 저장하기
xml = open("forecast.xml","r",encoding="utf-8").read()


# 현재 날씨구분으로 도시들을 저장 (dictionary객체)

info = {} #dictionary 사용
soup = BeautifulSoup(xml, "html.parser")
for location in soup.find_all("location") :
    name = location.find("city").string
    weather = location.find("wf").string
    if not (weather in info) :
        info[weather] = []
    info[weather].append(name)

for weather in info.keys() :
    print("+",weather)
    for name in info[weather] :
        print("/-",name)
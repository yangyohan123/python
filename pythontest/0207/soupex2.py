'''
Created on 2020. 2. 7.

@author: GDJ-19
'''
from bs4 import BeautifulSoup # html 분석 모듈
import urllib.request as req # url 사용 모듈

url = \
"http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
#res : url 전달된 데이터. soup의 분석 대상 데이터
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser") # BeautifulSoup

title = soup.find("title").string # title 태그의 내용(아이디값이 아님, 클래스가 아님.)
wf = soup.find("wf").string
print(title)
print(wf)

#html

#![CDATA] => 태그를 나탄는것이 아닌 문자열을 나타냄 
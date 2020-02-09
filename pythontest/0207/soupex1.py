'''
Created on 2020. 2. 7.

@author: GDJ-19
'''

from bs4 import BeautifulSoup # pip install beautifulsoup4

html = '''
        <html><body>
        <div id="potal">
            <h1>포털 목록 </h1>
            <ul class="items">
                <li><a href="http://www.naver.com">naver</a></li>
                <li><a href="http://www.daum.net">daum</a></li>
            </ul>
        </div>
        </body></html>
'''

soup = BeautifulSoup(html, "html.parser")
print(type(soup))
links = soup.find_all("a")# a 태그 전부
for a in links :
    href = a.attrs["href"]
    text = a.string
    print(text, ">" , href)
h1 = soup.select_one("div#potal > h1").string 
print("h1=", h1)

li_list = soup.select("div#potal > ul.items > li")
for li in li_list :
    print("li=", li.string)
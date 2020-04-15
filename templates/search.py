import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


plusUrl = urllib.parse.quote_plus(input('검색어를 입력하세요'))

url = f'https://search.kyobobook.co.kr/web/search?vPstrKeyWord={plusUrl}&orderClick=LET'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

books = soup.find_all(class_='detail')
# title = books.select_one('div.title > a > strong')
for book in books:
    img = soup.select_one('#search_list > tr > td.image > div.cover > a > img')
    title = book.select('div.title > a')
    author = book.select('div.author > a')
    print(img)    # for a in img:
    #     print(a)
    # for i in title:
    #     print(i.text.strip())
    # for n in author:
    #     print(n.text.strip())
    #
    print()



#search_list > tr:nth-child(6) > td.image > div.cover > a > img
#search_list > tr:nth-child(6) > td.detail > div.title > a > span.category2
#search_list > tr:nth-child(6) > td.detail > div.title > a > strong

#search_list > tr:nth-child(6) > td.detail > div.author
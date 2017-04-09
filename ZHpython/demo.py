'''
http://baike.baidu.com/link?url=XTFh9zlUd0wThQEkdrWlWulSl76qqnH8CFB8aAtsCjZe87OpIkcTsnQGvYIngOcgOyzTxy1m-di-bzda1W0K6q

'''

from bs4 import BeautifulSoup


count = '<div class="ddd"><div class="bb"></div></div>'
soup = BeautifulSoup(count,"html.parser",from_encoding='utf-8')

links = soup.find_all('div',class_='aaa')

print(links)
for link in links:
    print(link)
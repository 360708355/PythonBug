import http.cookiejar as cookielib
import urllib.request as urllib2
from bs4 import BeautifulSoup
from email.charset import Charset

#鐩存帴璇锋眰
# response = urllib2.urlopen('http://www.baidu.com')
#鑾峰彇鐘舵�佸悧
# print(response.getcode())

#璇诲彇鍐呭
# count = response.read()

#绗笁绉嶆柟娉� 娣诲姞cookie鐨勫鐞�
#import http.cookiejar as cookielib
#import urllib.request as urllib2

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')
#输出响应状态码
print(response.getcode())
count = response.read()
#输出网页的长度
print(len(count))
#输出网页的cookie
print(cj)
'''
#解析网页
begin
'''
soup = BeautifulSoup(count,"html.parser",from_encoding='utf-8')

links = soup.find_all('a')

for link in links:
    print(link)

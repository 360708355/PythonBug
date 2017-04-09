from bs4 import BeautifulSoup
from urllib import parse
import re

class HtmlParser(object):
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,"html.parser",from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        #print(new_urls,new_data)
        return new_urls,new_data
        
    @staticmethod
    def _get_new_urls(page_url,soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/(.*)"))
        #links = soup.find_all('a',href=re.compile(r"/item/*"))
        #links = soup.find_all('a')
        print(links)
        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
            #print(new_full_url)
        #print(new_urls)
        return new_urls

    @staticmethod
    def _get_new_data(page_url,soup):
        res_data = {}

        res_data['url'] = page_url
        #print(res_data['url'])
#         soup = soup.find('body')
        #print(soup)
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
#         for div in title_node:
#             print(div.attr('class'))
        #print(title_node)
#         title_node = title_node.find("h1")
        print(title_node)
        res_data['title'] = title_node.get_text()
        print(res_data['title'])
        
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        print(res_data['title'],res_data['url'],res_data['summary'])
        return res_data

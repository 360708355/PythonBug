
import http.cookiejar as cookielib
import urllib.request as urllib2

class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
        response = urllib2.urlopen(url)
        #response.decode('utf-8')
#         print(response.getcode())
        if response.getcode() != 200:
            return None
        return response.read()
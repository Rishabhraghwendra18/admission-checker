import back
from bs4 import BeautifulSoup
import urllib.error,urllib.request,urllib.parse

class scraping:
    def __init__(self):
        self.sql_data=back.check_sql()
    def scrap(self):
        for s_data in self.sql_data:
            if s_data[0]=='JAC-Delhi'or s_data[0]=='JOSSA':
                self.same_sites(s_data)
    def same_sites(self,data):
        site=urllib.request.urlopen(data[1])
        soup=BeautifulSoup(site,'html.parser')
        anchors=soup('a',href='#')
        for anchor in anchors:
            back.matching(data[0],anchor.text)
            # print('bat text: '+anchor.text.strip())

s=scraping()
s.scrap()

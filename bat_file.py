import back
from bs4 import BeautifulSoup
import urllib.error,urllib.request,urllib.parse
import concurrent.futures
from win10toast import ToastNotifier
import sys
import time
flag_stop=0
class scraping:
    def __init__(self):
        self.sql_data=back.check_sql()
        flag_stop=0
        while True:
            try:
                urllib.request.urlopen('https://www.google.co.in')
                self.scrap()
            except:
                if flag_stop==0:
                    notifier=ToastNotifier()
                    notifier.show_toast(title="No internet",msg="Admission checker can't fetch data from server. Make sure you are connected to internet",duration=8)
                    flag_stop+=1
                time.sleep(360)
                continue
            
    def scrap(self):
        for s_data in self.sql_data:
            try:
                if s_data[0]=='JAC-Delhi'or s_data[0]=='JOSSA':
                    self.same_sites(s_data)
                else:
                    self.diff_sites(s_data)
            except Exception:
                if flag_stop==0:
                    notifier=ToastNotifier()
                    notifier.show_toast(title=s_data[0]+' server error',msg=s_data[0]+ 'server is not responding',duration=8)
                    flag_stop+=1

    def same_sites(self,data):
        site=urllib.request.urlopen(data[1])
        soup=BeautifulSoup(site,'html.parser')
        anchors=soup('a',href='#')
        for anchor in anchors:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(back.matching,data[0],anchor.text)
            # print('bat text: '+anchor.text.strip())
    def diff_sites(self,data):
        site=urllib.request.urlopen(data[1])
        soup=BeautifulSoup(site,'html.parser')
        anchors=soup('a',class_='btn btn-primary btn-block btn-lg')
        # anchors=font_tag[0].find_all('a')
        for anchor in anchors:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.submit(back.matching,data[0],anchor.text)
            

time.sleep(180)
s=scraping()



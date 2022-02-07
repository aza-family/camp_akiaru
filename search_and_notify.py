# -*- coding: utf_8 -*-

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

import requests
from bs4 import BeautifulSoup
from slack import Slack

class SearchAndNotify:

    def __init__(self, url, month=None):
        #print("month:",month)
        # curl -X POST -d 'f_nengetsu=2022年3月' https://fumotoppara.secure.force.com/RS_Top
        #response = requests.post('http://www.example.com', data={'foo': 'bar'})
        #res = requests.get(url)
        res = requests.post(url, data={'f_nengetsu': month})

        self.soup = BeautifulSoup(res.text, 'html.parser', from_encoding='utf-8')

    def run(self):
        camp_maru = None
        camp_sankaku = None
        camp_x = None
        sankaku_text='△'
        maru_text='○'
        day_of_week = '土'
        camp_site = 'キャンプサイト'
        month = self.soup.find('option', selected=True).string

        #print(month.string)
        for el in self.soup.find_all('span', text=day_of_week):
            
            #print(el.parent.parent)
            camp = el.parent.parent.select_one('td:nth-of-type(3)')
            #print(camp)
            camp_maru = camp.find(text=maru_text)
            #print(camp_maru)
            camp_sankaku = camp.find(text=sankaku_text)
            if camp_maru is not None:
                day = camp_maru.parent.parent.parent.parent.select_one('td:nth-of-type(1)').string.encode('utf-8').decode('ascii', 'ignore')
                #print(camp_maru.parent.parent.parent.parent.select_one('td:nth-of-type(1)'))
                Slack(camp_site,maru_text,month, day,day_of_week).post()
            if camp_sankaku is not None:
                day = camp_sankaku.parent.parent.parent.parent.select_one('td:nth-of-type(1)').string.encode('utf-8').decode('ascii', 'ignore')
                #print(camp_maru.parent.parent.parent.parent.select_one('td:nth-of-type(1)'))
                Slack(camp_site,sankaku_text,month, day,day_of_week).post()

            #if camp_sankaku is not None:
            #    print('camp_sankaku:',camp_sankaku)
                #Slack('キャンプサイト','△').post()
            #camp_x = camp.findNext('td', text=maru_text)
            #if camp_maru:
            #   #print('○:',camp_maru)
               #Slack('キャンプサイト','○').post()
            #if camp_sankaku:
            #   print('△:',camp_sankaku)
               #Slack('キャンプサイト','△').post()

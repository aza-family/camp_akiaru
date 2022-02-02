#coding: UTF-8

import requests
from bs4 import BeautifulSoup
from slack import Slack

url = 'https://fumotoppara.secure.force.com/RS_Top'

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser', from_encoding='utf-8')

maru = None
sankaku = None
sankaku_text='△'
maru_text='○'

for el in soup.find_all('span', text='土'):
    for el2 in el.parent.parent.find_all('td', text=maru_text):
       #print(el2.text)
       maru = el2.text
    for el2 in el.parent.parent.find_all('td', text=sankaku_text):
       #print(el2.text)
       sankaku = el2.text

if maru:
   print('○:',maru)
   Slack('○').post()

if sankaku:
   print('△:',sankaku)
   Slack('△').post()

# <td class="td_itemvalue tbl_top_td1"><span style="color: #0000FF">土</span></td>
#△
# <a href="./RS_reservation1?kind=dorm&amp;p1=2022&amp;p2=2&amp;p3=18" class="reserv_btn4 FewColor" target="_self"><span class="tbl_top_sts">△</span></a>
#○
#<a href="./RS_reservation1?kind=villa&amp;p1=2022&amp;p2=2&amp;p3=17" class="reserv_btn3 " target="_self"><span class="tbl_top_sts">○</span><div></div></a>

#coding: UTF-8

import requests
from bs4 import BeautifulSoup
from slack import Slack

# url = 'https://koto-kosodate-portal.jp/smf/mizube/general/refresh_cal.php?center_cd=20' #大島
url = 'https://koto-kosodate-portal.jp/smf/mizube/general/refresh_cal.php?center_cd=10' #東陽
# url = 'https://koto-kosodate-portal.jp/smf/mizube/general/refresh_cal.php?center_cd=40' #南砂
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

result = soup.find_all('a', attrs={ 'class': lambda val: val in ['bgO', 'bgR'] }) 

if result:
    print('result:',result)
    Slack.post()
else:
   print('result is empty:',result)
   #Slack.post()

# if result2:
#     print('result2:',result2)
#     Slack.post()
# else:
#    print('result2 is empty:',result2)
   #Slack.post()
# --- Slack Post ---


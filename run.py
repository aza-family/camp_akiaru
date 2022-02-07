# -*- coding: utf_8 -*-
#import os, sys
#sys.path.append(os.path.join(os.path.dirname(__file__), 'site-packages'))

#import requests
#from bs4 import BeautifulSoup
#from slack import Slack
from search_and_notify import SearchAndNotify

# キャンプサイト -> 2
# コテージ柏    -> 3
# 翠山荘       -> 4 	
# 毛無山荘     -> 5

url = 'https://fumotoppara.secure.force.com/RS_Top'
# curl -X POST -d 'f_nengetsu=2022年3月' https://fumotoppara.secure.force.com/RS_Top
SearchAndNotify(url).run()
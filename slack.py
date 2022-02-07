# -*- coding: utf_8 -*-
#import sys,io
#print(sys.getdefaultencoding())
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#import sys, codecs
#sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import slackweb
# import requests
import settings


SLACK_WEBHOOK = settings.SLACK_WEBHOOK
print(SLACK_WEBHOOK)
SLACK_CHANNEL='#camp_캠핑파파'
SLACK_USER='キャンプ空き警報発令！！'
# SLACK_TEXT="空きがでたっぽいよ！！急げ"

class Slack:

    def __init__(self, camp, status, month, day, day_of_week):
        #self.type = status
        self.txt = "{}に{}{}日({}曜日){}空きを見つけました!!".format(camp, month, day, day_of_week,status)
        self.url = "https://fumotoppara.secure.force.com/RS_Top"

        # self.url = ""
    def post(self):
        slack=slackweb.Slack(url=SLACK_WEBHOOK)
        attachments=[]
        attachment={
                    "color": "#36a64f",
                    "fields":[
                          {
                          "title": "リンク:",
                          "value": self.url,
                          }
                      ]
                    }
        attachments.append(attachment)
        slack.notify(text=self.txt, channel=SLACK_CHANNEL, username=SLACK_USER, attachments=attachments)
#coding: UTF-8

import slackweb
# import requests
import settings


SLACK_WEBHOOK = settings.SLACK_WEBHOOK
print(SLACK_WEBHOOK)
SLACK_CHANNEL='#camp_캠핑파파'
SLACK_USER='キャンプ空き警報発令！！'
# SLACK_TEXT="空きがでたっぽいよ！！急げ"

class Slack:

    def __init__(self, type):
        self.type = type
        self.txt = "土曜日に{}空きが見つけました!!".format(type)
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
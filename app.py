# coding=UTF-8
import re
import numpy as np
import pandas as pd
import jieba_hant as jieba
import sys
import json
import random


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
import datetime

import google

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Nth5PHJ+ps4EwPRh+JzwLFUiVzLtDh6EydoOV3TjvoKb70MuMKmOA61pfiO67Mn8cJk6aIKtVUTzGA6GAHeEeCy4fYzwBfGrAVkeXPbnJkPq6PNAhQXQ1WccISco1lbOZSSSF/vWuVeBs2UZhrbIfgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('0c080474e1078590f3325766d808989d')

from flask import render_template

@app.route("/")
def home():
    return render_template("home.html")

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text_chat=event.message.text
    print(text_chat)
    if event.message.type == 'text':
        Sorry=[[446, 2005],[446,2007],[446,2008],[789,10879],[789,10887]]
        if(text_chat=="教學"):
            texts="東華大學網頁右上角有個搜尋器，可以去那邊把你想問的問題丟入"
            message_text = TextSendMessage(text=texts)
            message_sticker = StickerSendMessage(package_id=11537,sticker_id=52002770)
            message=[message_text,message_sticker]
            line_bot_api.reply_message(event.reply_token, message)
        if(text_chat=="願意評分"):
            quickreply_message = TextSendMessage(
            text='請評分("請輸入1,2,3,4,5")',
            quick_reply=QuickReply(items=[
            QuickReplyButton(action=MessageAction(image_url='https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png'
            ,label="1", text="1")),
            QuickReplyButton(action=MessageAction(image_url='https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png'
            ,label="2", text="2")),
            QuickReplyButton(action=MessageAction(image_url='https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png'
            ,label="3", text="3")),
            QuickReplyButton(action=MessageAction(image_url='https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png'
            ,label="4", text="4")),
            QuickReplyButton(action=MessageAction(image_url='https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png'
            ,label="5", text="5"))
            ])
            )

            line_bot_api.reply_message(event.reply_token, quickreply_message)
        elif(text_chat=="1"or text_chat=="2"or text_chat=="3"or text_chat=="4"or text_chat=="5"):
            texts="謝謝你的回饋"
            message_text = TextSendMessage(text=texts)
            message_sticker = StickerSendMessage(package_id=11537,sticker_id=52002743)
            message=[message_text,message_sticker]
            id=event.source.user_id
            google.googlesheet_score(text_chat,id)
            line_bot_api.reply_message(event.reply_token, message)
        else:
            texts="此LineBot已暫時停止維護"
            message_text = TextSendMessage(text=texts)
            message_sticker = StickerSendMessage(package_id=11537,sticker_id=52002770)
            
            id=event.source.user_id
            google.googlesheet_text(text_chat,id)
            
            #df = pd.read_excel('all.xls') 取消all這個表格，計算後發現好像不需要
            #載入自建辭典
            jieba.load_userdict("dict.txt")
            #lists= ['  '.join(jieba.cut_for_search(s))for s in [text_chat]]
            lists= jieba.lcut_for_search(text_chat)
            print('search模式：')
            print(lists)
            #listss= ['  '.join(jieba.cut(s,cut_all=False))for s in [text_chat]]
            listss= jieba.lcut(text_chat,cut_all=False)
            print('精準模式：')
            print(listss)
            listsss= jieba.lcut(text_chat,cut_all=True)
            print('全模式: ')
            print(listsss)
            '''
            from sklearn.feature_extraction.text import CountVectorizer
            count_vec=CountVectorizer() #创建词袋数据结构
            cv_fit=count_vec.fit_transform(lists)
                   #词汇表
            print(cv_fit)
            names=count_vec.get_feature_names()
            print(names)
            sum=cv_fit.toarray().sum(axis=0)
            CountsList = zip(names,sum)
            df_que = pd.DataFrame(data=CountsList,columns=['Names','Sums'])
            print(df_que)
            df_que=df_que.sort_values(by='Sums')
            que_number=df_que.shape[0]
            
            '''
            for i in lists:
                if i == ' ':
                    lists.remove(' ')
            print (lists)
            for i in listss:
                if i == ' ':
                    listss.remove(' ')
            print (listss)
            que_number=len(lists)
            print(lists[0][0])
            print(lists[0])
            print(que_number)
            protability=0
            total_rule=12
            differ=0
            rule_site=' '
            first=' '
            second=' '
            third=' '
            #以下是規則相關名稱
            website=['https://liff.line.me/1655771132-YlmplRBQ','https://liff.line.me/1655771132-ebVX3qRP',
            'https://liff.line.me/1655771132-y5pGMRNa','https://liff.line.me/1655771132-QwxjLdlY',
            'https://liff.line.me/1655771132-RLpOZA8D','https://liff.line.me/1655771132-brrxZl3V',
            'https://liff.line.me/1655771132-0jlB6MpK','https://liff.line.me/1655771132-qjBG50W6',
            'https://liff.line.me/1655771132-y77Wk8jx','https://liff.line.me/1655771132-w0D4AK3N',
            'https://liff.line.me/1655771132-p9437JN6','https://liff.line.me/1655771132-K8j3WVNr']
            names=['提前畢業方法','五年一貫','校際選課','抵免學分','轉系','延誤繳交學雜費','停修','跨域自主學習認證實施辦法','畢業資格','輔系','選課','雙主修']
            #每一個規則會有一個答案
            answer=[[0 for _ in range(2)] for _ in range(total_rule)]
            #幫規則編號好0,1,2,3,4,5,6,7,8,9,10,11
            for i in range(0,total_rule):
                answer[i][0]=i
            #print(answer)
            #統整跟問題相關的詞在每一個規則分別出現幾次
            appear = [[0 for _ in range(total_rule)] for _ in range(que_number)]
            #統整跟問題相關的詞總共出現幾次
            all=[0 for _ in range(que_number)]
            #k是0-11個規則
            for i in range(0,total_rule):
                df_else=pd.read_excel(str(i)+'.xls')
                #j是0到總共分成幾個詞
                for j in range(0,que_number):
                    for k in range(0,df_else.shape[0]):
                        #如果規則第i個詞剛好等於分詞後的詞
                        if(df_else['Names'][k]==lists[j]):
                            appear[j][i]= df_else['Sums'][k]
                            all[j]=all[j]+appear[j][i]
                            break
            #k是0-11個規則
            for i in range(0,total_rule):
                protability=0
                #j是0到總共分成幾個詞
                #做NaiveBayes
                for j in range(0,que_number):
                    #一開始把可能是這個規則的機率都設成0.5
                    PA=0.5
                    PAc=0.5
                    PBA=float(appear[j][i])
                    print (PBA)
                    PBAC=float(all[j]-appear[j][i])
                    if((PBA*PA+PBAC*PAc)==0):
                        PAB=0.0
                    else:
                        PAB=PBA*PA/(PBA*PA+PBAC*PAc)
                        round(PAB,3)
                        protability=protability+PAB
                protability=protability/que_number
                answer[i][1]=round(protability,3)
                print (names[i]+':'+str(answer[i][1]))
                print(appear)
            for i in range(0,total_rule):
                for j in range(0,total_rule-1):
                    if(answer[j][1]<answer[j+1][1]):
                        temp=answer[j+1]
                        answer[j+1]=answer[j]
                        answer[j]=temp
            print(answer)
            print (lists)
            print(appear)
            print(all)
            first_index=answer[0][0]
            second_index=answer[1][0]
            third_index=answer[2][0]
            first=names[first_index]
            second=names[second_index]
            third=names[third_index]
            print(first+':'+str(answer[0][1]))
            print(second+':'+str(answer[1][1]))
            print(third+':'+str(answer[2][1]))
            flex_answer_error=FlexSendMessage(alt_text='回饋',contents={
                  "type": "bubble",
                  "size": "mega",
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "願意幫我們評分嗎？",
                            "align": "center"
                          },
                          {
                            "type": "button",
                            "action": {
                              "type": "message",
                              "text": "願意評分",
                              "label": "願意"
                            },
                            "height": "sm",
                            "style": "secondary"
                          }
                        ]
                      }
                    ]
                  }
                })
            ndhu_google='https://www.google.com/search?sitesearch=ndhu.edu.tw&as_q='
            for i in listss:
                ndhu_google=ndhu_google+i+'+'
            message_text1 = TextSendMessage(text="可以試試一下這個連結尋找你需要的答案: "+ndhu_google)
            if('時候'in text_chat):
                texts="有關於時效性的問題 目前都還沒列入知識庫的規劃"
            google.googlesheet(text_chat,first,answer[0][1],second,answer[1][1],third,answer[2][1],id)
            message_text = TextSendMessage(text=texts)
            sticker_n =random.randrange(0,5)
            message_sticker = StickerSendMessage(package_id=Sorry[sticker_n][0],sticker_id=Sorry[sticker_n][1])
            message=[message_text,message_sticker,flex_answer_error,message_text1]
            line_bot_api.reply_message(event.reply_token, message)
                        


@handler.add(MessageEvent, message=StickerMessage)
def handle_message(event):
    message_text = TextSendMessage(text="謝謝你的貼圖。")
    message_sticker = StickerSendMessage(package_id=11537,sticker_id=52002770)
    message=[message_text,message_sticker]
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

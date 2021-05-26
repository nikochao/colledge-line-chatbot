# coding=UTF-8

import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
import datetime


def googlesheets(text_chat,answer0,answer1,answer2,answer3,answer4,answer5,answer6,answer7,answer8,user_id):
    #GDriveJSON就輸入下載下來Json檔名稱
    #GSpreadSheet是google試算表名稱
    GDriveJSON = 'ndhulinebot.json'
    GSpreadSheet = 'ndhulinebotfeedback'
    while True:
        try:
            scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
            key = SAC.from_json_keyfile_name(GDriveJSON, scope)
            gc = gspread.authorize(key)
            worksheet = gc.open(GSpreadSheet).sheet1
        except Exception as ex:
            print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
            print('Google sheet login failed with error:', ex)
            sys.exit(1)
        if text_chat!="":
            time=f'{datetime.datetime.now().ctime()}'
            worksheet.append_row((time,text_chat,answer0,answer1,answer2,answer3,answer4,answer5,answer6,answer7,answer8,user_id))
            print('新增一列資料到試算表' ,GSpreadSheet)
            return 1;

def googlesheet(text_chat,answer0,answer1,answer2,answer3,answer4,answer5,user_id):
    #GDriveJSON就輸入下載下來Json檔名稱
    #GSpreadSheet是google試算表名稱
    GDriveJSON = 'ndhulinebot.json'
    GSpreadSheet = 'ndhulinebotfeedback'
    while True:
        try:
            scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
            key = SAC.from_json_keyfile_name(GDriveJSON, scope)
            gc = gspread.authorize(key)
            worksheet = gc.open(GSpreadSheet).sheet1
        except Exception as ex:
            print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
            print('Google sheet login failed with error:', ex)
            sys.exit(1)
        if text_chat!="":
            time=f'{datetime.datetime.now().ctime()}'
            worksheet.append_row((time,text_chat,answer0,answer1,answer2,answer3,answer4,answer5,user_id))
            print('新增一列資料到試算表' ,GSpreadSheet)
            return 1;

def googlesheet_score(text_chat,user_id):
    #GDriveJSON就輸入下載下來Json檔名稱
    #GSpreadSheet是google試算表名稱
    GDriveJSON = 'ndhulinebot.json'
    GSpreadSheet = 'ndhulinebotfeedback'
    while True:
        try:
            scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
            key = SAC.from_json_keyfile_name(GDriveJSON, scope)
            gc = gspread.authorize(key)
            worksheet = gc.open(GSpreadSheet).worksheet('feedback')
        except Exception as ex:
            print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
            print('Google sheet login failed with error:', ex)
            sys.exit(1)
        if text_chat!="":
            time=f'{datetime.datetime.now().ctime()}'
            worksheet.append_row((time,text_chat,user_id))
            print('新增feedback到試算表' ,GSpreadSheet)
            return 1;
def googlesheet_text(text_chat,user_id):
    #GDriveJSON就輸入下載下來Json檔名稱
    #GSpreadSheet是google試算表名稱
    GDriveJSON = 'ndhulinebot.json'
    GSpreadSheet = 'ndhulinebotfeedback'
    while True:
        try:
            scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
            key = SAC.from_json_keyfile_name(GDriveJSON, scope)
            gc = gspread.authorize(key)
            worksheet = gc.open(GSpreadSheet).worksheet('all_message')
        except Exception as ex:
            print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
            print('Google sheet login failed with error:', ex)
            sys.exit(1)
        if text_chat!="":
            time=f'{datetime.datetime.now().ctime()}'
            worksheet.append_row((time,text_chat,user_id))
            print('新增一列資料到試算表' ,GSpreadSheet)
            return 1;


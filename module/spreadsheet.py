import discord
import datetime
import gspread
from google.oauth2.service_account import Credentials


client = discord.Client()

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credentials = Credentials.from_service_account_file(
    "C:/Users/deidra/Desktop/学習用プロジェクト/Key_Google/discord-bot-lyla-spreadsheet-8749c597f866.json",
    scopes=scopes
)
gc = gspread.authorize(credentials)
sh = gc.open("Lylaのスプレッドシート")



def monthcheck():
    worksheet_feed = sh.worksheets()              
    today = datetime.date.today().strftime('%Y%m')    
    exist = False
    for current in worksheet_feed:
        if current.title == today:
            exist = True                                
    if exist == False:                                 
         sh.add_worksheet(title=today, rows = 100, cols = 4)      
         newsheet = sh.worksheet(today) 
         newsheet.update('A1','収入')
         newsheet.update('C1','支出')   
    return sh.worksheet(today)

async def ledger(message):
    if message.content.endswith("スプシ"):
        monthcheck()
        today = datetime.date.today().strftime('%Y%m')
        print(sh.worksheet(today).get("A1"))

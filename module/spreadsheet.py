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



async def ledger(message):
    if message.content.endswith("スプシ"):
        print(sh.sheet1.get("A1"))

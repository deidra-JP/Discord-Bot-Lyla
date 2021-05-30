import discord
import requests
from bs4 import BeautifulSoup
import pickle
import datetime
import os

client = discord.Client()
news_path = "C:/Users/deidra/Desktop/学習用プロジェクト/Py_discord_bot_lyla/.info/.news_info/"
n_datetime_today = f'{datetime.date.today()}'
news_list = []



async def news_message(message):
# ニュース検索機能
    if message.content.endswith("経済ニュースお願い"):
        response = requests.get('https://news.yahoo.co.jp')
        html = BeautifulSoup(response.content, 'html.parser')
        for a in html.select('.topicsList .topicsListItem  a'): 
            a += (a['href'], list(a.strings)[0])
        n_text_path = os.path.join(news_path, "news_date" + n_datetime_today + "info.sav")        
        file = open(n_text_path, "wb")
        news_list.append(a)
        pickle.dump(news_list,file)
        file.close()
        print(news_list)


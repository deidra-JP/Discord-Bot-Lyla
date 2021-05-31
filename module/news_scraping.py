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


# Yahoo JAPAN newsからスクレイピング
async def economy_news_message(message):
# 経済ニュース検索機能
    if message.content.endswith("経済ニュースお願い"):
        response = requests.get("https://news.yahoo.co.jp/categories/business")
        html = BeautifulSoup(response.content, 'html.parser')
        topic = html.find(class_ = "sc-jgVwMx iXtPJx")
        for news_e_message in topic.find_all("a"): 
            n_e_m_text = news_e_message.text
            news_list.append(n_e_m_text)
            await message.channel.send(news_e_message.text) 
            e_n_url = news_e_message.get("href") 
            news_list.append(e_n_url)
            await message.channel.send(e_n_url)
        n_text_path = os.path.join(news_path, "news_date" + n_datetime_today + "info.sav")
        file = open(n_text_path, "wb")
        pickle.dump(news_list,file)
        file.close()
        print(news_list)

async def domestic_news_message(message):
# 国内ニュース検索機能
    if message.content.endswith("国内ニュースお願い"):
        response = requests.get("https://news.yahoo.co.jp/categories/domestic")
        html = BeautifulSoup(response.content, 'html.parser')
        topic = html.find(class_ = "sc-jgVwMx iXtPJx")
        for news_d_message in topic.find_all("a"): 
            n_d_m_text = news_d_message.text
            news_list.append(n_d_m_text)
            await message.channel.send(news_d_message.text) 
            d_n_url = news_d_message.get("href") 
            news_list.append(d_n_url)
            await message.channel.send(d_n_url)
        n_text_path = os.path.join(news_path, "news_date" + n_datetime_today + "info.sav")
        file = open(n_text_path, "wb")
        pickle.dump(news_list,file)
        file.close()
        print(news_list)

async def world_news_message(message):
# 国際ニュース検索機能
    if message.content.endswith("国際ニュースお願い"):
        response = requests.get("https://news.yahoo.co.jp/categories/world")
        html = BeautifulSoup(response.content, 'html.parser')
        topic = html.find(class_ = "sc-jgVwMx iXtPJx")
        for news_w_message in topic.find_all("a"): 
            n_w_m_text = news_w_message.text
            news_list.append(n_w_m_text)
            await message.channel.send(news_w_message.text) 
            w_n_url = news_w_message.get("href") 
            news_list.append(w_n_url)
            await message.channel.send(w_n_url)
        n_text_path = os.path.join(news_path, "news_date" + n_datetime_today + "info.sav")
        file = open(n_text_path, "wb")
        pickle.dump(news_list,file)
        file.close()
        print(news_list)        

async def entertainment_news_message(message):
# エンタメニュース検索機能
    if message.content.endswith("エンタメニュースお願い"):
        response = requests.get("https://news.yahoo.co.jp/categories/entertainment")
        html = BeautifulSoup(response.content, 'html.parser')
        topic = html.find(class_ = "sc-jgVwMx iXtPJx")
        for news_et_message in topic.find_all("a"): 
            n_et_m_text = news_et_message.text
            news_list.append(n_et_m_text)
            await message.channel.send(news_et_message.text) 
            et_n_url = news_et_message.get("href") 
            news_list.append(et_n_url)
            await message.channel.send(et_n_url)
        n_text_path = os.path.join(news_path, "news_date" + n_datetime_today + "info.sav")
        file = open(n_text_path, "wb")
        pickle.dump(news_list,file)
        file.close()
        print(news_list)        

async def sports_news_message(message):
# スポーツニュース検索機能
    if message.content.endswith("スポーツニュースお願い"):
        response = requests.get("https://news.yahoo.co.jp/categories/sports")
        html = BeautifulSoup(response.content, 'html.parser')
        topic = html.find(class_ = "sc-jgVwMx iXtPJx")
        for news_s_message in topic.find_all("a"): 
            n_s_m_text = news_s_message.text
            news_list.append(n_s_m_text)
            await message.channel.send(news_s_message.text) 
            s_n_url = news_s_message.get("href") 
            news_list.append(s_n_url)
            await message.channel.send(s_n_url)
        n_text_path = os.path.join(news_path, "news_date" + n_datetime_today + "info.sav")
        file = open(n_text_path, "wb")
        pickle.dump(news_list,file)
        file.close()
        print(news_list)              

async def it_news_message(message):
# ITニュース検索機能
    if message.content.endswith("ITニュースお願い"):
        response = requests.get("https://news.yahoo.co.jp/categories/it")
        html = BeautifulSoup(response.content, 'html.parser')
        topic = html.find(class_ = "sc-jgVwMx iXtPJx")
        for news_i_message in topic.find_all("a"): 
            n_i_m_text = news_i_message.text
            news_list.append(n_i_m_text)
            await message.channel.send(news_i_message.text) 
            i_n_url = news_i_message.get("href") 
            news_list.append(i_n_url)
            await message.channel.send(i_n_url)
        n_text_path = os.path.join(news_path, "news_date" + n_datetime_today + "info.sav")
        file = open(n_text_path, "wb")
        pickle.dump(news_list,file)
        file.close()
        print(news_list)                 

async def science_news_message(message):
# サイエンスニュース検索機能
    if message.content.endswith("サイエンスニュースお願い"):
        response = requests.get("https://news.yahoo.co.jp/categories/science")
        html = BeautifulSoup(response.content, 'html.parser')
        topic = html.find(class_ = "sc-jgVwMx iXtPJx")
        for news_ss_message in topic.find_all("a"): 
            n_ss_m_text = news_ss_message.text
            news_list.append(n_ss_m_text)
            await message.channel.send(news_ss_message.text) 
            ss_n_url = news_ss_message.get("href") 
            news_list.append(ss_n_url)
            await message.channel.send(ss_n_url)
        n_text_path = os.path.join(news_path, "news_date" + n_datetime_today + "info.sav")
        file = open(n_text_path, "wb")
        pickle.dump(news_list,file)
        file.close()
        print(news_list)                        

async def life_news_message(message):
# ライフニュース検索機能
    if message.content.endswith("ライフニュースお願い"):
        response = requests.get("https://news.yahoo.co.jp/categories/life")
        html = BeautifulSoup(response.content, 'html.parser')
        topic = html.find(class_ = "sc-jgVwMx iXtPJx")
        for news_l_message in topic.find_all("a"): 
            n_l_m_text = news_l_message.text
            news_list.append(n_l_m_text)
            await message.channel.send(news_l_message.text) 
            l_n_url = news_l_message.get("href") 
            news_list.append(l_n_url)
            await message.channel.send(l_n_url)
        n_text_path = os.path.join(news_path, "news_date" + n_datetime_today + "info.sav")
        file = open(n_text_path, "wb")
        pickle.dump(news_list,file)
        file.close()
        print(news_list)         

async def local_news_message(message):
# ローカルニュース検索機能
    if message.content.endswith("ローカルニュースお願い"):
        response = requests.get("https://news.yahoo.co.jp/categories/local")
        html = BeautifulSoup(response.content, 'html.parser')
        topic = html.find(class_ = "sc-jgVwMx iXtPJx")
        for news_lo_message in topic.find_all("a"): 
            n_lo_m_text = news_lo_message.text
            news_list.append(n_lo_m_text)
            await message.channel.send(news_lo_message.text) 
            lo_n_url = news_lo_message.get("href") 
            news_list.append(lo_n_url)
            await message.channel.send(lo_n_url)
        n_text_path = os.path.join(news_path, "news_date" + n_datetime_today + "info.sav")
        file = open(n_text_path, "wb")
        pickle.dump(news_list,file)
        file.close()
        print(news_list)                
# メッセージに反応する関数をまとめる
import sys
import discord
import toml
import random
import os
import pickle
import datetime
import hashlib
from module import picture_print
from module import long_text_print
from module import weather_forecast
from module import greeting_jp
from module import news_scraping
from module import spreadsheet
from module import game
from dna import ability
from googlesearch import search


CONFIG = toml.load(open("/Users/deidra/Desktop/学習用プロジェクト/Py_discord_bot_lyla/config.toml", encoding="utf-8_sig"))
TOKEN = CONFIG["config"]["token"]
CHANNELID = CONFIG["config"]["channel_id"]
client = discord.Client()
uranai = CONFIG["uranai_list"] 
path = "C:/Users/deidra/Desktop/学習用プロジェクト/Py_discord_bot_lyla/.info/.user_info/"
ModeFlag = 0
CreateFlag = 0
datetime_today = f'{datetime.date.today()}'
user_info_list = []




# 起動時に動作する処理
@client.event
async def on_ready():
    print('ログインしました')
    channel = client.get_channel(CHANNELID)
    await channel.send('んんっ～　起床！！')       

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    
    global ModeFlag
    global CreateFlag

    if message.author.bot:
        return

    # メッセージやメンションを貰うとそのユーザーのsavが日付ごとに作成・リストにその内容が追記される。
    if message.content.endswith("セーブファイルお願い"):
        random_mention = ["君の事憶えとくね！", "これから憶えとくね！", "記憶力〇", "記憶力◎", "記憶しとくよ～"]
        mention_hentou = random.choice(random_mention)
        reply = f'{message.author.mention}' + mention_hentou 
        await message.channel.send(reply)
        user_info_id = f'{message.author.id}'
        text_path = os.path.join(path, user_info_id + "date" + datetime_today + "info.sav")        
        file = open(text_path, "wb")
        pickle.dump(user_info_list,file)
        file.close()
    else:
        user_mention = f'{message.content}'
        user_info_id = f'{message.author.id}'
        text_path = path + user_info_id + "date" + datetime_today + "info.sav"
        file = open(text_path, "wb")
        user_info_list.append(user_info_id + user_mention)
        pickle.dump(user_info_list,file)
        file.close()
        # テスト時のみ
        print(user_info_list)

    # 占い
    if message.content.endswith("占いお願い"):
        uranai_message = random.choice(uranai)
        await message.channel.send("はーい！　今日の運勢は・・・・・・・" + "::" + uranai_message + "::")
    
    # サイコロ機能
    if message.content.endswith("６面サイコロお願い"):
        saikoro_random6 = random.randrange(1,6)
        saikoro6 = str(saikoro_random6)
        await message.channel.send("はいよ！" + saikoro6)
    
    # ランダム12桁整数
    if message.content.endswith("パスワードお願い"): 
        num_random12 = random.randrange(100000000000,999999999999)
        random12 = str(num_random12)
        await message.channel.send("はいよ！" + random12)
    
    # CryptoGame用sha256ハッシュ関数
    if message.content.endswith("BotWar"):
        str_CHANNELID = str(CHANNELID)
        Bot_War_ID = hashlib.sha256(TOKEN.encode('utf-8') + str_CHANNELID.encode('utf-8')).hexdigest()
        print(Bot_War_ID)
        
    # しょーもな返答リスト
    if message.content.endswith("俺以外ダメージでてなさすぎ"):
        await message.channel.send("それで負けてるんだから意味ねえんだよ　しょーもないハラスしてる暇あったらオブジェクト絡めボケ") 

    # チャンネルを作成する非同期関数を実行して発言したチャンネルのカテゴリ内にnewチャンネル作成
    if CreateFlag == 1:
        channel_name = message.content
        category_id = message.channel.category_id
        category = message.guild.get_channel(category_id)
        new_channel = await category.create_text_channel(name = channel_name)
        text = f'{new_channel.mention} を作成したよ！'
        CreateFlag = 0
        await message.channel.send(text)
    
    # チャンネルを作成する非同期関数の呼び出し
    if message.content.startswith("チャンネル作成お願い"):
        CreateFlag = 1
        await message.channel.send("名前どうするー？")

    # 検索機能
    if message.content == '検索終了':
        random_syuuryou = ["おつかれ！", "見つかったかな？", "見つかったカナ？", "どうだったかな？", "終了～！", "おわり！"]
        syuuryou_hentou = random.choice(random_syuuryou)
        await message.channel.send(syuuryou_hentou)
        ModeFlag = 0
    if ModeFlag == 1:
        kensaku = message.content
        count = 0
        # 日本語で検索した上位5件を順番に表示
        for url in search(kensaku, lang="jp",num = 5):
            await message.channel.send(url)
            text_path = path + user_info_id + "date" + datetime_today + "info.sav"
            url_str = str(url)
            user_info_list.append(kensaku + url_str)
            count += 1
            if(count == 5):
               break  
    
    # google検索モードへの切り替え
    if message.content.endswith("検索お願い"):
        ModeFlag = 1
        await message.channel.send("何について調べるー？")  
    
    # 指定した日時のリストを取り出す
    if message.content.startswith("date2"):
        save_yobidasi = message.content
        save_id = f'{message.author.id}'
        save_file = os.path.join(path, save_id + save_yobidasi)
        file = open(save_file, "rb")
        load = pickle.load(file)
        file.close()
        print(f'{load}')

    await picture_print.picture_message(message)
    
    await long_text_print.long_text_message(message)

    await weather_forecast.weather_message(message)

    await greeting_jp.greeting_jp_message(message)

    await news_scraping.economy_news_message(message)

    await news_scraping.domestic_news_message(message)

    await news_scraping.world_news_message(message)

    await news_scraping.entertainment_news_message(message)

    await news_scraping.sports_news_message(message)

    await news_scraping.it_news_message(message)

    await news_scraping.science_news_message(message)

    await news_scraping.life_news_message(message)

    await news_scraping.local_news_message(message)
    
    await spreadsheet.ledger(message)

    await spreadsheet.ledger(message)

    await game.HieroMagia_message(message)

    await game.Dicegame_message(message)

    await ability.choice_ability(message)

    #!SHUTDOWN_BOTが入力されたら強制終了
    if message.content.endswith("!SHUTDOWN_BOT_LYLA"):
        await message.channel.send("おやすみなさい( ˘ω˘ )")
        await client.logout()
        await sys.exit()              

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
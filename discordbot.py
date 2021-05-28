# メッセージに反応する関数をまとめる
import sys
import discord
import toml
import random
import os
import pickle
import datetime
import hashlib
import picture_print
import long_text_print
import urllib.request
import json
from googlesearch import search


CONFIG = toml.load(open('/Users/deidra/Desktop/学習用プロジェクト/Py_discord_bot_lyla/config.toml', encoding="utf-8_sig"))
TOKEN = CONFIG['config']['token']
CHANNELID = CONFIG['config']['channel_id']
client = discord.Client()
uranai = CONFIG['uranai_list'] 
path = "C:/Users/deidra/Desktop/学習用プロジェクト/Py_discord_bot_lyla/.user_info/"
ModeFlag = 0
datetime_today = f'{datetime.date.today()}'
user_info_list = []
citycode = '090010'
weather = urllib.request.urlopen('https://weather.tsukumijima.net/api/forecast/city/' + citycode).read()
weather = json.loads(weather.decode('utf-8'))

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
    if message.author.bot:
        return

    # メッセージやメンションを貰うとそのユーザーのsavが日付ごとに作成・リストにその内容が追記される。
    if message.content.endswith("セーブファイル作って"):
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
    
    #おはよう返答リスト１（おは）
    if message.content.endswith("おは"):
        await message.channel.send("おは！")  
    if message.content.endswith("おはー"):
        await message.channel.send("おはー！")         
    if message.content.endswith("おは～"):
        await message.channel.send("おは～！")   
    if message.content.endswith("おはぽよ"):
        await message.channel.send("おはぽよ！")     
    if message.content.endswith("おは！"):
        await message.channel.send("オハ！")  
    if message.content.endswith("おはー！"):
        await message.channel.send("おはおは！")         
    if message.content.endswith("おは～！"):
        await message.channel.send("おはおは～！")  
    if message.content.endswith("おっは"):
        await message.channel.send("おっは！")   
    if message.content.endswith("おっはー"):
        await message.channel.send("おっはー！")  
    if message.content.endswith("おはおは"):
        await message.channel.send("おはおは～！")
    if message.content.endswith("おはよ"):
        await message.channel.send("おはよ！") 
    if message.content.endswith("おはよー！"):
        await message.channel.send("おはよ～！")     
    if message.content.endswith("おはよーさん！"):
        await message.channel.send("おはよー")
    if message.content.endswith("おはよん"):
        await message.channel.send("おはよ！")
    if message.content.endswith("おはよ！"):
        await message.channel.send("おはよ～")
    if message.content.endswith("おはよう"):
        await message.channel.send("おはよ！")
    if message.content.endswith("おはようさん"):
        await message.channel.send("おはよ～！")
    if message.content.endswith("おはよ～"):
        await message.channel.send("おはよ！")
    if message.content.endswith("おはよー"):
        await message.channel.send("おはよー！")        
    if message.content.endswith("おはよ～！"):
        await message.channel.send("おはよう！")
    if message.content.endswith("おはよ～"):
        await message.channel.send("おはようさん！")
    if message.content.endswith("おはよ～！"):
        await message.channel.send("おはようー！")    
    if message.content.endswith("おはようございます"):
        await message.channel.send("おはようございます")
    if message.content.endswith("おはようございます！"):
        await message.channel.send("おはうございます！")

    #こん返答リスト１（こん）   
    if message.content.endswith("こん"):
        await message.channel.send("こん！")  
    if message.content.endswith("こんー"):
        await message.channel.send("こんー！")         
    if message.content.endswith("こん～"):
        await message.channel.send("こん～！")   
    if message.content.endswith("こんちゃ"):
        await message.channel.send("こんちゃ～よ～！")     
    if message.content.endswith("こん！"):
        await message.channel.send("こんこん！")  
    if message.content.endswith("こんー！"):
        await message.channel.send("こんちゃ！")         
    if message.content.endswith("こん～！"):
        await message.channel.send("こんこん～！") 
    if message.content.endswith("ばんちゃ"):
        await message.channel.send("ばんちゃ！")   
    if message.content.endswith("おばんです"):
        await message.channel.send("ばんわー！")  
    if message.content.endswith("ばんばん"):
        await message.channel.send("ばんばん！") 
    if message.content.endswith("こんにちは"):
        await message.channel.send("こんにちは！")  
    if message.content.endswith("こんにちはー"):
        await message.channel.send("こんにちはー！")         
    if message.content.endswith("こんにちは～"):
        await message.channel.send("こんにちは～！")   
    if message.content.endswith("ｺﾝﾁｬ"):
        await message.channel.send("ｺﾝﾁｬ！")     
    if message.content.endswith("ｺﾝ！"):
        await message.channel.send("ｺﾝｺﾝ！")    
    if message.content.endswith("コン"):
        await message.channel.send("コン！")  
    if message.content.endswith("こんにちわ"):
        await message.channel.send("こんにちわ！")         
    if message.content.endswith("こんにちわ！"):
        await message.channel.send("こんちゃちゃ！")   
    if message.content.endswith("こんちゃちゃ"):
        await message.channel.send("こんちゃ～よ～！！")     
    if message.content.endswith("ばんわ！"):
        await message.channel.send("ばんわ！")        
    if message.content.endswith("ばんわ～"):
        await message.channel.send("ばんわ～！")  
    if message.content.endswith("ばんわ"):
        await message.channel.send("ばんわ")         
    if message.content.endswith("こんばんわ"):
        await message.channel.send("こんばんわ！")   
    if message.content.endswith("こんばんは"):
        await message.channel.send("こんばんは！")     
    if message.content.endswith("こんばんわ！"):
        await message.channel.send("こんばんワ！")      
    if message.content.endswith("やほ"):
        await message.channel.send("やほ！")  
    if message.content.endswith("やほー"):
        await message.channel.send("やほー！")         
    if message.content.endswith("やほ～"):
        await message.channel.send("やほ～！")   
    if message.content.endswith("やほ！"):
        await message.channel.send("やほ")  
    if message.content.endswith("やほー！"):
        await message.channel.send("やほー")         
    if message.content.endswith("やほ～！"):
        await message.channel.send("やほ～")   
    if message.content.endswith("やほい"):
        await message.channel.send("やほい！")  
    if message.content.endswith("うぇ～い"):
        await message.channel.send("うぇ～い！")         
    if message.content.endswith("やっほー"):
        await message.channel.send("やっほー！")   
    if message.content.endswith("やっほー！"):
        await message.channel.send("やっほー")   
    if message.content.endswith("やっほ～"):
        await message.channel.send("やっほ～！")    
    if message.content.endswith("やっほ～！"):
        await message.channel.send("やっほ～")     
    
    # ポートフォリオに適さない為、64行分Githubから削除
         

    # 名前付きで返す 
    if message.content.endswith("ライラ"):
        random_namae_henji = ["君呼んだ？", "君呼んだー？", "君なんか用ー？", "君やほい", "君おつかり！", "君やっほ！", "君呼んだかな～？", "♡"]
        namae_henji = random.choice(random_namae_henji)
        username = message.author.name
        await message.channel.send(username + namae_henji )

    if message.content.endswith("Lyla"):
        random_namae_henji2 = ["君呼んだ？", "君呼んだー？", "君なんか用ー？", "君やほい", "君おつかり！", "君やっほ！", "君呼んだかな～？", "♡"]
        namae_henji2 = random.choice(random_namae_henji2)
        username = message.author.name
        await message.channel.send(username + namae_henji2 ) 

    if message.content.endswith("lyla"):
        random_namae_henji3 = ["君呼んだ？", "君呼んだー？", "君なんか用ー？", "君やほい", "君おつかり！", "君やっほ！", "君呼んだかな～？", "♡"]
        namae_henji3 = random.choice(random_namae_henji3)
        username = message.author.name
        await message.channel.send(username + namae_henji3 )  

    if message.content.endswith("ライラ好き"):
        random_namae_henji4 = ["ｸﾝありがと！", "君ありがと！♡", "君照れる", "君口が達者ね", "君好きよ！", "♡"]
        namae_henji4 = random.choice(random_namae_henji4)
        username = message.author.name
        await message.channel.send(username + namae_henji4 ) 

    if message.content.endswith("ライラちゃん好き"):
        random_namae_henji5 = ["ｸﾝありがと！", "君ありがと！♡", "君照れる", "君口が達者ね", "君好きよ！", "♡"]
        namae_henji5 = random.choice(random_namae_henji5)
        username = message.author.name
        await message.channel.send(username + namae_henji5 )                                        

    # 占い
    if message.content.endswith("占いお願い"):
        uranai_message = random.choice(uranai)
        await message.channel.send("はーい！　今日の運勢は・・・・・・・" + "::" + uranai_message + "::")

    # ランダム12桁整数
    if message.content.endswith("パスワード作って"): 
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

    # 天気予報機能
    if message.content.endswith("天気予報お願い"):
        weather_hentou = weather['location']['city']
        weather_hentou += "の天気は、\n"
        for w in weather['forecasts']:
            weather_hentou += w['dateLabel'] + "が" + w['telop'] + "\n"
        weather_hentou += "です。"
        await message.channel.send(weather_hentou)

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
            file = open(text_path, "wb")
            url_str = str(url)
            user_info_list.append(kensaku + url_str)
            pickle.dump(user_info_list,file)
            file.close()
            print(user_info_list)
            count += 1
            if(count == 5):
               break  
    
    # google検索モードへの切り替え
    if message.content.endswith("検索して"):
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
        print(f'{load[1]}')

    await picture_print.picture_message(message)
    
    await long_text_print.long_text_message(message)

    #!SHUTDOWN_BOTが入力されたら強制終了
    if message.content.endswith("!SHUTDOWN_BOT_LYLA"):
        await message.channel.send("おやすみなさい( ˘ω˘ )")
        await client.logout()
        await sys.exit()              

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
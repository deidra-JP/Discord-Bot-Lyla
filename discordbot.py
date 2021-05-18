# インストールした discord.py を読み込む
import sys
import discord
import toml
import asyncio
import random
import os
import pickle
import datetime
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
    

# 起動時に動作する処理
@client.event
async def on_ready():
    print('ログインしました')
    channel = client.get_channel(CHANNELID)
    await channel.send('んんっ～　起床！！')       

# メンション受け取り時の処理
@client.event
async def reply(message):
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
        list_user_info = user_info_list.append(user_mention)
        pickle.dump(list_user_info,file)
        file.close()
        print(user_info_list)
    
    #おはよう返答リスト１（おは）    
    if message.content == 'おは':
        await message.channel.send('おは！')  
    if message.content == 'おはー':
        await message.channel.send('おはー！')         
    if message.content == 'おは～':
        await message.channel.send('おは～！')   
    if message.content == 'おはぽよ':
        await message.channel.send('おはぽよ！')     
    if message.content == 'おは！':
        await message.channel.send('オハ！')  
    if message.content == 'おはー！':
        await message.channel.send('おはおは！')         
    if message.content == 'おは～！':
        await message.channel.send('おはおは～！')  
    if message.content == 'おっは':
        await message.channel.send('おっは！')   
    if message.content == 'おっはー':
        await message.channel.send('おっはー！')  
    if message.content == 'おはおは':
        await message.channel.send('おはおは～！')                      
    
    #おはよう返答ランダムリスト（おはよ）
    if message.content.startswith("おはよ"):
        random_ohayou = ["おはよう！", "オハヨ！", "おはようね～", "おはよん！", "おはー！", "おはおは！",
         "おはぽよやほい！", "おはよぉ～！", "おはようさん～！", "おはようさん！", "おはよーさん！",
          "おはよ～！", "おはよー！", "おはようさんね！", "おはよ！"]
        aisatu_asa = random.choice(random_ohayou)
        await message.channel.send(aisatu_asa)
    
    #こん返答リスト１（こん）    
    if message.content == 'こん':
        await message.channel.send('こん！')  
    if message.content == 'こんー':
        await message.channel.send('こんー！')         
    if message.content == 'こん～':
        await message.channel.send('こん～！')   
    if message.content == 'こんちゃ':
        await message.channel.send('こんちゃ～よ～！')     
    if message.content == 'こん！':
        await message.channel.send('こんこん！')  
    if message.content == 'こんー！':
        await message.channel.send('こんちゃ！')         
    if message.content == 'こん～！':
        await message.channel.send('こんこん～！')  
    if message.content == 'ばんちゃ':
        await message.channel.send('ばんちゃ！')   
    if message.content == 'おばんです':
        await message.channel.send('ばんわー！')  
    if message.content == 'ばんばん':
        await message.channel.send('ばんばん！') 
    if message.content == 'こんにちは':
        await message.channel.send('こんにちは！')  
    if message.content == 'こんにちはー':
        await message.channel.send('こんにちはー！')         
    if message.content == 'こんにちは～':
        await message.channel.send('こんにちは～！')   
    if message.content == 'ｺﾝﾁｬ':
        await message.channel.send('ｺﾝﾁｬ！')     
    if message.content == 'ｺﾝ！':
        await message.channel.send('ｺﾝｺﾝ！')    
    if message.content == 'コン':
        await message.channel.send('コン！')  
    if message.content == 'こんにちわ':
        await message.channel.send('こんにちわ！')         
    if message.content == 'こんにちわ！':
        await message.channel.send('こんちゃちゃ！')   
    if message.content == 'こんちゃちゃ':
        await message.channel.send('こんちゃ～よ～！！')     
    if message.content == 'ばんわ！':
        await message.channel.send('ばんわ！')        
    if message.content == 'ばんわ～':
        await message.channel.send('ばんわ～！')  
    if message.content == 'ばんわ':
        await message.channel.send('ばんわ')         
    if message.content == 'こんばんわ':
        await message.channel.send('こんばんわ！')   
    if message.content == 'こんばんは':
        await message.channel.send('こんばんは！')     
    if message.content == 'こんばんわ！':
        await message.channel.send('こんばんワ！')      
    if message.content == 'やほ':
        await message.channel.send('やほ！')  
    if message.content == 'やほー':
        await message.channel.send('やほー！')         
    if message.content == 'やほ～':
        await message.channel.send('やほ～！')   
    if message.content == 'やほ！':
        await message.channel.send('やほ')  
    if message.content == 'やほー！':
        await message.channel.send('やほー')         
    if message.content == 'やほ～！':
        await message.channel.send('やほ～')   
    if message.content == 'やほい':
        await message.channel.send('やほい！')  
    if message.content == 'うぇ～い':
        await message.channel.send('うぇ～い！')         
    if message.content == 'やっほー':
        await message.channel.send('やっほー！')   
    if message.content == 'やっほー！':
        await message.channel.send('やっほー')   
    if message.content == 'やっほ～':
        await message.channel.send('やっほ～！')    
    if message.content == 'やっほ～！':
        await message.channel.send('やっほ～')              

    #下ネタ返答リスト
    if message.content.startswith("ちんこ"):    
        random_simoneta_hentou = ["は？", "最低ね", "はぁ？", "低俗ね", "あ？？？？"]
        simoneta_hentou_tinnko = random.choice(random_simoneta_hentou)
        await message.channel.send(simoneta_hentou_tinnko)
    if message.content.startswith("まんこ"):    
        random_simoneta_hentou2 = ["は？最低", "最低ね・・・", "はぁ？ちょっと", "低俗ねあなた", "あぁ？？？？"]
        simoneta_hentou_manko = random.choice(random_simoneta_hentou2)
        await message.channel.send(simoneta_hentou_manko) 
    if message.content.startswith("おちんちん"):    
        random_simoneta_hentou3 = ["何言ってるの？", "あなた最低ね", "ねえはぁ？", "ほんと低俗ね", "あ？"]
        simoneta_hentou_otinntinn = random.choice(random_simoneta_hentou3)
        await message.channel.send(simoneta_hentou_otinntinn)  
    if message.content.startswith("ちんぽ"):    
        random_simoneta_hentou4 = ["は？きも", "きもい最低ね", "はぁ？ちょっとやめて", "最低で低俗ね", "あ？？"]
        simoneta_hentou_tinnpo = random.choice(random_simoneta_hentou4)
        await message.channel.send(simoneta_hentou_tinnpo)  
    if message.content.startswith("うんこ"):    
        random_simoneta_hentou5 = ["トイレ行ってきな", "小学生か", "きちゃない", "手洗った？", "トイレットペーパーあった？"]
        simoneta_hentou_unnko = random.choice(random_simoneta_hentou5)
        await message.channel.send(simoneta_hentou_unnko)          
    if message.content.startswith("うんち"):    
        random_simoneta_hentou6 = ["トイレ行ってきなて", "中学生か", "きちゃないよ", "手洗ったかい？", "トイレットペーパー足しといて"]
        simoneta_hentou_unnti = random.choice(random_simoneta_hentou6)
        await message.channel.send(simoneta_hentou_unnti) 
    if message.content.startswith("ﾁﾝﾎﾟ"):    
        random_simoneta_hentou7 = ["は？きも", "きもい最低ね", "はぁ？ちょっとやめて", "最低で低俗ね", "あ？？"]
        simoneta_hentou_tinnpox = random.choice(random_simoneta_hentou7)
        await message.channel.send(simoneta_hentou_tinnpox) 
    if message.content.startswith("ウンチ"):    
        random_simoneta_hentou8 = ["はやくトイレ行ってきなて", "男子中学生か", "きちゃないよぺっぺ", "手洗ったかな？", "トイレットペーパー足して"]
        simoneta_hentou_unntixx = random.choice(random_simoneta_hentou8)
        await message.channel.send(simoneta_hentou_unntixx)  
    if message.content.startswith("ウンコ"):    
        random_simoneta_hentou9 = ["トイレ行ってきなゴリラ", "ゴリラ", "ウホ", "？", "トイレットペーパー使える？"]
        simoneta_hentou_unnkoxx = random.choice(random_simoneta_hentou9)
        await message.channel.send(simoneta_hentou_unnkoxx)   
    if message.content.startswith("チンコ"):    
        random_simoneta_hentou10 = ["は・・・？", "最低ねほんと", "はぁ・・・？", "低俗ねほんと", "あ？？は？？"]
        simoneta_hentou_tinnkoxx = random.choice(random_simoneta_hentou10)
        await message.channel.send(simoneta_hentou_tinnkoxx)     
    if message.content.startswith("マンコ"):    
        random_simoneta_hentou11 = ["は？最低・・・", "最低ね・・・やめて", "はぁ？ちょっときもい", "最低最悪低俗ねあなた", "あぁ？？？？もっかいいってみ？"]
        simoneta_hentou_mankoxx = random.choice(random_simoneta_hentou11)
        await message.channel.send(simoneta_hentou_mankoxx)  
    if message.content.startswith("オチンチン"):    
        random_simoneta_hentou12 = ["何言ってるの？中年のキモオヤジ", "あなた最低ねはじを知りなさい", "ねえはぁ？やめて", "ほんっと低俗ね", "あ？ねえ"]
        simoneta_hentou_otinntinnxx = random.choice(random_simoneta_hentou12)
        await message.channel.send(simoneta_hentou_otinntinnxx)   
    if message.content.startswith("チンポ"):    
        random_simoneta_hentou13 = ["は？きもいんだけど", "きもい最低クズ", "はぁ？ちょっとやめてださないでよ", "最低で低俗ね、、鏡観たことある？", "あ？？は？？"]
        simoneta_hentou_tinnpoxx = random.choice(random_simoneta_hentou13)
        await message.channel.send(simoneta_hentou_tinnpoxx)                                

    # 名前付きで返す
    if message.content.startswith("ライラ"):
        random_namae_henji = ["君呼んだ？", "君呼んだー？", "君なんか用ー？", "君やほい", "君おつかり！", "君やっほ！", "君呼んだかな～？", "♡"]
        namae_henji = random.choice(random_namae_henji)
        username = message.author.name
        await message.channel.send(username + namae_henji )     

    if message.content.startswith("Lyla"):
        random_namae_henji2 = ["君呼んだ？", "君呼んだー？", "君なんか用ー？", "君やほい", "君おつかり！", "君やっほ！", "君呼んだかな～？", "♡"]
        namae_henji2 = random.choice(random_namae_henji2)
        username = message.author.name
        await message.channel.send(username + namae_henji2 ) 

    if message.content.startswith("lyla"):
        random_namae_henji3 = ["君呼んだ？", "君呼んだー？", "君なんか用ー？", "君やほい", "君おつかり！", "君やっほ！", "君呼んだかな～？", "♡"]
        namae_henji3 = random.choice(random_namae_henji3)
        username = message.author.name
        await message.channel.send(username + namae_henji3 )  

    if message.content.startswith("ライラ好き"):
        random_namae_henji4 = ["ｸﾝありがと！", "君ありがと！♡", "君照れる", "君口が達者ね", "君好きよ！", "♡"]
        namae_henji4 = random.choice(random_namae_henji4)
        username = message.author.name
        await message.channel.send(username + namae_henji4 ) 

    if message.content.startswith("ライラちゃん好き"):
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

    # しょーもな返答リスト
    if message.content.startswith("俺以外ダメージでてなさすぎ"):
        await message.channel.send('それで負けてるんだから意味ねえんだよ　しょーもないハラスしてる暇あったらオブジェクト絡めボケ') 
    
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
            count += 1
            if(count == 5):
               break  
    
    # google検索モードへの切り替え
    if message.content.endswith("検索して"):
        ModeFlag = 1
        await message.channel.send('何について調べるー？')  
    
    #!SHUTDOWN_BOTが入力されたら強制終了
    if message.content.startswith('!SHUTDOWN_BOT_LYLA'):
        await message.channel.send('おやすみなさい( ˘ω˘ )')
        await client.logout()
        await sys.exit() 

# 話しかけられたかの判定
@client.event
async def on_message(message):
    if client.user in message.mentions:
        await reply(message)  

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
        list_user_info = user_info_list.append(user_mention)
        pickle.dump(list_user_info,file)
        file.close()
        print(user_info_list)
    
    #おはよう返答リスト１（おは）    
    if message.content == 'おは':
        await message.channel.send('おは！')  
    if message.content == 'おはー':
        await message.channel.send('おはー！')         
    if message.content == 'おは～':
        await message.channel.send('おは～！')   
    if message.content == 'おはぽよ':
        await message.channel.send('おはぽよ！')     
    if message.content == 'おは！':
        await message.channel.send('オハ！')  
    if message.content == 'おはー！':
        await message.channel.send('おはおは！')         
    if message.content == 'おは～！':
        await message.channel.send('おはおは～！')  
    if message.content == 'おっは':
        await message.channel.send('おっは！')   
    if message.content == 'おっはー':
        await message.channel.send('おっはー！')  
    if message.content == 'おはおは':
        await message.channel.send('おはおは～！')                      
    
    #おはよう返答ランダムリスト（おはよ）
    if message.content.startswith("おはよ"):
        random_ohayou = ["おはよう！", "オハヨ！", "おはようね～", "おはよん！", "おはー！", "おはおは！",
         "おはぽよやほい！", "おはよぉ～！", "おはようさん～！", "おはようさん！", "おはよーさん！",
          "おはよ～！", "おはよー！", "おはようさんね！", "おはよ！"]
        aisatu_asa = random.choice(random_ohayou)
        await message.channel.send(aisatu_asa)
    
    #こん返答リスト１（こん）    
    if message.content == 'こん':
        await message.channel.send('こん！')  
    if message.content == 'こんー':
        await message.channel.send('こんー！')         
    if message.content == 'こん～':
        await message.channel.send('こん～！')   
    if message.content == 'こんちゃ':
        await message.channel.send('こんちゃ～よ～！')     
    if message.content == 'こん！':
        await message.channel.send('こんこん！')  
    if message.content == 'こんー！':
        await message.channel.send('こんちゃ！')         
    if message.content == 'こん～！':
        await message.channel.send('こんこん～！')  
    if message.content == 'ばんちゃ':
        await message.channel.send('ばんちゃ！')   
    if message.content == 'おばんです':
        await message.channel.send('ばんわー！')  
    if message.content == 'ばんばん':
        await message.channel.send('ばんばん！') 
    if message.content == 'こんにちは':
        await message.channel.send('こんにちは！')  
    if message.content == 'こんにちはー':
        await message.channel.send('こんにちはー！')         
    if message.content == 'こんにちは～':
        await message.channel.send('こんにちは～！')   
    if message.content == 'ｺﾝﾁｬ':
        await message.channel.send('ｺﾝﾁｬ！')     
    if message.content == 'ｺﾝ！':
        await message.channel.send('ｺﾝｺﾝ！')    
    if message.content == 'コン':
        await message.channel.send('コン！')  
    if message.content == 'こんにちわ':
        await message.channel.send('こんにちわ！')         
    if message.content == 'こんにちわ！':
        await message.channel.send('こんちゃちゃ！')   
    if message.content == 'こんちゃちゃ':
        await message.channel.send('こんちゃ～よ～！！')     
    if message.content == 'ばんわ！':
        await message.channel.send('ばんわ！')        
    if message.content == 'ばんわ～':
        await message.channel.send('ばんわ～！')  
    if message.content == 'ばんわ':
        await message.channel.send('ばんわ')         
    if message.content == 'こんばんわ':
        await message.channel.send('こんばんわ！')   
    if message.content == 'こんばんは':
        await message.channel.send('こんばんは！')     
    if message.content == 'こんばんわ！':
        await message.channel.send('こんばんワ！')      
    if message.content == 'やほ':
        await message.channel.send('やほ！')  
    if message.content == 'やほー':
        await message.channel.send('やほー！')         
    if message.content == 'やほ～':
        await message.channel.send('やほ～！')   
    if message.content == 'やほ！':
        await message.channel.send('やほ')  
    if message.content == 'やほー！':
        await message.channel.send('やほー')         
    if message.content == 'やほ～！':
        await message.channel.send('やほ～')   
    if message.content == 'やほい':
        await message.channel.send('やほい！')  
    if message.content == 'うぇ～い':
        await message.channel.send('うぇ～い！')         
    if message.content == 'やっほー':
        await message.channel.send('やっほー！')   
    if message.content == 'やっほー！':
        await message.channel.send('やっほー')   
    if message.content == 'やっほ～':
        await message.channel.send('やっほ～！')    
    if message.content == 'やっほ～！':
        await message.channel.send('やっほ～')              

    #下ネタ返答リスト
    if message.content.startswith("ちんこ"):    
        random_simoneta_hentou = ["は？", "最低ね", "はぁ？", "低俗ね", "あ？？？？"]
        simoneta_hentou_tinnko = random.choice(random_simoneta_hentou)
        await message.channel.send(simoneta_hentou_tinnko)
    if message.content.startswith("まんこ"):    
        random_simoneta_hentou2 = ["は？最低", "最低ね・・・", "はぁ？ちょっと", "低俗ねあなた", "あぁ？？？？"]
        simoneta_hentou_manko = random.choice(random_simoneta_hentou2)
        await message.channel.send(simoneta_hentou_manko) 
    if message.content.startswith("おちんちん"):    
        random_simoneta_hentou3 = ["何言ってるの？", "あなた最低ね", "ねえはぁ？", "ほんと低俗ね", "あ？"]
        simoneta_hentou_otinntinn = random.choice(random_simoneta_hentou3)
        await message.channel.send(simoneta_hentou_otinntinn)  
    if message.content.startswith("ちんぽ"):    
        random_simoneta_hentou4 = ["は？きも", "きもい最低ね", "はぁ？ちょっとやめて", "最低で低俗ね", "あ？？"]
        simoneta_hentou_tinnpo = random.choice(random_simoneta_hentou4)
        await message.channel.send(simoneta_hentou_tinnpo)  
    if message.content.startswith("うんこ"):    
        random_simoneta_hentou5 = ["トイレ行ってきな", "小学生か", "きちゃない", "手洗った？", "トイレットペーパーあった？"]
        simoneta_hentou_unnko = random.choice(random_simoneta_hentou5)
        await message.channel.send(simoneta_hentou_unnko)          
    if message.content.startswith("うんち"):    
        random_simoneta_hentou6 = ["トイレ行ってきなて", "中学生か", "きちゃないよ", "手洗ったかい？", "トイレットペーパー足しといて"]
        simoneta_hentou_unnti = random.choice(random_simoneta_hentou6)
        await message.channel.send(simoneta_hentou_unnti) 
    if message.content.startswith("ﾁﾝﾎﾟ"):    
        random_simoneta_hentou7 = ["は？きも", "きもい最低ね", "はぁ？ちょっとやめて", "最低で低俗ね", "あ？？"]
        simoneta_hentou_tinnpox = random.choice(random_simoneta_hentou7)
        await message.channel.send(simoneta_hentou_tinnpox) 
    if message.content.startswith("ウンチ"):    
        random_simoneta_hentou8 = ["はやくトイレ行ってきなて", "男子中学生か", "きちゃないよぺっぺ", "手洗ったかな？", "トイレットペーパー足して"]
        simoneta_hentou_unntixx = random.choice(random_simoneta_hentou8)
        await message.channel.send(simoneta_hentou_unntixx)  
    if message.content.startswith("ウンコ"):    
        random_simoneta_hentou9 = ["トイレ行ってきなゴリラ", "ゴリラ", "ウホ", "？", "トイレットペーパー使える？"]
        simoneta_hentou_unnkoxx = random.choice(random_simoneta_hentou9)
        await message.channel.send(simoneta_hentou_unnkoxx)   
    if message.content.startswith("チンコ"):    
        random_simoneta_hentou10 = ["は・・・？", "最低ねほんと", "はぁ・・・？", "低俗ねほんと", "あ？？は？？"]
        simoneta_hentou_tinnkoxx = random.choice(random_simoneta_hentou10)
        await message.channel.send(simoneta_hentou_tinnkoxx)     
    if message.content.startswith("マンコ"):    
        random_simoneta_hentou11 = ["は？最低・・・", "最低ね・・・やめて", "はぁ？ちょっときもい", "最低最悪低俗ねあなた", "あぁ？？？？もっかいいってみ？"]
        simoneta_hentou_mankoxx = random.choice(random_simoneta_hentou11)
        await message.channel.send(simoneta_hentou_mankoxx)  
    if message.content.startswith("オチンチン"):    
        random_simoneta_hentou12 = ["何言ってるの？中年のキモオヤジ", "あなた最低ねはじを知りなさい", "ねえはぁ？やめて", "ほんっと低俗ね", "あ？ねえ"]
        simoneta_hentou_otinntinnxx = random.choice(random_simoneta_hentou12)
        await message.channel.send(simoneta_hentou_otinntinnxx)   
    if message.content.startswith("チンポ"):    
        random_simoneta_hentou13 = ["は？きもいんだけど", "きもい最低クズ", "はぁ？ちょっとやめてださないでよ", "最低で低俗ね、、鏡観たことある？", "あ？？は？？"]
        simoneta_hentou_tinnpoxx = random.choice(random_simoneta_hentou13)
        await message.channel.send(simoneta_hentou_tinnpoxx)                                

    # 名前付きで返す
    if message.content.startswith("ライラ"):
        random_namae_henji = ["君呼んだ？", "君呼んだー？", "君なんか用ー？", "君やほい", "君おつかり！", "君やっほ！", "君呼んだかな～？", "♡"]
        namae_henji = random.choice(random_namae_henji)
        username = message.author.name
        await message.channel.send(username + namae_henji )     

    if message.content.startswith("Lyla"):
        random_namae_henji2 = ["君呼んだ？", "君呼んだー？", "君なんか用ー？", "君やほい", "君おつかり！", "君やっほ！", "君呼んだかな～？", "♡"]
        namae_henji2 = random.choice(random_namae_henji2)
        username = message.author.name
        await message.channel.send(username + namae_henji2 ) 

    if message.content.startswith("lyla"):
        random_namae_henji3 = ["君呼んだ？", "君呼んだー？", "君なんか用ー？", "君やほい", "君おつかり！", "君やっほ！", "君呼んだかな～？", "♡"]
        namae_henji3 = random.choice(random_namae_henji3)
        username = message.author.name
        await message.channel.send(username + namae_henji3 )  

    if message.content.startswith("ライラ好き"):
        random_namae_henji4 = ["ｸﾝありがと！", "君ありがと！♡", "君照れる", "君口が達者ね", "君好きよ！", "♡"]
        namae_henji4 = random.choice(random_namae_henji4)
        username = message.author.name
        await message.channel.send(username + namae_henji4 ) 

    if message.content.startswith("ライラちゃん好き"):
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

    # しょーもな返答リスト
    if message.content.startswith("俺以外ダメージでてなさすぎ"):
        await message.channel.send('それで負けてるんだから意味ねえんだよ　しょーもないハラスしてる暇あったらオブジェクト絡めボケ') 
        
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
            count += 1
            if(count == 5):
               break  
    
    # google検索モードへの切り替え
    if message.content.endswith("検索して"):
        ModeFlag = 1
        await message.channel.send('何について調べるー？')  
    
    #!SHUTDOWN_BOTが入力されたら強制終了
    if message.content.startswith('!SHUTDOWN_BOT_LYLA'):
        await message.channel.send('おやすみなさい( ˘ω˘ )')
        await client.logout()
        await sys.exit()              

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)


    

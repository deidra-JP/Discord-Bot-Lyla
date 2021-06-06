import discord
import random

client = discord.Client()


async def greeting_jp_message(message):
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
     #下ネタ返答リスト
    if message.content.endswith("ちんこ"):    
        random_simoneta_hentou = ["は？", "最低ね", "はぁ？", "低俗ね", "あ？？？？"]
        simoneta_hentou_tinnko = random.choice(random_simoneta_hentou)
        await message.channel.send(simoneta_hentou_tinnko)
    if message.content.endswith("まんこ"):    
        random_simoneta_hentou2 = ["は？最低", "最低ね・・・", "はぁ？ちょっと", "低俗ねあなた", "あぁ？？？？"]
        simoneta_hentou_manko = random.choice(random_simoneta_hentou2)
        await message.channel.send(simoneta_hentou_manko) 
    if message.content.endswith("おちんちん"):    
        random_simoneta_hentou3 = ["何言ってるの？", "あなた最低ね", "ねえはぁ？", "ほんと低俗ね", "あ？"]
        simoneta_hentou_otinntinn = random.choice(random_simoneta_hentou3)
        await message.channel.send(simoneta_hentou_otinntinn)  
    if message.content.endswith("ちんぽ"):    
        random_simoneta_hentou4 = ["は？きも", "きもい最低ね", "はぁ？ちょっとやめて", "最低で低俗ね", "あ？？"]
        simoneta_hentou_tinnpo = random.choice(random_simoneta_hentou4)
        await message.channel.send(simoneta_hentou_tinnpo)  
    if message.content.endswith("うんこ"):    
        random_simoneta_hentou5 = ["トイレ行ってきな", "小学生か", "きちゃない", "手洗った？", "トイレットペーパーあった？"]
        simoneta_hentou_unnko = random.choice(random_simoneta_hentou5)
        await message.channel.send(simoneta_hentou_unnko)          
    if message.content.endswith("うんち"):    
        random_simoneta_hentou6 = ["トイレ行ってきなて", "中学生か", "きちゃないよ", "手洗ったかい？", "トイレットペーパー足しといて"]
        simoneta_hentou_unnti = random.choice(random_simoneta_hentou6)
        await message.channel.send(simoneta_hentou_unnti) 
    if message.content.endswith("ﾁﾝﾎﾟ"):    
        random_simoneta_hentou7 = ["は？きも", "きもい最低ね", "はぁ？ちょっとやめて", "最低で低俗ね", "あ？？"]
        simoneta_hentou_tinnpox = random.choice(random_simoneta_hentou7)
        await message.channel.send(simoneta_hentou_tinnpox) 
    if message.content.endswith("ウンチ"):    
        random_simoneta_hentou8 = ["はやくトイレ行ってきなて", "男子中学生か", "きちゃないよぺっぺ", "手洗ったかな？", "トイレットペーパー足して"]
        simoneta_hentou_unntixx = random.choice(random_simoneta_hentou8)
        await message.channel.send(simoneta_hentou_unntixx)  
    if message.content.endswith("ウンコ"):    
        random_simoneta_hentou9 = ["トイレ行ってきなゴリラ", "ゴリラ", "ウホ", "？", "トイレットペーパー使える？"]
        simoneta_hentou_unnkoxx = random.choice(random_simoneta_hentou9)
        await message.channel.send(simoneta_hentou_unnkoxx)   
    if message.content.endswith("チンコ"):    
        random_simoneta_hentou10 = ["は・・・？", "最低ねほんと", "はぁ・・・？", "低俗ねほんと", "あ？？は？？"]
        simoneta_hentou_tinnkoxx = random.choice(random_simoneta_hentou10)
        await message.channel.send(simoneta_hentou_tinnkoxx)     
    if message.content.endswith("マンコ"):    
        random_simoneta_hentou11 = ["は？最低・・・", "最低ね・・・やめて", "はぁ？ちょっときもい", "最低最悪低俗ねあなた", "あぁ？？？？もっかいいってみ？"]
        simoneta_hentou_mankoxx = random.choice(random_simoneta_hentou11)
        await message.channel.send(simoneta_hentou_mankoxx)  
    if message.content.endswith("オチンチン"):    
        random_simoneta_hentou12 = ["何言ってるの？中年のキモオヤジ", "あなた最低ねはじを知りなさい", "ねえはぁ？やめて", "ほんっと低俗ね", "あ？ねえ"]
        simoneta_hentou_otinntinnxx = random.choice(random_simoneta_hentou12)
        await message.channel.send(simoneta_hentou_otinntinnxx)   
    if message.content.endswith("チンポ"):    
        random_simoneta_hentou13 = ["は？きもいんだけど", "きもい最低クズ", "はぁ？ちょっとやめてださないでよ", "最低で低俗ね、、鏡観たことある？", "あ？？は？？"]
        simoneta_hentou_tinnpoxx = random.choice(random_simoneta_hentou13)
        await message.channel.send(simoneta_hentou_tinnpoxx)     

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
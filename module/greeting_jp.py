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
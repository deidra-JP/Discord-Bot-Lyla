from re import T
import discord
import pickle
import os
import random

client = discord.Client()
game_path = "C:/Users/deidra/Desktop/学習用プロジェクト/Py_discord_bot_lyla/.game/"
HieroglypheFlag = 0
HieroglypheUserFlag = 0
HUsercount = 0
HUsercount_f1 = 0
HieroMagia_f1 = 0
HieroMagia_f2 = 0
HieroMagia_f3 = 0
HieroMagia_f4 = 0
hieroglyphe_deck_list = []
HieroMagia_game_user_list = []
HieroMagia_game_hand_list = []
HCardCheck = True
message_reset = 0


Dicegame_user_list = []
DicegameFlag = 0
DicegameUserFlag = 0
D_count = 0
D_U_count = 0


    


#HieroMagiaゲーム用関数
async def HieroMagia_message(message):

    global HieroglypheFlag
    global HieroglypheUserFlag
    global HUsercount
    global HUsercount_f1
    global HieroMagia_f1
    global HieroMagia_f2
    global HieroMagia_f3
    global HieroMagia_f4
    global hieroglyphe_deck_list
    global HCardCheck
    global message_reset
  


    # HieroMagia ゲームユーザー設定 (1)
    if HieroglypheUserFlag == 1:
        Hieroglyphe_user_join = message.content
        if Hieroglyphe_user_join == "参戦":
            Hieroglyphe_user = message.author.name
            name_Hieroglyphe_user = str(Hieroglyphe_user)
            HieroMagia_game_user_list.append(name_Hieroglyphe_user)
            await message.channel.send("把握")
        elif message.content == ("〆切"):    
            await message.channel.send("じゃあこれでゲーム始めるよ～")
            hieroglyphe_deck_list = ["𓄿  a - 1", "𓇋  a - 2", "𓇌  a - 3", "𓏭  a - 4",
              "𓂝  a - 5", "𓅱  a - 6", "𓏲  a - 7", "𓃀  a - 8", "𓊪  a - 9", "𓆑  a - 10",
              "𓅓  a - 11", "𓐝  a - 12", "𓈖  a - 13", "𓋔  b - 1", "𓂋  b - 2", "𓉔  b - 3",
              "𓎛  b - 4", "𓐍  b - 5", "𓄡  b - 6", "𓋴  b - 7", "𓊃  b - 8", "𓈙  b - 9",
               "𓈛  b - 10", "𓈜  b - 11", "𓈎  b - 12", "𓎡  b - 13", "𓎼  c - 1", "𓎤  c - 2",
              "𓏏  c - 3", "𓍘  c - 4", "𓍿  c - 5", "𓂧  c - 6", "𓆓  c - 7", "𓀀  c - 8",
              "𓀁  c - 9", "𓀂  c - 10", "𓀃  c - 11", "𓀄  c - 12", "𓀅  c - 13", "𓀆  d - 17",
              "𓀇  d - 19"]
            HieroglypheUserFlag = 0
            HieroglypheFlag = 1 
        else:
            random_sizukani = ["しーっ！！", "黙れええええええええ！！", "ちょい静かに！", "参戦希望以外は一回しずかに！", "ちょいまち"]   
            sizukani_site = random.choice(random_sizukani)
            await message.channel.send(sizukani_site)     
    
    # HieroMagia ゲーム機能 開始フェーズ (2)
    if HieroglypheFlag == 1:
        for HieroMagia_user_name in HieroMagia_game_user_list:
            await message.channel.send(HieroMagia_user_name)
            HUsercount += 1
            await message.channel.send(str(HUsercount) + "番")
            slot_random_shuffle = random.sample(hieroglyphe_deck_list, 5)
            for hieroglyphe_list in slot_random_shuffle:
                await message.channel.send(hieroglyphe_list)  
                HieroMagia_game_hand_list.append(hieroglyphe_list)  
                hm_text_path = os.path.join(game_path, "HieroMagia" + str(HieroMagia_user_name) + "_hand.sav")        
                gfile = open(hm_text_path, "wb")  
                pickle.dump(HieroMagia_game_hand_list,gfile)
                gfile.close()
                print(HieroMagia_game_hand_list)
            HieroMagia_game_hand_list.clear()
            for deck_remove in slot_random_shuffle:
                hieroglyphe_deck_list.remove(deck_remove)
        await message.channel.send("手札オープン")
        print(hieroglyphe_deck_list)
        HieroglypheFlag = 0
        HieroMagia_f1 = 1
        await message.channel.send("１番の人から順に交換したい手札をコピペしてね！")

    if HieroMagia_f1 == 1:   
        if not message.content.endswith("〆切"): 
            for HieroMagia_f1_user in HieroMagia_game_user_list:
                if message.author.name == HieroMagia_f1_user:
                    HUsercount_f1 += 1
                    Card_Change = message.content
                    hm_text_path = os.path.join(game_path, "HieroMagia" + str(HieroMagia_f1_user) + "_hand.sav")        
                    gfile = open(hm_text_path, "rb") 
                    a_HHand_list = pickle.load(gfile)
                    a_HHand_list.remove(Card_Change) 
                    b_HHand_list = random.sample(hieroglyphe_deck_list, 1)
                    c_HHand_list = b_HHand_list[0]
                    a_HHand_list.append(c_HHand_list)
                    hieroglyphe_deck_list.remove(c_HHand_list)
                    gfile.close()
                    gfile = open(hm_text_path, "wb")
                    pickle.dump(a_HHand_list,gfile)
                    gfile.close()
                    await message.channel.send(a_HHand_list)
                    for Change_HieroMagia_game_hand_list in a_HHand_list:
                        await message.channel.send(Change_HieroMagia_game_hand_list)  
                    print(hieroglyphe_deck_list)          
                    if HUsercount == HUsercount_f1:
                        HieroMagia_f1 = 0
                        HieroMagia_f2 = 1
                        await message.channel.send("フェーズ２にいくよ！")
                    else:
                        await message.channel.send("次の人交換したいカードをコピペしてね！")
    # HieroMagia ゲーム機能呼び出し (0)
    if message.content.endswith("HieroMagiaお願い"):
        await message.channel.send("誰が遊ぶ-？ やるなら参戦って打って！OKだったら〆切って打ってね～")
        HieroglypheUserFlag = 1
        

#//////////////////////////////////////////////////////////////////////////////////

async def Dicegame_message(message):    
    
    global DicegameFlag
    global DicegameUserFlag
    global D_count
    global D_U_count 
    
    
    
    # サイコロゲーム　ゲームユーザー設定
    if DicegameUserFlag == 1:
        if message.content.endswith("参戦"):
            dicegame_user = message.author.name
            dicegame_user_id = str(dicegame_user)
            Dicegame_user_list.append(dicegame_user_id)
            await message.channel.send("把握")
            D_U_count += 1
        else:
            random_sizukani = ["静かに！！！！", "静かにしててええ", "ちょっと静かにしててええ", "今は黙れ＾＾", "黙ってて＾＾", "うるさい＾＾", "今余計なこと喋らないで＾＾", "口を閉じて＾＾"]
            sizukani_message = random.choice(random_sizukani)
            await message.channel.send(sizukani_message)
        if D_U_count == 2:
            await message.channel.send("いざ、勝負。")
            DicegameUserFlag = 0
            DicegameFlag = 1
            D_U_count = 0    
    
    #サイコロゲーム　ゲーム機能
    if DicegameFlag == 1:
        for dicegame_user_name in Dicegame_user_list:
            await message.channel.send(dicegame_user_name)
            D_count += 1
            random_dice = random.randrange(1,6)
            message_dice = str(random_dice)
            await message.channel.send(message_dice)
            if D_count == 1:
                u1 = message_dice
            if D_count == 2: 
                u2 = message_dice
        if u1 > u2:
            await message.channel.send("-------" + str(Dicegame_user_list[0]) + "の勝ち-------")
            D_count = 0
            DicegameFlag = 0
        if u2 > u1:
            await message.channel.send("-------" + str(Dicegame_user_list[1]) + "の勝ち-------")
            D_count = 0
            DicegameFlag = 0
        if u1 == u2:
            await message.channel.send("引き分け")
            D_count = 0
            DicegameFlag = 0
    #サイコロゲーム ゲーム機能呼び出し
    if message.content.endswith("サイコロゲームお願い"):
        await message.channel.send("2人用ゲームね！参加者は参戦って入力して～")
        DicegameUserFlag = 1
from re import S
import discord
import datetime
import gspread
from google.oauth2.service_account import Credentials
from gspread.models import Spreadsheet

client = discord.Client()

# スプシを開く
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

ledger_frag = "終"

# ledger関数で使用する関数
# 日付ごとのシートを作成し、最低限のフレームを作成
def monthcheck():
    worksheet_feed = sh.worksheets()              
    today = datetime.date.today().strftime("%Y%m")    
    exist = False
    for current in worksheet_feed:
        if current.title == today:
            exist = True                                
    if exist == False:                                 
         sh.add_worksheet(title = today, rows = 100, cols = 4)      
         newsheet = sh.worksheet(today) 
         newsheet.update("A1", "収入")
         newsheet.update("C1", "支出")   
    return sh.worksheet(today)

# 収入をインポート
def add_income(worksheet, name, amount):
    lists = worksheet.get_all_values()  
    rows = len(lists) + 1               
    worksheet.update_cell(rows, 1, name)  
    worksheet.update_cell(rows, 2, amount)

# 支出をインポート    
def add_spending(worksheet, name, amount):
    lists = worksheet.get_all_values()
    rows = len(lists) + 1               
    worksheet.update_cell(rows, 3, name)  
    worksheet.update_cell(rows, 4, amount)

# まとめのシートを日付ごとに作成し更新
def check_total(worksheet):             
    lists = worksheet.get_all_values()  
    rows = len(lists)                   
    worksheet.update("B1", "=SUM(B2:B" + str(rows) + ")", value_input_option = "USER_ENTERED")  
    worksheet.update("D1", "=SUM(D2:D" + str(rows) + ")", value_input_option = "USER_ENTERED") 
    today = datetime.date.today().strftime("%Y/%m")         
    con_worksheet = sh.worksheet("まとめ")                    
    conclusion = con_worksheet.get_all_values()
    exist = False
    index = 1
    for day in conclusion:                                     
        if day[0] == today:
            exist = True
            break
        index = index + 1
   
    if exist == False:                                         
        index = len(conclusion) + 1 
        con_worksheet.update_cell(index,1,today)
            
    con_worksheet.update_cell(index,2,worksheet.acell("B1").value)
    con_worksheet.update_cell(index,3,worksheet.acell("D1").value)

    conclusion = con_worksheet.get_all_values()                 
    con_rows = len(conclusion) 
    
    con_worksheet.update("B2", "=SUM(B3:B" + str(con_rows) + ")", value_input_option = "USER_ENTERED")  
    con_worksheet.update("C2", "=SUM(C3:C" + str(con_rows) + ")", value_input_option = "USER_ENTERED")  

# 収入のチェック
def check_income(worksheet):           
    return worksheet.acell("B1").value  

# 支出のチェック
def check_spending(worksheet):        
    return worksheet.acell("D1").value 



# インポート先で呼び出す関数
async def ledger(message):  
    global ledger_frag
    if message.content == "終了":     
        ledger_frag = "終"
        await message.channel.send("おつかり！")
    if ledger_frag == "":     
        today = datetime.date.today().strftime("%Y%m")
        worksheet = monthcheck()
        receipt = message.content.split(",")
        if receipt[0] == "収入":
            receipt[2] = receipt[2].replace("円", "")
            if len(receipt) != 3:                      
                await message.channel.send("これ無効だよ！　フォーマットにしたがってね　：例：　収入、なにで収入を得たか、10000円")     
            add_income(worksheet, str(receipt[1]), int(receipt[2]))   
            check_total(worksheet)  
            await message.channel.send("" + receipt[1] + "による収入" + receipt[2]+ "円を記録しました。\r\n記録後の今月の収入は" + str(int(check_income(worksheet))) + "円です。")
        elif receipt[0] == "支出":
            receipt[2] = receipt[2].replace("円", "")
            if len(receipt) != 3:                      
                await message.channel.send("これ無効だよ！　フォーマットにしたがってね　：例：　支出、なににお金使ったか、10000円")     
            add_spending(worksheet, str(receipt[1]), int(receipt[2]))   
            check_total(worksheet)  
            await message.channel.send("" + receipt[1] + "による支出" + receipt[2] + "円を記録しました。\r\n記録後の今月の支出は" + str(int(check_spending(worksheet))) + "円です。")
        elif message.content == "シート":
            await message.channel.send("https://docs.google.com/spreadsheets/d/1pAoo-uQ9fyjtx_zIp0Z_zM2aP8bwlEkAnoLhVRq9fQI/edit#gid=0")
        elif message.content == "今月の収入":         
            await message.channel.send("今月の収入は" + str(int(check_income(worksheet))) + "円です。")
        elif message.content == "今月の支出":         
            await message.channel.send("今月の支出は" + str(int(check_spending(worksheet))) + "円です。")        
        else :       
            # テスト用　
            print(sh.worksheet(today).get("A1"))
                
    if message.content.endswith("スプレッドシートお願い"):
        worksheet_matome = 1
        worksheet_today = 1
        worksheets = sh.worksheets()
        for sheet in worksheets:
            if sheet.title == "まとめ":
                worksheet_matome += 1
            else:  
                worksheet_today += 1
        if worksheet_matome == 1:
            sh.add_worksheet(title = "まとめ", rows = 100, cols = 4)
        ledger_frag = ""
        await message.channel.send("スプレッドシート管理モードに入るよ！")


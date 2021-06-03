import discord
import datetime
import gspread
from discord.ext import commands
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



def monthcheck():
    worksheet_feed = sh.worksheets()              
    today = datetime.date.today().strftime("%Y%m")    
    exist = False
    for current in worksheet_feed:
        if current.title == today:
            exist = True                                
    if exist == False:                                 
         sh.add_worksheet(title=today, rows = 100, cols = 4)      
         newsheet = sh.worksheet(today) 
         newsheet.update("A1","収入")
         newsheet.update("C1","支出")   
    return sh.worksheet(today)

def add_income(worksheet, name, amount):
    worksheet = monthcheck()
    lists = worksheet.get_all_values()  
    rows = len(lists) + 1               
    worksheet.update_cell(rows,1,name)  
    worksheet.update_cell(rows,2,amount)
    
def add_spending(worksheet, name, amount):
    worksheet = monthcheck()
    lists = worksheet.get_all_values()
    rows = len(lists) + 1               
    worksheet.update_cell(rows,3,name)  
    worksheet.update_cell(rows,4,amount)

def check_total(worksheet):             
    worksheet = monthcheck()
    lists = worksheet.get_all_values()  
    rows = len(lists)                   
    worksheet.update("B1",'=SUM(B2:B'+str(rows)+')',value_input_option='USER_ENTERED')  
    worksheet.update("D1",'=SUM(D2:D'+str(rows)+')',value_input_option='USER_ENTERED') 
    today = datetime.date.today().strftime("%Y/%m")         
    con_worksheet = sh.worksheet("まとめ")                    
    conclusion = con_worksheet.get_all_values()
    exist = False
    index = 1
    for day in conclusion :                                     
        if day[0] == today :
            exist = True
            break
        index = index + 1
   
    if exist == False :                                         
        index = len(conclusion) + 1
        con_worksheet.update_cell(index,1,today)
            
    con_worksheet.update_cell(index,2,worksheet.acell("B1").value)
    con_worksheet.update_cell(index,3,worksheet.acell("D1").value)

    conclusion = con_worksheet.get_all_values()                 
    con_rows = len(conclusion) 
    
    con_worksheet.update("B2",'=SUM(B3:B'+str(con_rows)+')',value_input_option='USER_ENTERED')  
    con_worksheet.update("C2","=SUM(C3:C"+str(con_rows)+')',value_input_option='USER_ENTERED')  

def check_income(worksheet):   
    worksheet = monthcheck()         
    return worksheet.acell("B1").value  

def check_spending(worksheet):        
    worksheet = monthcheck()  
    return worksheet.acell("D1").value 

async def ledger(message):
    if message.content.endswith("スプシ"):
        monthcheck()
        today = datetime.date.today().strftime("%Y%m")
        print(sh.worksheet(today).get("A1"))
    
    worksheet = monthcheck()
    
    if message.content == "シート" :
            await message.channel.send("https://docs.google.com/spreadsheets/d/1pAoo-uQ9fyjtx_zIp0Z_zM2aP8bwlEkAnoLhVRq9fQI/edit#gid=0")
    if message.content == "今月の収入" :         
            await message.channel.send("今月の収入は"+str(int(check_income(worksheet)))+"円です。")
    if message.content == "今月の支出" :         
            await message.channel.send("今月の支出は"+str(int(check_spending(worksheet)))+"円です。")
    
    receipt = message.content.split(',')

    if len(receipt) != 3 :                      #支出、収入の入力がフォーマットに沿ってなかったら弾く
            await message.channel.send('入力が無効')
            return
    receipt[2] = receipt[2].replace('円','')     #金額に円と付いてたらその部分を取り除く
    if receipt[0] == '収入' :
            add_income(worksheet,str(receipt[1]),int(receipt[2]))   #収入を書き込む
            check_total(worksheet)  #収支の合計をチェックし入力させる
            await message.channel.send(''+receipt[1]+'による収入'+receipt[2]+'円を記録しました。\r\n記録後の今月の収入は'+str(int(check_income(worksheet)))+'円です。')
            return
    elif receipt[0] == '支出' :
            add_spending(worksheet,str(receipt[1]),int(receipt[2]))   #収入を書き込む
            check_total(worksheet)  #収支の合計をチェックし入力させる
            await message.channel.send(''+receipt[1]+'による支出'+receipt[2]+'円を記録しました。\r\n記録後の今月の支出は'+str(int(check_spending(worksheet)))+'円です。')
            return
    else :
            await message.channel.send('入力が無効')
            return    
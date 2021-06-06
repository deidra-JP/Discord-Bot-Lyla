import discord
import random

client = discord.Client()

async def picture_message(message):
# 画像返答
    if message.content == "画像お願い":
        atarimaeda_path = 'C:/Users/deidra/Desktop/学習用プロジェクト/Py_discord_bot_lyla/.picture/illegal/1.jpg'
        hansei_path = 'C:/Users/deidra/Desktop/学習用プロジェクト/Py_discord_bot_lyla/.picture/illegal/2.png'
        file = [atarimaeda_path, hansei_path]
        file2 = random.choice(file)
        file3 = discord.File(file2, filename=file2)
        await message.channel.send(file=file3)
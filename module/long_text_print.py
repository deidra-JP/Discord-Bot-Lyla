import discord
import random

client = discord.Client()


async def long_text_message(message):
# テキスト長文返答
    if message.content == "長文お願い":
        Ethereum1_path = 'C:/Users/deidra/Desktop/学習用プロジェクト/Py_discord_bot_lyla/.long_text/Ethereum/1.txt'
        Ethereum2_path = 'C:/Users/deidra/Desktop/学習用プロジェクト/Py_discord_bot_lyla/.long_text/Ethereum/2.txt'
        file = [Ethereum1_path, Ethereum2_path]
        file2 = random.choice(file)
        file3 = discord.File(file2, filename=file2)
        await message.channel.send(file=file3)

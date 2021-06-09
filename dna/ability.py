import discord
import random

client = discord.Client()
ability0_4 = []

ability_list = [
# あ行
"愛情",
"暗黒",
"安全",
"安心感",
"安堵",
"哀悼",
"悪辣",
"悪徳",
"悪心",
"医療",
"意思",
"因子",
"育児",
"引導",
"移送",
"陰鬱",
"陰惨",
"稲妻",
"雷",
"嘶き",
"岩",
"岩浪",
"石垣",
]

async def choice_ability(message):
    if message.content.endswith("アビリティ取得お願い"):
        ability = {
            # あ行
            "愛情": "03b,01a,34a,22s,43s,06r",
            "暗黒": "03b,01a,34a,22s,43s,06r",
            "安全": "03b,01a,34a,22s,43s,06r",
            "安心感": "03b,01a,34a,22s,43s,06r",
            "安堵": "03b,01a,34a,22s,43s,06r",
            "哀悼": "03b,01a,34a,22s,43s,06r",
            "悪辣": "03b,01a,34a,22s,43s,06r",
            "悪徳": "03b,01a,34a,22s,43s,06r",
            "悪心": "03b,01a,34a,22s,43s,06r",
            "医療": "03b,01a,34a,22s,43s,06r",
            "意思": "03b,01a,34a,22s,43s,06r",
            "因子": "03b,01a,34a,22s,43s,06r",
            "育児": "03b,01a,34a,22s,43s,06r",
            "引導": "03b,01a,34a,22s,43s,06r",
            "移送": "03b,01a,34a,22s,43s,06r",
            "陰鬱": "03b,01a,34a,22s,43s,06r",
            "陰惨": "03b,01a,34a,22s,43s,06r",
            "稲妻": "03b,01a,34a,22s,43s,06r",
            "雷": "03b,01a,34a,22s,43s,06r",
            "嘶き": "03b,01a,34a,22s,43s,06r",
            "岩": "03b,01a,34a,22s,43s,06r",
            "岩浪": "03b,01a,34a,22s,43s,06r",
            "石垣": "03b,01a,34a,22s,43s,06r",
        }
        
        ability_random_shuffle = random.sample(ability_list, 5)
        ability0_4.append(ability[ability_random_shuffle[0]])
        ability0_4.append(ability[ability_random_shuffle[1]])
        ability0_4.append(ability[ability_random_shuffle[2]])
        ability0_4.append(ability[ability_random_shuffle[3]])
        ability0_4.append(ability[ability_random_shuffle[4]])
        await message.channel.send(ability0_4)

        ability0 = ability0_4[0]
        ability0s = ability0.split(',')
        await message.channel.send(ability0s)
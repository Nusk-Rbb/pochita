import discord
import discord.member as member
import discord.message as message
TOKEN = "MTA1NTQ5NjI5OTY5MDA4MjM3NA.GOa-KH.B0cuNLAw1QUHroNg5WiF2RzUcvxQyklDx3FERY"
id_absent_channel = 1052268392637284492
id_absent_role = 1057638045643456542
emoji_absent = '❌'


client = discord.Client()

@client.event
async def on_ready():
    #ログインしたらメッセージを表示する
    print("Log in")    


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '/dog':
        await message.channel.send('わん！')


client.run(TOKEN)
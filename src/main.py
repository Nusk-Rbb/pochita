import discord
import config

f = open("config.txt", "r")
datalist = f.readline()

id_absent_channel = datalist[0]
 d_absent_role = datalist[1]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    #ログインしたらメッセージを表示する
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(str(config.TOKEN))
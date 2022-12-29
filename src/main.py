import discord
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN", None)

id_absent_channel = 1052268392637284492
id_absent_role = 1057638045643456542

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


client.run(str(TOKEN))
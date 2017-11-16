import discord
import asyncio
from pathlib import Path

client = discord.Client()

@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)

@client.event
async def on_message(message):
    print("Message posted by", message.author)
    if str(message.author) == "apokalyptikprophet#0900":
        content = message.content
        content = content.replace("s", "sss")
        await client.edit_message(message, content)

token = None
token_fp = Path(__file__).parent / Path("bot.token")
with token_fp.open("r", encoding="utf-8") as f:
    token = f.read()
    token = token.replace("\n", "")

client.run(token)

import logging
import discord
import asyncio
from pathlib import Path


logging.basicConfig(level=logging.INFO)
client = discord.Client()


@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)


@client.event
async def on_message(message):
    is_me = True if str(message.author) == "apokalyptikprophet#0900" else False
    # if is_me:
    #     print(f"Message on {message.server.name}-{message.channel.id}")
    ch_id = message.channel.id
    is_correct_channel = True if ch_id == "368380401095409668" else False
    if is_me and is_correct_channel:
        # print(f"Processing message on {message.channel.id}...")
        content = message.content
        modified = content.replace("s", "sss")
        if content != modified:
            # print("Replaced 's's with 'sss's - editing message!")
            await client.edit_message(message, modified)


token = None
token_fp = Path(__file__).parent / Path("bot.token")
with token_fp.open("r", encoding="utf-8") as f:
    token = f.read()
    token = token.replace("\n", "")

client.run(token, bot=False)

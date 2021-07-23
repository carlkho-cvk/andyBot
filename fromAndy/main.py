import os
import discord
from hentai import Hentai, Format, Option
from keepalive import keepalive
# bot
client = discord.Client()

# IMPORTANT
# placeChannelID Here
# placeBotToken here

my_secret = os.environ['token']
@client.event
async def on_ready():
    print("Bot on!")

@client.event
async def on_message(message):


     if len(message.content) == 6:
        await message.channel.send("Nice")

        code = message.content

        doujin = Hentai(code)
        Hentai.exists(doujin.id)
        await message.channel.send("You looked for: " + doujin.title(Format.Pretty))
        await message.channel.send([tag.name for tag in doujin.tag])
        await message.channel.send(doujin.upload_date)
        
        for x in doujin.image_urls:
           await message.channel.send(x)

        await message.reply('Start reading from the top. Click the message I am replying to above me!', mention_author=False)

# Run on server
keepalive()
client.run(my_secret)
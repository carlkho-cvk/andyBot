import discord
from hentai import Hentai, Format, Option

# make a request to nhentai.net
doujin = Hentai(177013)
date = doujin.upload_date


# bot
client = discord.Client()

# IMPORTANT
# placeChannelID Here
channel_ID = 866334360542249021
# placeBotToken here
botToken = "ODY0NDE2NjMzMDE4Mzg0NDA0.YO1IuQ.eoV7yQZ0jfyKVEEVTILBfn7zysM"



@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        embedVar = discord.Embed(title=doujin.title(Format.Pretty), description="Enjoy your jackol! ;)", color=0xFF33FF)
        embedVar.add_field(name="Tags", value=[tag.name for tag in doujin.tag], inline=False)
        embedVar.add_field(name="Upload Date", value=doujin.upload_date, inline=False)
        await message.channel.send(embed=embedVar)

# Run on server
client.run(botToken)
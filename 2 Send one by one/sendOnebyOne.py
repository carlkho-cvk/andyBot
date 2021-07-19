import discord
from hentai import Hentai, Format

# variables for Discord bot
client = discord.Client()

# IMPORTANT
# placeChannelID Here
channel_ID = 866334360542249021
# placeBotToken here
botToken = "ODY0NDE2NjMzMDE4Mzg0NDA0.YO1IuQ.eoV7yQZ0jfyKVEEVTILBfn7zysM"

# variables for Hentai
doujin = Hentai(321942)
Hentai.exists(doujin.id)

# variables for Discord bot
@client.event
async def on_message(message):
    if message.content.startswith('!hello'):

        general_channel = client.get_channel(channel_ID)

        for x in doujin.image_urls:
            await general_channel.send(x)

#run bot on Discord
client.run(botToken)
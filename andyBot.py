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

        # step 1 - give details
        embedVar = discord.Embed(title=doujin.title(Format.Pretty), description="yummy", color=0xFF33FF)
        embedVar.add_field(name="tag", value=[tag.name for tag in doujin.tag], inline=False)
        embedVar.add_field(name="upload date", value=doujin.upload_date, inline=False)
        await message.channel.send(embed=embedVar)

        # step 2 - place all panels
        for x in doujin.image_urls:
            await general_channel.send(x)

        # step 3 - reply to embed
        await message.reply('Start reading from the top. Click the message I am replying to above me!', mention_author=False)

#run bot on Discord
client.run(botToken)
from hentai import Hentai, Format
import discord

# bot
client = discord.Client()

# IMPORTANT
# placeChannelID Here
channel_ID = 855337824420364298
# placeBotToken here
botToken = "ODY0NDE2NjMzMDE4Mzg0NDA0.YO1IuQ.eoV7yQZ0jfyKVEEVTILBfn7zysM"

# make a request to nhentai.net
chosenDoujin = Hentai(177013)
allPagesUrls = chosenDoujin.image_urls
noPages = len(allPagesUrls)

# True
Hentai.exists(chosenDoujin.id)

# ['https://i.nhentai.net/galleries/987560/1.jpg', ... ]

# initiateBot
@client.event
async def on_ready():
    print("start")
    general_channel = client.get_channel(channel_ID)
    await general_channel.send((next(iter(allPagesUrls))))

# Run on server
client.run(botToken)
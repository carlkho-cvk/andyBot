import discord
from discord.ext import tasks

# bot
client = discord.Client()

# IMPORTANT
# placeChannelID Here
channel_ID = 866334360542249021
# placeBotToken here
botToken = "ODY0NDE2NjMzMDE4Mzg0NDA0.YO1IuQ.eoV7yQZ0jfyKVEEVTILBfn7zysM"\

@tasks.loop(seconds = 1) # repeat after every 10 seconds
async def myLoop():
    general_channel = client.get_channel(channel_ID)
    await general_channel.send("Bayot Andy jackolero no judge tho", delete_after=20)

myLoop.start()

# Run on server
client.run(botToken)
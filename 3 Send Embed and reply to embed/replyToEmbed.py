import discord.ext

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
        await message.reply('Hello!', mention_author=True)


# Run on server
client.run(botToken)
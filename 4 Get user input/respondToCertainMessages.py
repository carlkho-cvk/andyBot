import discord

# bot
client = discord.Client()

# IMPORTANT
# placeChannelID Here
channel_ID = 855337824420364298
# placeBotToken here
botToken = "ODY0NDE2NjMzMDE4Mzg0NDA0.YO1IuQ.eoV7yQZ0jfyKVEEVTILBfn7zysM"

@client.event
async def on_ready():
    print("Bot on!")

@client.event
async def on_message(message):
    if len(message.content) == 6:
        general_channel = client.get_channel(channel_ID)
        await general_channel.send("Nice")

        code = message.content
        await general_channel.send("You looked for: " + code)

# Run on server
client.run(botToken)


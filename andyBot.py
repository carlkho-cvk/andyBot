import discord
from hentai import Hentai, Format

# variables for Discord bot
client = discord.Client()

# IMPORTANT
# placeChannelID Here
channel_ID = 866334360542249021
# placeBotToken here
botToken = ""

# variables for Hentai
doujin = Hentai(321942)
Hentai.exists(doujin.id)

# variables for Discord bot


# give instructions
@client.event
async def on_ready():
    print("Bot on!")
    general_channel = client.get_channel(channel_ID)
    await general_channel.send('Place a 6-digit code to get the whole doujin')

# when user places a 6-digit code
@client.event
async def on_message(message):

    general_channel = client.get_channel(channel_ID)

    # step 0 - ask user for code
    if len(message.content) == 6:
        await message.channel.send("Nice")

        code = message.content

        doujin = Hentai(code)
        Hentai.exists(doujin.id)
        await message.channel.send("You looked for: ")

        # step 1 - give details
        embedVar = discord.Embed(title=doujin.title(Format.Pretty), color=0xFF33FF)
        embedVar.add_field(name="tag", value=str([tag.name for tag in doujin.tag]), inline=False)
        embedVar.add_field(name="upload date", value=str(doujin.upload_date), inline=False)
        await message.channel.send(embed=embedVar)

        # step 2 - place all panels
        for x in doujin.image_urls:
            await general_channel.send(x)

        # step 3 - reply to orig message (read from top)
        await message.reply('Start reading from the top. Click the message I am replying to above me!', mention_author=False)

#run bot on Discord
client.run(botToken)

import discord
import random
from discord.ext import commands

description = "Luezoid's bot"
bot = commands.Bot(command_prefix = ".", description = description)
path = "alts/alt_file.txt"
alt_file = open(path, "r")

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='type .info for help'))

@bot.command(pass_context = True)
async def getalt(ctx):
    message = ctx.message
    alt_tmp = "Here's your alt: " + alt_file.readline()
    await bot.send_message(message.author, alt_tmp)
    await bot.send_message(message.channel, "{0} Check your PM for your free alt!".format(message.author.mention)) #getalt

@bot.command(pass_context = True)
async def info(ctx):
    info = """
    Hi, my name is Luezoid Bot. Here's what I can do!

    ∴Commands∴

    « Use .info to show this message! »
    « Use .youtube to see the different channels! »
    « Use .getalt to get a minecraft account! »
    « Use .flip to flip a coin! »
    « Use .embed (title, description) to format fancy text! »

    Coded by Twashi and Luezoid with Python 3.6
    """
    message = ctx.message
    em = discord.Embed(title = 'Information', description = info, colour = 0xff0000)
    em.set_author(name = 'Luezoid Bot', icon_url = "https://cdn.discordapp.com/attachments/366186774172663808/366228601844006912/LuezoidBotIcon.png")
    await bot.send_message(message.channel, embed = em)

@bot.command(pass_context = True)
async def youtube(ctx):
    yt_commands = """
    Youtube commands

    ∴Commands∴

    « Use .youtube_luezoid to see Luezoid's channel! »
    « Use .youtube_ghastly to see Ghastly Gaming's channel! »
    « Use .youtube_waitiboii to see WaiTiBoii's channel! »
    « Use .youtube_maddninjja to see Madd_Ninjja's channel! »
    """
    message = ctx.message
    em = discord.Embed(title = 'Youtube Commands', description = yt_commands, colour = 0xff0000)
    em.set_author(name = 'Luezoid Bot', icon_url = "https://cdn.discordapp.com/attachments/366186774172663808/366228601844006912/LuezoidBotIcon.png")
    await bot.send_message(message.channel, embed = em)

@bot.command()
async def flip():
    flip = ["Heads!", "Tails!"] # define variable
    flipped_coin = random.choice(flip) # choose heads or tails
    await bot.say(flipped_coin) # say heads or tails

@bot.command(pass_context = True)
async def youtube_luezoid(ctx):
    message = ctx.message
    em = discord.Embed(title = 'Sub to Luezoid', description = 'Click the link above to sub!', colour = 0xff0000, url = "https://www.youtube.com/channel/UCNmMi5tPCWkrJLzWN29mceA?sub_confirmation=1")
    em.set_author(name = 'Luezoid Bot', icon_url = "https://cdn.discordapp.com/attachments/366186774172663808/366228601844006912/LuezoidBotIcon.png")
    await bot.send_message(message.channel, embed = em)

@bot.command(pass_context = True)
async def youtube_waitiboii(ctx):
    message = ctx.message
    em = discord.Embed(title = 'Sub to WaiTiBoii', description = 'Click the link above to sub!', colour = 0xff0000, url = "https://www.youtube.com/channel/UCFcD6-vMWTwCWzUqWpIyKVg?sub_confirmation=1")
    em.set_author(name = 'Luezoid Bot', icon_url = "https://cdn.discordapp.com/attachments/366186774172663808/366228601844006912/LuezoidBotIcon.png")
    await bot.send_message(message.channel, embed = em)

@bot.command(pass_context = True)
async def youtube_maddninjja(ctx):
    message = ctx.message
    em = discord.Embed(title = 'Sub to Madd_Ninjja', description = 'Click the link above to sub!', colour = 0xff0000, url = "https://www.youtube.com/channel/UC6-vAToW1zRNj5vbhYMMggw?sub_confirmation=1")
    em.set_author(name = 'Luezoid Bot', icon_url = "https://cdn.discordapp.com/attachments/366186774172663808/366228601844006912/LuezoidBotIcon.png")
    await bot.send_message(message.channel, embed = em)

@bot.command(pass_context = True)
async def youtube_ghastly(ctx):
    message = ctx.message
    em = discord.Embed(title = 'Sub to GhastlyGaming', description = 'Click the link above to sub!', colour = 0xff0000, url = "https://www.youtube.com/channel/UCUXOdq1ElKAJ53MK_kPcwBw?sub_confirmation=1")
    em.set_author(name = 'Luezoid Bot', icon_url = "https://cdn.discordapp.com/attachments/366186774172663808/366228601844006912/LuezoidBotIcon.png")
    await bot.send_message(message.channel, embed = em)

@bot.command(pass_context = True)
async def embed(ctx, title, desc):
    message = ctx.message
    em = discord.Embed(title = title, description = desc, color = 0xff0000)
    em.set_author(name = message.author, icon_url = "https://cdn.discordapp.com/attachments/366186774172663808/366228601844006912/LuezoidBotIcon.png")
    await bot.send_message(message.channel, embed = em)

@bot.command(pass_context = True)
async def rules(ctx):
    message = ctx.message
    desc = """
    **« Rules »**

    **Spam**
    Do not spam the text channels with random/stupid stuff

    **Swearing**
    Swearing *is* allowed, but please do not flood the chat with swear words

    **Behaviour**
    Be respectful to other players and admins

    **Listen**
    If an admin says something, listen. Simple.

    **Alts**
    Use the .getalt command to use get an alt. Repeats of alts can happen.

    **Bugs**
    Report any bugs you find to Twashi or Madd_Luezoid.
    """
    em = discord.Embed(title = "Rules", description = desc, color = 0xff0000)
    em.set_author(name = message.author, icon_url = "https://cdn.discordapp.com/attachments/366186774172663808/366228601844006912/LuezoidBotIcon.png")
    await bot.send_message(message.channel, embed = em)

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content == "Hello":
        await client.send_message(message.channel, "World")
 
bot.run("MzY2MTI1MTg3OTc4MTAwNzM2.DLoULA.Bse6p55KCBl35FfrfSb5enIpDAY") #token

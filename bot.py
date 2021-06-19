import discord
from discord.ext import commands
from decouple import config
from helpers.emoji_management import Emoji

token = config('TOKEN')

client = commands.Bot(command_prefix='.', help_command=None, activity=discord.Game(name=".help"))

emoji_class = Emoji(json_path='emojis.json')

alias_list = emoji_class.alias_list()


@client.event
async def on_ready():
    print("Bot is online!")


    


@client.command(aliases=['e'])
async def emoji_old(ctx, *, emoji):
    response = emoji_class.obtain_emoji(emoji)
    if response == 0:
        if ctx.message.author.id == 120210302364024833:
            await ctx.send(f"This emoji doesn't exist {ctx.message.author.name}, you amazing human being.")
        else:
            await ctx.send(f"This emoji doesn't exist {ctx.message.author.name}, you idiot.")
        await ctx.message.delete()
    else:
        await ctx.send(file=discord.File(response), content="Sent by **{}**".format(ctx.message.author.name))
        await ctx.message.delete()


@client.command(aliases=alias_list)
async def emoji(ctx):
    response = emoji_class.obtain_emoji(ctx.message.content[1:])
    if response == 0:
        if ctx.message.author.id == 120210302364024833:
            await ctx.send(f"This emoji doesn't exist {ctx.message.author.name}, you amazing human being.")
        else:
            await ctx.send(f"This emoji doesn't exist {ctx.message.author.name}, you idiot.")
        await ctx.message.delete()
    else:
        await ctx.send(file=discord.File(response), content="Sent by **{}**".format(ctx.message.author.name))
        await ctx.message.delete()


@client.command(aliases=['el'])
async def emojilist(ctx):
    response = emoji_class.emoji_list()
    await ctx.send(response)

@client.command(aliases=['h'])
async def help(ctx):
    response = 'First, type `.el` to see available emojis.\nThey can be accessed by typing `.emojiname`\n Depending on live updates, emojis can also be accessed using `.e emojiname`'
    await ctx.send(response)

client.run(token)

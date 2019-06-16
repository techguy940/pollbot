import discord
from discord.ext import commands

#prefix
bot=commands.Bot(command_prefix='PREFIX_HERE')

#bot_event
@bot.event
async def on_ready():
    print('Bot is online')
    print(bot.user.id)

#poll_comand
@bot.command()
async def poll(ctx,*,message):
    msg = await ctx.send(f'''Poll by {ctx.author.mention}\n{message}''')

    await msg.add_reaction('👍')
    await msg.add_reaction('👎')

#token
bot.run('TOKEN_HERE')

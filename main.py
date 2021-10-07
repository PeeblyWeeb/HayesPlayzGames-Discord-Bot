import discord
import os
import time
import random


from discord.ext import commands
from discord.ext.commands import *
from upkeep import upkeep
from asyncio import sleep
from datetime import datetime

login = os.environ['LOGIN']

prefix = 'h!'


bot = commands.Bot(
  command_prefix=prefix
)

# When logged in announce to console.
@bot.event
async def on_ready():
  print(f'Ready! Logged in as {bot.user.name}')
  await bot.change_presence(status=discord.Status.idle, activity=discord.Game('PeeblyWeeb | h!help'))


@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, CommandNotFound):
    await ctx.reply(":x: Oops, That command doesn't exist!", delete_after=1.5)
    print(str(ctx.message.author) + ' Typed: \'' + str(ctx.message.content) + '\' \n-- but the command doesn\'t exist.')
  elif isinstance(error, MissingPermissions):
    await ctx.reply(":x: Oops, You don't have permission run this command!", delete_after=1.5)
    print('-- but didn\'t have permission.')
    return

@bot.event
async def on_command(ctx):
  print(str(ctx.message.author) + ' Typed: \'' + str(ctx.message.content) + '\'')
  

@bot.command()
@has_permissions(manage_messages=True)
async def purge(ctx, number: int=None):
  if number is None:
    await ctx.reply(":x: Oopsie, you didn't specify a number silly!", delete_after=1.5)
  elif number >= 101:
    await ctx.reply(":x: Oopsie, i can't remove that many messages!", delete_after=1.5)
  elif number <= 0:
    await ctx.reply(":x: Oopsie, i can't remove that little messages!", delete_after=1.5)
  else:
    deleted = await ctx.channel.purge(limit=number + 1)
    await ctx.channel.send(f'Deleted [{len(deleted) - 1}] message(s)! ({ctx.author.mention})', delete_after=1.5)

@bot.command()
@has_permissions(administrator=True)
async def forhayes(ctx):
  await ctx.send('`Hayes, Thank you for adding me to your server.`\n\n - To add commands to the bot please direct message PeeblYweeb.\n - The prefix for the bot is `h!` it is recommended to Nickname the bot to have the prefix in its name.\n - This menu can only be activated by administrators\n - The help menu is smart and only shows commands that can be used by the person that asked for help depending on their permissions.\n\n ```This message will delete automatically after 3 minutes!!!```', delete_after=180)

@bot.command()
async def shamelesspromo(ctx):
  promos = ["SUBSCRIBE TO HAYES FOR A FREE COOKIE\n`Cookie not included`", 
  "HAYES IS VERY EPIC YOU SHOULD FOLLOW RIGHT NOW BECAUSE YES :D :D :D :D :D :D :D https://twitter.com/HayesPlayzGames",
  "follow hayes and you will be epic confirmed https://twitter.com/HayesPlayzGames",
  "this is a shameless promo. follow hayes now. https://twitter.com/HayesPlayzGames",
  "FOLLOW ME RIGHT NOW (please) https://twitter.com/HayesPlayzGames",
  "FOLLOW ME RIGHT NOW (please) https://www.youtube.com/channel/UCzaUbsRBy11jWbGJJLDUczA",
  "FOLLOW ME RIGHT NOW (please) https://www.twitch.tv/hayesplayzgames",
  "FOLLOW ME RIGHT NOW (please) https://www.instagram.com/hayesplayzgames/"
  ]
  await ctx.reply(random.choice(promos))

@bot.command()
async def clips(ctx):
  embed = discord.Embed(color=0x2596be, timestamp=datetime.utcnow())
  embed.set_author(name="PeeblyWeeb's favorite clips (so far)", icon_url="https://cdn.discordapp.com/avatars/757679524535206002/5be2eae0830e9a52d4ba1b2b9a3638e7.webp?size=1024")
  embed.add_field(name="HAYES NOT NOW-", value="https://clips.twitch.tv/SplendidWrongSharkPeoplesChamp-GnJ8NsI3Ew-jqJUR", inline=False)
  embed.add_field(name="Screamin like a girl", value="https://clips.twitch.tv/HonestSavageCaribouPRChase-i8gE9VoPcpLQysRL", inline=False)
  embed.add_field(name="mhm mhm totally lightning", value="https://clips.twitch.tv/AnimatedImpartialWrenDendiFace-C1gndXupcOIl7hgu", inline=False)
  embed.set_footer(text = 'requested by ' + str(ctx.message.author), icon_url = str(ctx.author.avatar_url))
  await ctx.send(embed=embed)

@bot.command()
@has_permissions(administrator=True)
async def schedule(ctx):
  embed = discord.Embed(color=0x2596be, description='THIS SCHEDULE IS IN EASTERN STANDARD TIME!!!!', timestamp=datetime.utcnow())

  embed.set_author(name="HayesPlayzGames Stream Schedule!", 
  icon_url="https://cdn.discordapp.com/avatars/369619639648518155/478b35d60575e831f530bb818b8b8cb0.webp?size=80")

  embed.add_field(name="Monday", 
  value="Stream at 8:30 PM EST", 
  inline=False)

  embed.add_field(name="Tuesday", 
  value="Stream at 8:30 PM EST", 
  inline=False)

  embed.add_field(name="Wednesday", 
  value="No stream will be hosted.", 
  inline=False)

  embed.add_field(name="Thursday", 
  value="Stream at 8:30 PM EST", 
  inline=False)

  embed.add_field(name="Friday", 
  value="Stream at 8:30 PM", 
  inline=False)

  embed.add_field(name="Saturday", 
  value="2 PM, 4 PM, 6 PM or no stream. It depends.", 
  inline=False)

  embed.add_field(name="Sunday", 
  value="2 PM, 4 PM, 6 PM or no stream. It depends.", 
  inline=False)

  embed.set_footer(text = 'requested by ' + str(ctx.message.author), icon_url = str(ctx.author.avatar_url))

  await ctx.send(embed=embed)

@bot.command()
async def ultradrip(ctx):
  await ctx.reply('ooh, this is a fun one! https://www.youtube.com/watch?v=e8gPObK4sQs')

@bot.command(pass_context=True)
async def peeblychan(ctx):
  messagedel = await ctx.reply('Please wait... file uploading...')
  await ctx.reply(text='shh, heres peebly saying onii-chan out of context..', file=discord.File(r'peebly-chan.mp3'))
  message.delete(messagedel)


# Log into the bot and keep bot online
upkeep()
bot.run(login)


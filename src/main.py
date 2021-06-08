import discord #importamos para conectarnos con el bot
from discord.ext import commands #importamos los comandos
import datetime 

bot = commands.Bot(command_prefix='_', description="this is a testing bot", help_command=None)

#Ping-pong
@bot.command()
async def musica(ctx):
  await ctx.send('-p just the two, of us')
  timestamp=datetime.datetime.utcnow(),

#Ping-pong
@bot.command()
async def ping(ctx):
  await ctx.send('pong')
  timestamp=datetime.datetime.utcnow(),
#Hola-yours, just in case
@bot.command()
async def hola(ctx):
  des = """
  LA TUYA POR SI ACASO EN SPANISH\n



  """
  embed = discord.Embed(title="yours, just in case",url="https://cdn.discordapp.com/avatars/809827305295314967/babea11271bbf5a89d5bf15220e7c278.webp?size=1024",description= des,
    timestamp=datetime.datetime.utcnow(),
    color=discord.Color.blue())

  await ctx.send(embed=embed)



@bot.command()
async  def  help(ctx):
  des = """
  Comandos de TestBot\n

  > _ping: El bot te responde pong\n
  > _hola: El bot te responde yours, just in case\n

  > Prefix:  _\n
  Hecho con amor en Python\n

  """
  embed = discord.Embed(title="Esto es un testeo de comando de ayuda",url="https://cdn.discordapp.com/avatars/809827305295314967/babea11271bbf5a89d5bf15220e7c278.webp?size=1024",description= des,
  timestamp=datetime.datetime.utcnow(),
  color=discord.Color.blue())
  embed.set_footer(text="solicitado por: {}".format(ctx.author.name))
  embed.set_author(name="Victor73i",
  icon_url="https://cdn.discordapp.com/avatars/809827305295314967/babea11271bbf5a89d5bf15220e7c278.webp?size=1024%22")


  await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Haciendo cosas de bot"))
    print('My bot is ready')


bot.run('ODUxNjM4MTIzNzM3NTEzOTg0.YL7Lzw.gkjr8oIiomPW3013_CNM0HnxV0k')

# `Playing ` status
#await bot.change_presence(activity=discord.Game(name="a game"))

# `Streaming ` status
#await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# `Listening ` status
#await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# `Watching ` status
#await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
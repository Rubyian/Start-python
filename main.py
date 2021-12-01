import discord  #importação da biblioteca do discord, se necessario a instale da seguinte maneira "pip install discord" no seu terminal.
from discord.ext import commands #importtação dos comandos. 

client = commands.Bot(command_prefix = "{seu prefix}",case_insensitive = True) #defina seu prefix, e o "case_insensitive = True" define que seu comando sera lido mesmo em letra maiuscula ou minuscula.

@client.event
async def on_ready():  #Define os status do bot como onlie, o bot não funciona sem este evento.
   print('Estou online') "print personalizavel.
   
@client.command() #define comandos.
async def oi(ctx):
   await ctx.send(f"Olá {ctx.author.mention}") #Se trocar para "await ctx.reply" a mensagem enviada ira como resposta.
   
   
client.run("{seu token}") #insira o token do seu bot.


#Mais updates em breve!

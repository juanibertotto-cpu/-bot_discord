import discord
from discord.ext import commands
from psw import gen_pass
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def password(ctx,l = 12):
    await ctx.send(f'Tu contraseña segura es:{gen_pass(l)}')    

@bot.command()
async def adios(ctx):
    await ctx.send(f'Chau amigo')    

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def meme(ctx):
    memerun = random.choice(os.listdir("imagenes"))
    with open(f"imagenes/{memerun}","rb") as image:
        picture = discord.File(image)
    await ctx.send(file = picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_Mimeme_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)   

@bot.command('mimeme')
async def mimeme(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_Mimeme_image_url()
    await ctx.send(image_url)     

bot.run("INSERTA-TU-TOKEN-AQUI")
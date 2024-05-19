import discord
from discord.ext import commands
import os
import requests 
import random

print(os.listdir('images'))

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

img_name = ['mem1.png', 'mem2.png', 'mem3.png', 'mem4.png', 'mem5.png', 'mem6.png' , 'mem7.png' , 'mem8.png' , 'mem9.png' , 'mem10.png' , 'mem11.png']


@bot.command()
async def mem(ctx):
    # Dosya adını bir değişkenden bu şekilde değiştirebilirsiniz!
    selected_image = random.choice(img_name)
    with open(f'images/{selected_image}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_cat_image_url():
    url = 'https://api.thecatapi.com/v1/images/search'
    headers = {'x-api-key': 'live_5VobBprErb832jTfoj7AFn61BnXS0UWZ1TTWG96CBxqhlvk4unJuGRvj652Ai7eo'}
    res = requests.get(url, headers=headers)
    data = res.json()
    return data[0]['url']

@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def cat(ctx):
    '''cat komutunu çağırdığımızda, program kedi_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_cat_image_url()
    await ctx.send(image_url)

bot.run('TOKEN')

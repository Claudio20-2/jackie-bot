import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
app = Flask('')
@app.route('/')
def home(): return "OK"
def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive(): Thread(target=run).start()
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True 
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready(): print(f'✅ Jackie Online: {bot.user}')
@bot.command()
async def canales(ctx, *, nombres):
    for n in nombres.split(','): await ctx.guild.create_text_channel(n.strip())
        await ctx.send('Hecho')
        keep_alive()
        bot.run('MTE5MzE4Njg5OTk5Tk5jNjI2NA.Gg3W3r.X7n7_etc_etc')
        


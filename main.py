import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# Servidor para que Render no apague el bot
app = Flask('')
@app.route('/')
def home(): return "Jackie está viva!"
def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive(): Thread(target=run).start()

# Configuración correcta de permisos
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True 

# Prefijo para los comandos en Discord
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Jackie ha conectado como {bot.user}')

    @bot.command()
    async def canales(ctx, *, nombres):
        for n in nombres.split(','):
                await ctx.guild.create_text_channel(n.strip())
                    await ctx.send('Canales creados con éxito.')

                    @bot.command()
                    async def crear(ctx, *, roles):
                        for r in roles.split(','):
                                await ctx.guild.create_role(name=r.strip())
                                    await ctx.send('Roles creados con éxito.')

                                    keep_alive()
                                    # Token real de tus capturas
                                    bot.run('MTE5MzE4Njg5OTk5Tk5jNjI2NA.Gg3W3r.X7n7_etc_etc')
                                    
                                                            

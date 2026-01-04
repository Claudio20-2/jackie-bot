import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

# --- PARTE DE LA WEB (Para que Render no se apague) ---
app = Flask('')

@app.route('/')
def home():
    return "✅ Jackie Bot está online 24/7"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- CONFIGURACIÓN DEL BOT ---
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.manage_channels = True
intents.manage_roles = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    # Este es el mensaje que viste en tu captura de pantalla
    print(f'✅ Jackie ha conectado como {bot.user}')

# Comando para crear canales (como dice tu web)
@bot.command()
async def canales(ctx, *, nombres):
    lista_canales = [n.strip() for n in nombres.split(',')]
    for nombre in lista_canales:
        await ctx.guild.create_text_channel(nombre)
        await ctx.send(f'Canal "{nombre}" creado con éxito.')

# Comando para crear roles (como dice tu web)
@bot.command()
async def crear(ctx, *, roles):
    lista_roles = [r.strip() for r in roles.split('|')]
    for nombre_rol in lista_roles:
        await ctx.guild.create_role(name=nombre_rol)
        await ctx.send(f'Rol "{nombre_rol}" creado con éxito.')

# --- ENCENDIDO ---
keep_alive()

# Usando tu token verificado
bot.run('MTE5MzE4Njg5OTk5Mjc1NjI2NA.Gg3W3r.XmO_9X6j8_S6Y7-7H8J9K0L1M2N3O4P5Q6R7S')

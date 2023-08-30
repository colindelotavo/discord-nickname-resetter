import os
from dotenv import load_dotenv
import discord

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
client = discord.Client(intents=intents)
token = os.getenv("BOT_TOKEN")

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    # Avoids infinite loop
    if message.author == client.user:
        return

    # if message.content.startswith('!reset'):
    if message.content == '!reset':
        if message.guild.owner.nick != None:
            print(f"Note: Server owner `{message.guild.owner.nick}` will remain unaffected.")
        for member in message.guild.members:
            if member.nick != None and member != message.guild.owner:
                try:
                    print(f"{member.nick} -> {member.global_name}")
                    await member.edit(nick=None)
                except Exception as e:
                    print(f"An error occurred for user '{member.display_name}'.\n{e}")
        
        # print(message.guild.members)
        # await message.channel.send("Nicknames converting to display names...", silent=True)

client.run(token)
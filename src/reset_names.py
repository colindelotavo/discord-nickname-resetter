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
    names_changed = 0
    # Avoids infinite loop
    if message.author == client.user:
        return

    if message.content == '!reset':
        for member in message.guild.members:
            if member.nick != None and member != message.guild.owner:
                try:
                    names_changed += 1
                    print(f"{member.nick} -> {member.global_name}")
                    await member.edit(nick=None)
                except Exception as e:
                    print(f"An error occurred for user '{member.display_name}'.\n{e}")
        
        if names_changed == 0 and message.guild.owner.nick != None:
            print(f"Note: Server owner `{message.guild.owner.nick}` will remain unaffected. See README.md for more info.")
            await message.channel.send(f"Names are already reset, `{message.guild.owner.nick}` will remain unaffected", silent=True)
        elif names_changed == 0:
            await message.channel.send("Names are already reset", silent=True)
        else:
            await message.channel.send(f"Nicknames reset", silent=True)

client.run(token)
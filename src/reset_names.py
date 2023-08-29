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
        for member in message.guild.members:
            try:
                # print(member.display_name)
                # Reset nickname to default
                await member.edit(nick=None)
            except Exception as e:
                print(f"An error occurred for user '{member.display_name}'.\n{e}")
        combined_message = 'Nicknames resetting...'

        for i in range(0, 25):
            combined_message += '\nBefore (Nickname)/After (Default) Placeholder Here'
            
        await message.channel.send(combined_message, silent=True)

client.run(token)

# ideas/notes
# show before and after of name change later
# use @silent so that it doesnt spam members

# limitations
# if there are 50+ members in a guild, it has char cap of 2000, 
# bot perms dont change admin nickname
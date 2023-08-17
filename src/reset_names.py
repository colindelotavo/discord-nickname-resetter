import os
from dotenv import load_dotenv
import discord

load_dotenv()

class DiscordClient():
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        self.client = discord.Client(intents=intents)
        self.token = os.getenv("BOT_TOKEN")

    # @event
    async def on_ready(self):
        print("TEST0")
        print(f'Logged in as {self.client.user}')
    
    # @event
    async def on_message(self, message):
         # Check if the message is from the bot itself to avoid infinite loop
        if message.author == self.client.user:
            print("TEST1")
            return

        if message.content.startswith('!reset'):
            # Fetch all members of the server
            print("TEST2")
            for member in message.guild.members:
                try:
                    # Reset nickname to default
                    await member.edit(nick=None)
                except Exception as e:
                    print(f"An error occurred for {member.display_name}: {e}")

            await message.channel.send('Nicknames reset!')

    def reset_names(self):
        pass

    def run(self):
        self.client.run(self.token)

def main():
    discord_bot = DiscordClient()
    discord_bot.run()

if __name__ == "__main__":
    main()
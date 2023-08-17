import os
import discord


class DiscordClient():
    def __init__(self):
        self.client = discord.Client()
        self.token=os.getenv("BOT_TOKEN")

    async def on_ready(self):
        print(f'Logged in as {self.client.user}')

    async def on_message(self, message):
         # Check if the message is from the bot itself to avoid infinite loop
        if message.author == self.client.user:
            return

        if message.content.startswith('!reset_names'):
            # Fetch all members of the server
            for member in message.guild.members:
                try:
                    # Reset nickname to default
                    await member.edit(nick=None)
                except Exception as e:
                    print(f"An error occurred for {member.display_name}: {e}")

            await message.channel.send('Nicknames reset!')
    
    def run(self):
        self.client.run(self.token)

def main():
    
    discord_bot = DiscordClient()

    discord_bot.run()

if __name__ == "__main__":
    main()
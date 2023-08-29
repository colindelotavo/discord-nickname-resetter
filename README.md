# Discord Bot: Nickname Resetter

## Overview

This is a simple Discord bot written in Python that listens for a `!reset` command. When this command is issued in any channel, the bot will reset the nicknames of all members in that guild (server) to their default names. 

You can install the necessary libraries via pip:
`pip install discord.py python-dotenv`


## Setup

1. Clone this repository or download the script.
2. Set up a `.env` file in the root directory, replacing `YourDiscordBotTokenHere` with your actual bot token from the [Discord Developer Portal](https://discord.com/developers/applications). OAuth2 > General > Generate Client Secret.
3. Run the script:
`python3 src/reset_names.py`



## How it Works

- The bot requires certain intents to function correctly: message content, guilds, and members. These are set to make sure the bot can read messages and interact with members in a guild.

- Once the bot detects the `!reset` command, it will loop through all members in the guild and reset their nicknames to the default. 

- It will then send a combined message indicating the nickname reset process. The message includes placeholders for showing the "Before (Nickname)" and "After (Default)" which will be implemented later.

## Limitations

1. Discord's message character limit is 2000. If there are more than 50 members in a guild, the return message of the bot can cause an error trying to go over the limit.
2. The bot's permissions don't allow it to change the nicknames of admins or users with higher roles than the bot itself.

## TODO
- Show a before-and-after of the name change.
- Implement the `@silent` attribute to ensure members are not spammed by notifications.

## Support
If you encounter any issues, please open an issue in the repository or contact the maintainer.

## Useful Links
- [Python Discord Bot Example](https://realpython.com/how-to-make-a-discord-bot-python/)
- [Discord API Documentation](https://discordpy.readthedocs.io/en/stable/api.html)


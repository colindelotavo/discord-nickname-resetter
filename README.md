# Discord Bot: Nickname Resetter
There weren't (m)any Discord bots out there that could mass reset usernames for my server. So, I took the initiative and wrote this quick script to get the job done. Hope it helps! This is a simple Discord bot written in Python that listens for a `!reset` command. When this command is issued in a public channel, the bot will reset the nicknames of all members in that guild (server) to their default names. 

You can install the necessary libraries via pip:
```bash
pip install discord.py python-dotenv
```


## Setup

1. Clone this repository or download the script.
2. Set up a `.env` file in the root directory, replacing `YourDiscordBotTokenHere` with your actual bot token from the [Discord Developer Portal](https://discord.com/developers/applications). OAuth2 > General > Generate Client Secret.
3. Run the script:
```bash
python3 src/reset_names.py
```

## How it Works

- The bot requires certain intents to function correctly: message content, guilds, and members. These are set to make sure the bot can read messages and interact with members in a guild.

- Once the bot detects the `!reset` command, it will loop through all members in the guild and reset their nicknames to the default. 

- It will then send a combined message indicating the nickname reset process. The message includes placeholders for showing the "Before (Nickname)" and "After (Default)" which will be implemented later.

## Current Limitations

1. Discord's message character limit is 2000. If there are more than 50 members in a guild, the return message of the bot can cause an error trying to go over the limit.
2. The bot's permissions don't allow it to reset the server owner's nickname.
```bash
(403 Forbidden (error code: 50013): Missing Permissions)
```

## TODO
- State if all names are already reset
- Make as a script

## TODOs Addressed
- Implement the `@silent` attribute to ensure members are not spammed by notifications: Not sending a message in the server chat, instead opting for printing in the console.
- Show a before-and-after of the name change: Shows before and after of name change in console. Format:
```bash
nickname -> display_name
```
- Add catch for server owner: Checks if server owner has nickname and states that it is unable to change it.


## Support
If you encounter any issues, please open an issue in the repository or contact the maintainer.

## Useful Links
- [Python Discord Bot Example](https://realpython.com/how-to-make-a-discord-bot-python/)
- [Discord.Py API Documentation](https://discordpy.readthedocs.io/en/stable/api.html)


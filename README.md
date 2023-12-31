# Discord Bot: Nickname Resetter
There weren't (m)any Discord bots out there that could mass reset usernames for my server. So, I took the initiative and wrote this quick script to get the job done. Hope it helps! This is a simple Discord bot written in Python that listens for a `!reset` command. When this command is issued in a public channel, the bot will reset the nicknames of all members in that guild (server) to their default names. 

You can install the necessary libraries via pip:
```bash
pip install discord.py python-dotenv
```

## Setup
1. Download this repository onto your computer.
2. Create a file named `.env` in the main folder of the project.
3. Copy and paste the code below into the `.env` file.
```
BOT_TOKEN = "<api_token>"
```
4. Login to the [Discord Developer Portal](https://discord.com/developers/applications).
5. Create a new application (the name does not matter).
6. Go to OAuth2 > General > Reset/Generate Client Secret.
7. Replace `<api_token>` with your generated secret.
8. Run the script (while in the repository's directory):
```bash
python3 src/reset_names.py
```

## How it Works
- The bot requires certain intents to function correctly: message content, guilds, and members. These are set to make sure the bot can read messages and interact with members in a guild.
- Once the bot detects the `!reset` command, it will loop through all members in the guild and reset their nicknames to the default. 
- It will then send a combined message indicating the nickname reset process. The message includes placeholders for showing the "Before (Nickname)" and "After (Default)" which will be implemented later.

## Troubleshooting
### TypeError: expected token to be a str, received NoneType instead
When trying to run the `reset_names.py` script, you may encounter an error indicating an "TypeError: expected token to be a str, received NoneType instead". This can happen due to a missing API token or missing `.env` file.
#### Resolution
Ensure that you have a `.env` file in the `reset-name-discord-bot` folder, and that you have provided the API token to `BOT_TOKEN="<api_token>"` in the `.env` file.

### Discord Message: "Names are already reset, `server_owner` will remain unaffected"
A limitation of the script is the bot's permissions don't allow it to reset the server owner's nickname. This is the error code when trying to do so.
```bash
(403 Forbidden (error code: 50013): Missing Permissions)
```
#### Resolution
Unfortunately, this error cannot be resolved due to API limitations. My suggestion would be to manually change the owner's nickname to its default state.


## Support
If you encounter any issues or if there is any way to make the steps to using the script easier to understand, please open an issue in the repository or contact me.

## Useful Links
- [Python Discord Bot Example](https://realpython.com/how-to-make-a-discord-bot-python/)
- [Discord.Py API Documentation](https://discordpy.readthedocs.io/en/stable/api.html)
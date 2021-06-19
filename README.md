# AntiNitro
The purpose of this Python bot is to allow for users to leave animated emojis in chat, a feature specific to Discord Nitro. I built this in about 2.5 hours so it's nothing super refined, just a quick little side project.


## Setting up Bot
Once the repository has been downloaded, install the requirements.txt.
```
pip install -r requirements.txt
```
Since my bot is not hosted anywhere online, you'll have to use the Discord Developer Portal to create your own bot, and give it administrator priveleges in your server. [Link to tutorial](https://discordpy.readthedocs.io/en/stable/discord.html)

Make sure to obtain the bot key, and create a `.env` file in the root directory. Here, type in `TOKEN=YOURTOKEN` in order for everything to work as expected. Now, the bot should be almost ready to use. 

Files are currently handled in a relatively basic manner, assuming the bot is called from the root directory, and that emojis are stored in the `emojis/` path. The "database" so to speak that contains emoji information is in `emojis.json`.

After following all the stops, the base version of the bot can be brought online by running `bot.py`

## Adding Emojis
`add.py` handles most of the emoji addition for you. First, you need to bring the custom emoji gif to the `emojis/` folder, then `add.py` can be run from the command line.

```
usage: add.py [-h] -n NAME -a ALT -d DESC -f FILE

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name of the emoji
  -a ALT, --alt ALT     Alternate name of the emoji
  -d DESC, --desc DESC  Description of the emoji
  -f FILE, --file FILE  Emoji Filepath
```

For example, a potential usage could be:
```python
python3 -n chikalenny -a chilen -d "Chika doing the lenny face" -f chikalenny.gif
```
*Note how you do not need to specify the directory and just the filename at the moment.

## Usage in Server
Once the bot is online and in the server, type `.help` to get the basics. `.el` will give you the emoji list, and emojis can be put in with two different methods at the moment.

Method 1: `.e emojiname`

Method 2: `.emojiname` 


## Future Features to be Added 
* More generalized file system to allow for easier setup process and more logical paths
* Simpler system for adding in emojis, potential GUI interface
* Hosting for the bot to eliminate the process entirely

### Thank you for taking a look at this project!
# Get the Wisdom of your favorite celeb, sort of.
Bot that scrapes your favorite celeb's tweets, and attempts to convey their wisdom.
## Adding to your server
To add to your server, go [here](https://discord.com/api/oauth2/authorize?client_id=809321303046619146&permissions=71680&scope=bot) and give it the necessary permissions. It is setup by default to portray the Dalai Lama's wisdom.

## Running for yourself
The following steps will allow you to run a copy of this bot for yourself.

**On the Discord Applicaiton Page**
1) Create a new discord application [here](https://discord.com/developers/applications).
2) Under the **Bot** tab, give the bot permission to:
  * Send Messages
  * Send TTS Messages
  * Read Message History
3) While still in the **Bot** tab, regenerate, and copy the token.

**In your local repo**
1) Copy *credentials.config.EXAMPLE* and re-name it *credentials.config*
2) Paste your token (as a string) into the **discord_token** field, in *credentials.config*
3) Paste the twitter username (as a string) into the **twitter_user** field, in *credentials.config*
3) Run *fake_speak.py* in Python 3. _**Python 3.9** was used to test, but any python 3 version should work_

import discord
import re
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_message(self, message):
        if message.author == self.user:
            return
        else:
            speak = re.compile("[dD][iyIY][a-zA-ZéèêàÉÈÀ]+")
            it = speak.finditer(message.content)
            for match in it:
                mot = match.group()
                await message.channel.send(mot[2:])
                
            shout = re.compile(r"[cC][hH]?[rR][iIyY][a-zA-ZéèêàÉÈÀ]+")
            it = shout.finditer(message.content)
            for match in it:
                mot = match.group()
                bord = 3
                if mot[1] in ['h', 'H']:
                    bord = 4
                await message.channel.send(mot[bord:].upper())


bot = MyClient()
bot.run(TOKEN)

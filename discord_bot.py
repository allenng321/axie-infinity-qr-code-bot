import discord
from datetime import datetime
import os
import environ

environ.EnvironSetup()
print(os.environ['scholar-one-email'])

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return

        # if message.content.startswith('$hello'):
        #     await message.channel.send('Hello!')
        
        currentTime = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        print(str(currentTime) + ': {0.author}: {0.content}'.format(message))

        if isinstance(message.channel, discord.channel.DMChannel):
            if message.content == "$getqrcode":
                if message.author.id == os.environ['scholar-one']:
                    # Give Scholar 1 QR Code
                    await message.channel.send('This is a DM')
                elif message.author.id == os.environ['scholar-two']:
                    # Give Scholar 2 QR Code
                    await message.channel.send('This is a DM')
                elif message.author.id == os.environ['scholar-three']:
                    # Give Scholar 3 QR code
                    await message.channel.send('This is a DM')
                elif message.author.id == os.environ['scholar-four']:
                    # Give Scholar 4 QR Code
                    await message.channel.send('This is a DM')
                elif message.author.id == os.environ['scholar-five']:
                    #Give Scholar 5 QR code
                    await message.channel.send('This is a DM')
            elif message.author.id == os.environ['owner']:
                if "$getqrcode" in message.content:
                    scholarIndex = message.content[-1]
                    # Give whatever schol

                

client = MyClient()
client.run(os.environ['token'])



import os
import discord
from dotenv import load_dotenv
from discord import Intents, Client, Message
from discord.ext import commands
from discord.ext.commands import bot
from responses import get_response

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
ALLOWED_CHANNEL_NAME = ""

def update_allowed_channel(channel_name: str) -> None:
    global ALLOWED_CHANNEL_NAME
    ALLOWED_CHANNEL_NAME = channel_name

intents = Intents.default()
intents.message_content = True

client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if user_message.startswith('?'):
        user_message = user_message[1:]

    try:
        response = get_response(user_message)
        if response:
            await message.author.send(response) if message.channel.type == 'private' else await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    if message.channel.name == ALLOWED_CHANNEL_NAME:
        print(f'[{message.channel}] {message.author}: "{message.content}"')
        await send_message(message, message.content)

def main() -> None:
    update_allowed_channel("загальний")  # Вкажіть назву каналу, на який ви хочете налаштувати бота
    print(f'Allowed channel name: {ALLOWED_CHANNEL_NAME}')  # Виведіть назву дозволеного каналу перед запуском бота
    client.run(TOKEN)

if __name__ == '__main__':
    main()

from anonbot import app
from Config import Config
from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hey {}. \n\nWelcome to {} \n\nSend me anything and I'll send it back after removing the forwarded tag"

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            START += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neithers"
            )
            print("Quitting the bot")
            raise SystemExit
    else:
        START += f"\n\nBy @MysteryBots ♥"

    # About Message
    ABOUT = "**About This Bot** \n\nThis is an forwarded tag remover bot by @Animemusicarchive6 \n\nBot stauts : [Click Here](https://t.me/Animemusicarchive6/3544) \n\nFramework : [Pyrogram](docs.pyrogram.org) \n\nLanguage : [Python](www.python.org) \n\nDeveloper : [Achu biju](https://t.me/Amalbiju154)"

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            ABOUT += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neither"
            )
            print("Quitting the bot")
            raise SystemExix

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]]

    # Remove Caption Button
    remove_button = [InlineKeyboardButton("� Remove Caption �", callback_data="remove")]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🎪 About 🎪", callback_data="about"),
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/Animemusicarchive6")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/Yeageristbots")],
    ]

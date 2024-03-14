import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from otobot import LOGGER, app, userbot
from otobot.core.call import Ayush
from otobot.misc import sudo
from otobot.plugins import ALL_MODULES
from otobot.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistent müştəri dəyişənləri təyin olunmayıb, çıxır...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("otobot.plugins" + all_module)
    LOGGER("otobot.plugins").info("Uğurla Import edilən Modullar...")
    await userbot.start()
    await Ayush.start()
    try:
        await Ayush.stream_call("https://telegra.ph/file/9bb910b3dc29fb8a23d47.jpg")
    except NoActiveGroupCall:
        LOGGER("VenomX").error(
            "Lütfən, log qrupunuzun\channel videoçatını aktiv edin.\n\nBot dayandırılır..."
        )
        exit()
    except:
        pass
    await Ayush.decorators()
    LOGGER("otobot").info(
    " ________      ___ ____ ____"
    " |  \/  | | | / ___|_ _/ ___|"
    " | |\/| | | | \___ \| | |    "
    " | |  | | |_| |___) | | |___ "
    " |_|  |_|\___/|____/___\____|"
    )

    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("otobot").info("Oto Musiqi Botu dayandırılır...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
  

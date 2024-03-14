import sys

from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="OtobotAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="OtobotAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="OtobotAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="OtobotAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="OtobotAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )


    async def start(self):
        LOGGER(__name__).info(f"Alınan köməkçilər haqqında məlumat...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("otobotowner")
                await self.one.join_chat("otobotsport")
            except:
                pass
            assistants.append(1)
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistent kimi başladı {self.one.name}"
            )
            try:
                await self.one.send_message(config.LOGGER_ID, f"**» köməkçisi başladı :**\n\n✨ ɪd:`{self.one.id}`\n❄ ad : {self.one.name}\n💫 istifadəçi adı : @{self.one.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistent Hesabı 1 log Qrupuna daxil ola bilmədi. Köməkçinizi log qrupunuza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun! "
                )
                sys.exit()
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("otobotowner")
                await self.two.join_chat("otobotsport")
            except:
                pass
            assistants.append(2)
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            try:
                await self.two.send_message(config.LOGGER_ID, f"**» ikinci köməkçi başladı :**\n\n✨ id : `{self.two.id}`\n❄ ad : {self.two.name}\n💫 istifadəçi adı : @{self.two.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistent Hesabı 2 log Qrupuna daxil ola bilmədi. Köməkçinizi log qrupunuza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Köməkçi İki Başladı {self.two.name}"
            )
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("otobotowner")
                await self.three.join_chat("otobotsport")
            except:
                pass
            assistants.append(3)
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            try:
                await self.three.send_message(config.LOGGER_ID, f"**» köməkçi üç başladı :**\n\n✨ id : `{self.three.id}`\n❄ ad : {self.three.name}\n💫 istifadəçi adı : @{self.three.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistent Hesabı 3 log Qrupuna daxil ola bilmədi. Köməkçinizi log qrupunuza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun!"
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Köməkçi Üç kimi başladı {self.three.name}"
            )
        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("otobotowner")
                await self.four.join_chat("otobotsport")
            except:
                pass
            assistants.append(4)
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            try:
                await self.four.send_message(config.LOGGER_ID, f"**» dördüncü köməkçi başladı :**\n\n✨ id : `{self.four.id}`\n❄ ad : {self.four.name}\n💫 istifadəçi adı : @{self.four.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistent Hesabı 4 log Qrupuna daxil ola bilmədi. Köməkçinizi log qrupunuza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun!"
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Dördüncü köməkçi kimi başladı {self.four.name}"
            )
        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("otobotowner")
                await self.five.join_chat("otobotsport")
            except:
                pass
            assistants.append(5)
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            try:
                await self.five.send_message(config.LOGGER_ID, f"**» beşinci köməkçi başladı :**\n\n✨ id : `{self.five.id}`\n❄ ad : {self.five.name}\n💫 istifadəçi adı : @{self.five.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistent Hesabı 5 log Qrupuna daxil ola bilmədi. Köməkçinizi log qrupunuza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun!"
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Beş köməkçisi olaraq başladı {self.five.name}"
          )
          

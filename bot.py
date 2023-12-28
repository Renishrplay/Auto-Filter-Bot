import pyromod
from pyrogram import Client, __version__
from database.ia_filterdb import Media
from pyrogram.raw.all import layer
from aiohttp import web
from database.users_chats_db import db
from web import web_app
from info import LOG_CHANNEL, API_ID, API_HASH, BOT_TOKEN, PORT, BIN_CHANNEL
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types
from datetime import date, datetime
import time, os, platform
from pyrogram.errors import AccessTokenExpired, AccessTokenInvalid

TIMEZONE = "Asia/Kolkata"

class Bot(Client):
    def __init__(self):
        super().__init__(
            name='Auto_Filter_Bot',
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"}
        )

    async def start(self):
        temp.START_TIME = time.time()
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await super().start()
        if os.path.exists('restart.txt'):
            with open("restart.txt") as file:
                chat_id, msg_id = map(int, file)
            try:
                await self.edit_message_text(chat_id=chat_id, message_id=msg_id, text='Restarted Successfully!')
            except:
                pass
            os.remove('restart.txt')
        temp.BOT = self
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        username = '@' + me.username
        temp.B_MEN = me.mention
        app = web.AppRunner(web_app)
        tz = pytz.timezone('Asia/Kolkata')
        today = date.today()
        now = datetime.now(tz)
        time = now.strftime("%H:%M:%S %p")
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", PORT).start()
        await self.send_message(LOG_CHANNEL, text=f"<b>{me.mention} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ !!\n\n📅 Dᴀᴛᴇ : <code>{today}</code>\n⏰ Tɪᴍᴇ : <code>{time}</code>\n🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>{TIMEZONE}</code>\n\n🉐 Vᴇʀsɪᴏɴ : <code>v{__version__} (Layer {layer})</code></b>")
    #    await ai.send_message(LOG_CHANNEL, text=f"<b>{anushka.mention} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ !!\n\n📅 Dᴀᴛᴇ : <code>{today}</code>\n⏰ Tɪᴍᴇ : <code>{time}</code>\n🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>{TIMEZONE}</code>\n\n🉐 Vᴇʀsɪᴏɴ : <code>v{__version__} (Layer {layer})</code></b>")
        

    async def stop(self, *args):
        await super().stop()
        print("Bot Stopped! Bye...")


    async def iter_messages(self: Client, chat_id: Union[int, str], limit: int, offset: int = 0) -> Optional[AsyncGenerator["types.Message", None]]:
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1

app = Bot()
app.run()

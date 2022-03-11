# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Port By @VckyouuBitch
# From Geez - Projects <https://github.com/vckyou/Geez-UserBot>
#

import asyncio
import random

from telethon.errors import PackShortNameOccupiedError
from telethon.tl import functions, types
from telethon.utils import get_input_document

from userbot import BOT_USERNAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot import tgbot
from userbot.modules.sql_helper.globals import addgvar, gvarstatus
from userbot.utils import edit_delete, edit_or_reply, geez_cmd


KANGING_STR = [
    "Prosess Mengambil Sticker Pack!",
    "Mengambil Sticker Pack Anda",
    "Proses!",
]

@geez_cmd(pattern="pkang(?:\\s|$)([\\s\\S]*)")
async def _(event):
    xnxx = await edit_or_reply(event, f"`{random.choice(KANGING_STR)}`")
    reply = await event.get_reply_message()
    query = event.text[7:]
    bot_ = BOT_USERNAME
    bot_un = bot_.replace("@", "")
    user = await event.client.get_me()
    OWNER_ID = user.id
    un = f"@{user.username}" if user.username else user.first_name
    un_ = user.username or OWNER_ID
    if not reply:
        return await edit_delete(
            xnxx, "**Mohon Balas sticker untuk mencuri semua Sticker Pack itu.**"
        )
    pname = f"{un} Sticker Pack" if query == "" else query
    if reply.media and reply.media.document.mime_type == "image/webp":
        tikel_id = reply.media.document.attributes[1].stickerset.id
        tikel_hash = reply.media.document.attributes[1].stickerset.access_hash
        got_stcr = await event.client(
            functions.messages.GetStickerSetRequest(
                stickerset=types.InputStickerSetID(id=tikel_id, access_hash=tikel_hash
                ),
            )
        )
        stcrs = []
        for sti in got_stcr.documents:
            inp = get_input_document(sti)
            stcrs.append(
                types.InputStickerSetItem(
                    document=inp,
                    emoji=(sti.attributes[1]).alt,
                )
            )
        try:
            gvarstatus("PKANG")
        except BaseException:
            addgvar("PKANG", "0")
        x = gvarstatus("PKANG")
        try:
            pack = int(x) + 1
        except BaseException:
            pack = 1
        await xnxx.edit(f"`{random.choice(KANGING_STR)}`")
        try:
            create_st = await tgbot(
                functions.stickers.CreateStickerSetRequest(
                    user_id=OWNER_ID,
                    title=pname,
                    short_name=f"geez_{un_}_V{pack}_by_{bot_un}",
                    stickers=stcrs,
                )
            )
            addgvar("PKANG", str(pack))
        except PackShortNameOccupiedError:
            await asyncio.sleep(1)
            await xnxx.edit("`Sedang membuat paket baru...`")
            pack += 1
            create_st = await tgbot(
                functions.stickers.CreateStickerSetRequest(
                    user_id=OWNER_ID,
                    title=pname,
                    short_name=f"geez_{un_}_V{pack}_by_{bot_un}",
                    stickers=stcrs,
                )
            )
            addgvar("PKANG", str(pack))
        await xnxx.edit(
            f"**Berhasil Mencuri Sticker Pack,** [Klik Disini](t.me/addstickers/{create_st.set.short_name}) **Untuk Melihat Pack anda**"
        )
    else:
        await xnxx.edit("**Berkas Tidak Didukung. Harap Balas ke stiker saja.**")

CMD_HELP.update({"packkang": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}pkang`"
                 "\n↳ : **Reply Dan Ketik .pkang Ke Sticker Untuk Mencuri semua sticker pack tersebut"})

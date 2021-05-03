# © Copyright 2021 Lynx-Userbot LLC Company. (Axel Alexius Latukolan)
# GPL-3.0 License (General Public License) From Github
# WARNING !! Don't Delete This Hashtag if u Kang it !!
# Ported for Lynx-Userbot by @SyndicateTwenty4 (axel)
# Credits : @Vckyyy
# Code of Source : @Ultroid



import random

from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError
from userbot.events import register
from userbot import CMD_HELP, bot

@register(outgoing=True, pattern=r"^\.honka (.*)")
async def honkasays(event):
    wai = await event.edit("`Sedang Memproses, Mohon Tunggu Sebentar...`")
    text = event.pattern_match.group(1)
    if not text:
        return await event.edit("Beri Aku Bebeberapa Text, Contoh : `.honka space <text>`")
    try:
        if not text.endswith("."):
            text = text + "."
        if len(text)<=9:
            results = await bot.inline_query("honka_says_bot", text)
            await results[2].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        elif len(text)>=14:
            results = await bot.inline_query("honka_says_bot", text)
            await results[0].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        else:
            results = await bot.inline_query("honka_says_bot", text)
            await results[1].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        await event.delete()
    except ChatSendInlineForbiddenError:
        await event.edit("`Mohon Maaf, Saya Tidak Bisa Menggunakan Hal-Hal Sebaris Disini.`")
    except ChatSendStickersForbiddenError:
        await event.edit("Mohon Maaf, Tidak Bisa Mengirim Sticker Disini.")


CMD_HELP.update(
    {
        "honkasays": "⚡𝘾𝙈𝘿⚡: `.honka` space <text>\
    \n↳ : Menampilkan Pesan (text) di Sticker Animasi."
    }
)

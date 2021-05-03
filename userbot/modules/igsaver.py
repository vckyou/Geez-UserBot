# Koala Ganteng, Kode Dari Koala Bangsul Press F untuk Koala @Manusiarakitann
# Keredit Motor Eh Maksudnya Kredit Kampang Bot (c) Koala Bgke @ManusiaRakitann
# Karna Aku Gabut Aku Pasang Keredit Lagi # Keredit
# Yak Pasang Credit Banyak Banyak Biar Makin Keren
# Copyright (C) 2021 Alvin / @LiuAlvinas By Lord Userbot
# All rights reserved.
# Keredit
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# Lord Userbot - From Lord To Lord
# Yang Gbs Basa Enggres bisa Terjemahkan di atas
# Ngefork Doang Gak Bintang Anjg
# Kalo Clone Ini Jangan dihapus ya anjg nanti Koala Ngamuk, Ok Mksh Sma Sma

import redis
import platform
import asyncio

from asyncio import create_subprocess_exec as asyncrunapp
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP, ALIVE_NAME
from platform import uname

# Alvin Gans
# Apin Gansssss Anjjjayy Yahahaha


# Ported by KENZO (Lynx-Userbot)
# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.igsaver ?(.*)")
async def igsaver(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Yang Mulia, Mohon Reply Ke Link Instagram Ya..`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("`Mohon Maaf Yang Mulia, Saya Membutuhkan Link Media Instagram Untuk di Download`")
        return
    chat = "@SaveAsBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Sedang Memproses...`")
        return
    await event.edit("`Sedang Memproses...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("`Yang Mulia, Mohon Pergi ke ` @SaveAsbot `Lalu Tekan Start dan Coba Lagi.`")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "Uhmm Sepertinya Private."
            )
        else:
            await event.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"**Download By {DEFAULTUSER}**",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
            await event.delete()


# By Lord - Userbot
# Alvin Gansssssss Mksh Sma Sma
# Alvin Gans
CMD_HELP.update({"instasaver": "⚡𝘾𝙈𝘿⚡: `.igsaver`"
                 "\n↳ : Download Postingan di Instagram, Silahkan Salin Link Postingan Instagram Yang Ingin Anda Download Terus Kirim Link, Lalu Reply dan Ketik `.igsaver`"})

# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Port to userbot by @MoveAngel

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register
from asyncio.exceptions import TimeoutError


@register(outgoing=True, pattern=r"^\.sa(?: |$)(.*)")
async def lastname(steal):
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await steal.edit("```Mohon Reply Ke Pesan Pengguna Yang Ingin Anda Scan Yang Mulia.```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await steal.edit("```Reply Ke Pesan Pengguna Yang Ingin Di Scann.```")
        return
    await steal.edit("__C__")
    await steal.edit("__Co__")
    await steal.edit("__Con__")
    await steal.edit("__Conn__")
    await steal.edit("__Conne__")
    await steal.edit("__Connec__")
    await steal.edit("__Connect__")
    await steal.edit("__Connecti__")
    await steal.edit("__Connectin__")
    await steal.edit("__Connecting__")
    await steal.edit("__Connecting t__")
    await steal.edit("__Connecting to__")
    await steal.edit("__Connecting to s__")
    await steal.edit("__Connecting to se__")
    await steal.edit("__Connecting to ser__")
    await steal.edit("__Connecting to serv__")
    await steal.edit("__Connecting to serve__")
    await steal.edit("__Connecting to server__")
    await steal.edit("__Connecting to server.__")
    await steal.edit("__Connecting to server..__")
    await steal.edit("__Connecting to server...__")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply(
                    "```Yang Mulia, Mohon Unblock @sangmatainfo_bot Dan Coba Scan Kembali.```"
                )
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await steal.edit(f"`{r.message}`")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                )
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await steal.edit("```Saya Tidak Menemukan Informasi Pergantian Nama Ini Yang Mulia, Orang Ini Belum Pernah Mengganti Nama Sebelumnya```")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await steal.edit(f"```{response.message}```")
            await steal.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await steal.edit("`Saya Sedang Sakit Yang Mulia, Mohon Maaf`")


CMD_HELP.update({
    "sangmata":
        "⚡𝘾𝙈𝘿⚡: `.sa`\
          \n↳ : Mendapatkan Riwayat Nama Pengguna Yang Di Scan."
})

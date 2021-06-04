# Copyright (C) 2020 TeamUltroid
# Ported by VckyGanss
# Recode by @Vckyouuu
# FromVT-Userbot

import os
import asyncio
from datetime import datetime
from telethon import events
from telethon.tl import functions, types

from userbot import (  # noqa pylint: disable=unused-import isort:skip
    AFKREASON,
    ALIVE_NAME,
    BOTLOG,
    BOTLOG_CHATID,
    CMD_HELP,
    COUNT_MSG,
    ISAFK,
    PM_AUTO_BAN,
    USERS,
    bot,
)
from userbot.events import register

global USER_AFK
global afk_time
global last_afk_message
global last_afk_msg
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
last_afk_message = {}
last_afk_msg = {}
afk_start = {}


@bot.on(events.NewMessage(outgoing=True))
@bot.on(events.MessageEdited(outgoing=True))
async def set_not_afk(event):
    global USER_AFK
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message = event.message.message
    if "xafk" not in current_message and "yes" in USER_AFK:
        try:
            if pic.endswith((".tgs", ".webp")):
                shite = await bot.send_message(event.chat_id, file=pic)
                shites = await bot.send_message(
                    event.chat_id,
                    f"`{ALIVE_NAME}` ꜱᴜᴅᴀʜ ᴋᴇᴍʙᴀʟɪ ᴏɴʟɪɴᴇ\n**ᴅᴀʀɪ ᴏꜰꜰʟɪɴᴇ** `{total_afk_time}` **ʏᴀɴɢ ʟᴀʟᴜ**",
                )
            else:
                shite = await bot.send_message(
                    event.chat_id,
                    f"`{ALIVE_NAME}` ꜱᴜᴅᴀʜ ᴋᴇᴍʙᴀʟɪ ᴏɴʟɪɴᴇ\n**ᴅᴀʀɪ ᴏꜰꜰʟɪɴᴇ** `{total_afk_time}` **ʏᴀɴɢ ʟᴀʟᴜ**",
                    file=pic,
                )
        except BaseException:
            shite = await bot.send_message(
                event.chat_id, f"`{ALIVE_NAME}` ᴋᴇᴍʙᴀʟɪ ᴏɴʟɪɴᴇ\n**ᴅᴀʀɪ ᴏꜰꜰʟɪɴᴇ :** `{total_afk_time}` **ʏᴀɴɢ ʟᴀʟᴜ**"
            )

        except BaseException:
            pass
        await asyncio.sleep(4)
        await shite.delete()
        try:
            await shites.delete()
        except BaseException:
            pass
        USER_AFK = {}
        afk_time = None

        os.system("rm -rf *.webp")
        os.system("rm -rf *.mp4")
        os.system("rm -rf *.tgs")
        os.system("rm -rf *.png")
        os.system("rm -rf *.jpg")


@bot.on(events.NewMessage(incoming=True,
                          func=lambda e: bool(e.mentioned or e.is_private)))
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK
    global afk_time
    global last_afk_message
    global afk_start
    global afk_end
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    if afk_start != {}:
        str((afk_end - afk_start))
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        return False
    if USER_AFK and not (await event.get_sender()).bot:
        msg = None
        if reason:
            message_to_reply = (
                f"𝙋𝙀𝙎𝘼𝙉 𝙊𝙏𝙊𝙈𝘼𝙏𝙄𝙎\n\n╭┈──────────────┈\n**▸ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴏꜰꜰʟɪɴᴇ**\n"
                f"**▸ ᴋᴀʀᴇɴᴀ :** `{reason}`\n╰┈───────────┈")
        else:
            message_to_reply = f"𝙋𝙀𝙎𝘼𝙉 𝙊𝙏𝙊𝙈𝘼𝙏𝙄𝙎\n\n╭┈──────────────┈\n**▸ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴏꜰꜰʟɪɴᴇ**\n╰┈───────────┈"
        try:
            if pic.endswith((".tgs", ".webp")):
                msg = await event.reply(file=pic)
                msgs = await event.reply(message_to_reply)
            else:
                msg = await event.reply(message_to_reply, file=pic)
        except BaseException:
            msg = await event.reply(message_to_reply)
        await asyncio.sleep(2.5)
        if event.chat_id in last_afk_message:
            await last_afk_message[event.chat_id].delete()
        try:
            if event.chat_id in last_afk_msg:
                await last_afk_msg[event.chat_id].delete()
        except BaseException:
            pass
        last_afk_message[event.chat_id] = msg
        try:
            if msgs:
                last_afk_msg[event.chat_id] = msgs
        except BaseException:
            pass


@register(outgoing=True, pattern="^.off(?: |$)(.*)",
          disable_errors=True)  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    global USER_AFK
    global afk_time
    global last_afk_message
    global last_afk_msg
    global afk_start
    global afk_end
    global reason
    global pic
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    last_afk_msg = {}
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    if reply:
        pic = await event.client.download_media(reply)
    else:
        pic = None
    if not USER_AFK:
        last_seen_status = await bot(
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()
        USER_AFK = f"yes: {reason} {pic}"
        if reason:
            try:
                if pic.endswith((".tgs", ".webp")):
                    await bot.send_message(event.chat_id, file=pic)
                    await bot.send_message(
                        event.chat_id, f"⚡OᖴᖴᒪIᑎE\n\n╭┈──────────────┈\n**▸ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴏꜰꜰʟɪɴᴇ**\n**▸ ᴋᴀʀᴇɴᴀ :** `{reason}`\n╰┈──────────┈"
                    )
                else:
                    await bot.send_message(
                        event.chat_id, f"⚡OᖴᖴᒪIᑎE\n\n╭┈──────────────┈\n**▸ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴏꜰꜰʟɪɴᴇ**\n**▸ ᴋᴀʀᴇɴᴀ :** `{reason}`\n╰┈──────────┈", file=pic
                    )
            except BaseException:
                await bot.send_message(
                    event.chat_id, f"⚡OᖴᖴᒪIᑎE\n\n╭┈──────────────┈\n**▸ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴏꜰꜰʟɪɴᴇ**\n**▸ ᴋᴀʀᴇɴᴀ :** `{reason}`\n╰┈──────────┈"
                )
        else:
            try:
                if pic.endswith((".tgs", ".webp")):
                    await bot.send_message(event.chat_id, file=pic)
                    await bot.send_message(
                        event.chat_id, f"**⚡OᖴᖴᒪIᑎE**\n╭┈──────────────┈\n**▸ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴏꜰꜰʟɪɴᴇ**\n╰┈──────────┈"
                    )
                else:
                    await bot.send_message(
                        event.chat_id, f"**⚡OᖴᖴᒪIᑎE**\n╭┈──────────────┈\n**▸ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴏꜰꜰʟɪɴᴇ**\n╰┈──────────┈", file=pic
                    )
            except BaseException:
                await bot.send_message(event.chat_id, f"**OᖴᖴᒪIᑎE**\n╭┈──────────────┈\n**▸ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴏꜰꜰʟɪɴᴇ**\n╰┈──────────┈")
        await event.delete()
        try:
            if reason and pic:
                if pic.endswith((".tgs", ".webp")):
                    await bot.send_message(BOTLOG_CHATID, file=pic)
                    await bot.send_message(
                        BOTLOG_CHATID, f"**⚡OᖴᖴᒪIᑎE**\n╭┈──────────────┈\n**▸ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴏꜰꜰʟɪɴᴇ**\n**▸ ᴋᴀʀᴇɴᴀ :** `{reason}`\n╰┈──────────┈"
                    )
                else:
                    await bot.send_message(
                        BOTLOG_CHATID, f"**⚡OᖴᖴᒪIᑎE**\n╭┈──────────────┈\n**▸ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴏꜰꜰʟɪɴᴇ**\n**▸ ᴋᴀʀᴇɴᴀ :** `{reason}`\n╰┈──────────┈", file=pic
                    )
            elif reason:
                await bot.send_message(
                    BOTLOG_CHATID, f"\n**⚡OᖴᖴᒪIᑎE**\n╭┈──────────────┈\n**▸ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴏꜰꜰʟɪɴᴇ**\n**▸ ᴋᴀʀᴇɴᴀ :** `{reason}`\n╰┈──────────┈"
                )
            elif pic:
                if pic.endswith((".tgs", ".webp")):
                    await bot.send_message(BOTLOG_CHATID, file=pic)
                    await bot.send_message(BOTLOG_CHATID, f"**⚡OᖴᖴᒪIᑎE**\n╭┈──────────────┈\n**▸ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴏꜰꜰʟɪɴᴇ**\n╰┈──────────┈")
                else:
                    await bot.send_message(BOTLOG_CHATID, f"**⚡OᖴᖴᒪIᑎE**\n╭┈──────────────┈\n**▸ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴏꜰꜰʟɪɴᴇ**\n╰┈──────────┈", file=pic)
            else:
                await bot.send_message(BOTLOG_CHATID, f"**⚡OᖴᖴᒪIᑎE **\n╭┈──────────────┈\n **▸ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴏꜰꜰʟɪɴᴇ **\n╰┈──────────┈")
        except Exception as e:
            BOTLOG_CHATIDger.warn(str(e))


CMD_HELP.update({"off": ".off (reason) atau balas media untuk itu "
                 "\nPenggunaan afk bisa dengan media keren ketika seseorang menandai atau membalas salah satu pesan atau chat pribadi Anda."})

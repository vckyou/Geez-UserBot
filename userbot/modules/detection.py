# Copyright © 2021 Lynx-Userbot (LLC Company (WARNING))
# GPL-3.0 License From Github (General Public License)
# Ported From Cat Userbot For Lynx-Userbot By Alvin/LiuAlvinas.
# Based On Plugins
# Credits by Alvin/Liualvinas & Cat Userbot.

import time

from telethon.tl.custom import Dialog
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import User
from userbot.events import register
from userbot import CMD_HELP, bot
from telethon.errors.rpcerrorlist import YouBlockedUserError

#Ported by KENZO @TeamSecret_Kz

@register(outgoing=True, pattern=r"^\.detect(?: |$)(.*)")
async def detect(event):
    if event.fwd_from:
        return
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not event.reply_to_msg_id:
        await event.edit("```Please reply to the user or type .detect (ID/Username) that you want to detect.```")
        return
    if input_str:
        try:
            uid = int(input_str)
        except ValueError:
            try:
                u = await event.client.get_entity(input_str)
            except ValueError:
                await edit.event("`Please Give ID/Username to Find History.`"
                                 )
            uid = u.id
    else:
        uid = reply_message.sender_id
    chat = "@tgscanrobot"
    event = await event.edit("`Currently Doing Account Detection...`")
    event = await event.edit("__Connecting to server telegram.__")
    event = await event.edit("__Connecting to server telegram..__")
    event = await event.edit("__Connecting to server telegram...__")
    event = await event.edit("__Connecting to server telegram.__")
    event = await event.edit("__Connecting to server telegram..__")
    event = await event.edit("__Connecting to server telegram...__")
    event = await event.edit("__Connecting to server telegram.__")
    event = await event.edit("__Connecting to server telegram..__")
    event = await event.edit("__Connecting to server telegram...__")
    event = await event.edit("__Connecting to server telegram.__")
    event = await event.edit("__Connecting to server telegram..__")
    event = await event.edit("__Connecting to server telegram...__")
    async with bot.conversation(chat) as conv:
        try:
            await conv.send_message(f"{uid}")
        except YouBlockedUserError:
            await steal.reply(
                "```Please Unblock @tgscanrobot And Try Again.```"
            )
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.edit(response.text)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


# Alvin Bau Sawi
CMD_HELP.update({
    "detection":
        "⚡𝘾𝙈𝘿⚡: `.detect`\
          \n↳ : Melihat Riwayat Grup Yang Pernah/Sedang dimasuki."
})

# Copyright (C) 2021 Geez Project

from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot.events import register
from userbot import CMD_HELP


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@register(outgoing=True, pattern=r"^\.vcinvite(?: |$)(.*)",
          disable_errors=True, groups_only=True)
async def _(e):
    ok = await e.edit("`Inviting Members to Voice Chat...`")
    users = []
    z = 0
    async for user in e.client.iter_participants(e.chat_id):
        if not user.bot:
            users.append(user.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await ok.edit(f"`Invited {z} users`")


CMD_HELP.update(
    {
        "vcplugin": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcinvite`"
        "\n• : Mengundang Seseorang Kedalam Vcg"
    }
)

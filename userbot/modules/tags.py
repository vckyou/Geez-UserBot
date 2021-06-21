# Port By @VckyouuBitch From Geez - Project
# Copyright © Geez - Project
# Credits By Ultroid

from telethon.tl.types import ChannelParticipantAdmin as admin
from telethon.tl.types import ChannelParticipantCreator as owner
from telethon.tl.types import UserStatusOffline as off
from telethon.tl.types import UserStatusOnline as onn
from telethon.tl.types import UserStatusRecently as rec
from telethon.utils import get_display_name

from userbot.events import register
from userbot import CMD_HELP


@register(
    outgoing=True,
    pattern=r"^\.tag(on|off|all|bots|rec|admins|owner)?(.*)",
    disable_errors=True,
)
async def _(e):
    okk = e.text
    lll = e.pattern_match.group(2)
    users = 0
    o = 0
    nn = 0
    rece = 0
    if lll:
        xx = f"{lll}"
    else:
        xx = ""
    async for bb in e.client.iter_participants(e.chat_id, 99):
        users = users + 1
        x = bb.status
        y = bb.participant
        if isinstance(x, onn):
            o = o + 1
            if "on" in okk:
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(x, off):
            nn = nn + 1
            if "off" in okk:
                if not (bb.bot or bb.deleted):
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(x, rec):
            rece = rece + 1
            if "rec" in okk:
                if not (bb.bot or bb.deleted):
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(y, owner):
            if "admin" or "owner" in okk:
                xx += f"\n👑 [{get_display_name(bb)}](tg://user?id={bb.id}) 👑"
        if isinstance(y, admin):
            if "admin" in okk:
                if not bb.deleted:
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if "all" in okk:
            if not (bb.bot or bb.deleted):
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if "bot" in okk:
            if bb.bot:
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
    await e.client.send_message(e.chat_id, xx)
    await e.delete()


CMD_HELP.update({
    'tags':
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tag all`"
    "\n• : Tag Top 100 Members of chat."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tag admin`"
    "\n• : Tag Admins of that chat."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tag owner`"
    "\n• : Tag Owner of that chat."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tag bot`"
    "\n• : Tag Bots of that chat."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tag rec`"
    "\n• : Tag recently Active Members."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tag on`"
    "\n• : Tag online Members(work only if privacy off)."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tag off`"
    "\n• : Tag Offline Members(work only if privacy off)."
})

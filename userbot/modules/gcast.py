import asyncio

from userbot.events import register
from userbot import CMD_HELP, DEVS, owner


GCAST_BLACKLIST = [
    -1001473548283,  # SharingUserbot
    -1001752592753,  # TedeSupport
    -1001476936696,  # AnosSupport
    -1001327032795,  # UltroidSupport
    -1001294181499,  # UserBotIndo
    -1001419516987,  # VeezSupportGroup
    -1001459812644,  # GeezSupportGroup
    -1001296934585,  # X-PROJECT BOT
    -1001481357570,  # UsergeOnTopic
    -1001459701099,  # CatUserbotSupport
    -1001109837870,  # TelegramBotIndonesia
    -1001752592753,  # Skyzusupport
    -1001456135097,  # SpamBot
    -1001462425381,  # RamSupportGroup
    -1001699144606,  # its
    -1001267233272,  # POCONG SEREM
    -1001386557465,  # Kitarosupport
    -1001692751821,  # ramsupportt
]

# BLACKLIST IN GROUP SUPPORT

@register(outgoing=True, pattern=r"^\.gcast(?: |$)(.*)")
async def gcast(event):
    xnxx = await event.client.get_me()
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit("**Berikan Sebuah Pesan atau Reply**")
        return
    kk = await event.edit("`Sedang Mengirim Pesan Secara Global... 📢`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            if chat not in GCAST_BLACKLIST:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**[{owner}](tg://user?id={xnxx.id}) Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**"
    )

@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Sedang Mengirim pesan secara global`")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`Sedang Mengirim pesan secara global!!!...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            if chat not in DEVS:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(f"Berhasil Mengirim Pesan Ke `{done}` obrolan, kesalahan dalam `{er}` obrolan(s)")


CMD_HELP.update(
    {
        "gcast": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gcast`\
         \n↳ : Mengirim Pesan Group Secara Global."})

CMD_HELP.update(
    {
         "gucast": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gucast`\
         \n↳ : Mengirim Pesan Pribadi Secara Global."
    }
)

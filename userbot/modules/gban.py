from telethon.events import ChatAction
from userbot import ALIVE_NAME, CMD_HELP, DEVS, bot
from userbot.events import register
from userbot.utils import get_user_from_event


@bot.on(ChatAction)
async def handler(tele):
    if tele.user_joined or tele.user_added:
        try:
            from userbot.modules.sql_helper.gmute_sql import is_gmuted

            guser = await tele.get_user()
            gmuted = is_gmuted(guser.id)
        except BaseException:
            return
        if gmuted:
            for i in gmuted:
                if i.sender == str(guser.id):
                    chat = await tele.get_chat()
                    admin = chat.admin_rights
                    creator = chat.creator
                    if admin or creator:
                        try:
                            await client.edit_permissions(
                                tele.chat_id, guser.id, view_messages=False
                            )
                            await tele.reply(
                                f"**Pengguna Gban Telah Bergabung** \n"
                                f"**Pengguna**: [{guser.id}](tg://user?id={guser.id})\n"
                                f"**Aksi**  : `Banned`"
                            )
                        except BaseException:
                            return


@register(outgoing=True, pattern="^.gban(?: |$)(.*)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cgban(?: |$)(.*)")
async def gben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`Ingin Mengaktifkan Perintah Global Banned!`")
    else:
        dark = await dc.edit("`Memproses Global Banned Pengguna Ini!!`")
    me = await userbot.client.get_me()
    await dark.edit(f"`Global Banned Akan Segera Aktif!!`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_user_from_event(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit(f"`Terjadi Kesalahan`")
    if user:
        if user.id in DEVS:
            return await dark.edit(
                f"`Anda Tidak Bisa Melakukan Global Banned, Karena dia pembuatku 🤪`"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await dark.edit(f"`Global Banned Aktif ✅`")
            except BaseException:
                b += 1
    else:
        await dark.edit(f"`Mohon Balas Ke Pesan Pengguna`")
    try:
        if gmute(user.id) is False:
            return await dark.edit(
                f"**Kesalahan! Pengguna Ini Sudah Kena Perintah Global Banned.**"
            )
    except BaseException:
        pass
    return await dark.edit(
        f"**Perintah:** `{ALIVE_NAME}`\n**Pengguna:** [{user.first_name}](tg://user?id={user.id})\n**Aksi:** `Global Banned`"
    )


@register(outgoing=True, pattern="^.ungban(?: |$)(.*)")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cungban(?: |$)(.*)")
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`Membatalkan Perintah Global Banned Pengguna Ini`")
    else:
        dark = await dc.edit("`Membatalkan Perintah Global Banned`")
    me = await userbot.client.get_me()
    await dark.edit(
        f"`Memulai Membatalkan Perintah Global Banned, Jangan Songong Lagi Ya!!!`"
    )
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_user_from_event(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("`Terjadi Kesalahan`")
    if user:
        if user.id in DEVS:
            return await dark.edit(
                "**Pengguna Ini tidak bisa di Blacklist, Karna Dia adalah pembuatku**"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await dark.edit(f"`Membatalkan Global Banned... Memproses... `")
            except BaseException:
                b += 1
    else:
        await dark.edit("`Harap Balas Ke Pesan Pengguna`")
    try:
        if ungmute(user.id) is False:
            return await dark.edit(
                "**Kesalahan! Pengguna Sedang Tidak Di Global Banned.**"
            )
    except BaseException:
        pass
    return await dark.edit(
        f"**Perintah :** `{ALIVE_NAME}`\n**Pengguna:** [{user.first_name}](tg://user?id={user.id})\n**Aksi:** `Membatalkan Global Banned`"
    )


CMD_HELP.update(
    {
        "gban": "\
**Modules:** __Global Banned__\n\n**Perintah:** `.gban`\
\n**Penjelasan:** Melakukan Banned Secara Global Ke Semua Grup Dimana Anda Sebagai Admin\
\n\n**Perintah:** `.ungban`\
\n**Penjelasan:** Membatalkan Global Banned"
    }
)

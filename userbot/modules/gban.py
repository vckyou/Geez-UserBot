from telethon.events import ChatAction
from userbot import ALIVE_NAME, CMD_HELP, bot
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from userbot.events import register
from telethon.tl.types import MessageEntityMentionName


async def get_full_user(event):
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Mohon Gunakan ID Pengguna atau Username.`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("`Terjadi Kesalahan... Silahkan Hubungi` @VckyouuBitch", str(err))
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


@bot.on(ChatAction)
async def handler(tele):
    if tele.user_joined or tele.user_added:
        try:
            pass

            guser = await tele.get_user()
            gmuted = is_gbanned(guser.id)
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
                                f"**Pengguna GBAN Telah Bergabung** \n"
                                f"**Pengguna** : [{guser.id}](tg://user?id={guser.id})\n"
                                f"**Aksi**  : `Banned`"
                            )
                        except BaseException:
                            return


@register(outgoing=True, pattern="^.gbans(?: |$)(.*)")
async def gben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`Saya Sedang Mengaktifkan Perintah Global Banned !`")
    else:
        dark = await dc.edit("`Connected to server telegram...`")
    me = await userbot.client.get_me()
    await dark.edit(f"`Global Banned Akan Segera Aktif, Anda Akan Dibanned Secara Global Oleh {ALIVE_NAME}`")
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
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit(f"`Mohon Maaf, Terjadi Kesalahan.❌`")
    if user:
        if user.id == 1282429349:
            return await dark.edit(
                f"`🚫 Anda Tidak Bisa Melakukan Global Banned Ke Geez, Dia Adalah Pembuat Saya.`"
            )
        try:
            pass
        except BaseException:
            pass
        try:
            await userbot.client(BlockRequest(user))
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
        await dark.edit(f"`Mohon Reply Ke Pesan Pengguna Yang Ingin Di Ban.`")
    try:
        if gmute(user.id) is False:
            return await dark.edit(f"**❌ Error: Pengguna Ini Sudah Terkena Global Banned.**")
    except BaseException:
        pass
    return await dark.edit(
        f"**⊙ Perintah Dari :** `{ALIVE_NAME}`\n**⊙ Pengguna :** [{user.first_name}](tg://user?id={user.id})\n**⊙ Aksi :** `Global Banned`"
    )


@register(outgoing=True, pattern="^.ungbans(?: |$)(.*)")
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if not sender.id == me.id:
        dark = await dc.reply("`Membatalkan Global Banned Pengguna Ini.`")
    else:
        dark = await dc.edit("`Connected to server telegram...`")
    me = await userbot.client.get_me()
    await dark.edit(f"`Mulai Membatalkan Global Banned, Pengguna Ini Akan Dapat Bergabung Ke Grup Anda.`")
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
        user, reason = await get_full_user(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("`❌ Error: Terjadi Kesalahan.`")
    if user:
        if user.id == 1448477501:
            return await dark.edit("**Anda Tidak Bisa Melakukan Perintah Ini, Dia Adalah Pembuatku.**")
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        try:
            await userbot.client(UnblockRequest(user))
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
                await dark.edit(f"`Sedang Membatalkan Global Banned...\n in Progress... `")
            except BaseException:
                b += 1
    else:
        await dark.edit("`Harap Reply Ke Pesan Pengguna Yang Ingin Anda Batalkan.`")
    try:
        if ungmute(user.id) is False:
            return await dark.edit("**❌ Error: Pengguna Memang Tidak Terkena Global Banned.**")
    except BaseException:
        pass
    return await dark.edit(
        f"**⊙ Perintah Dari :** `{ALIVE_NAME}`\n**⊙ Pengguna :** [{user.first_name}](tg://user?id={user.id})\n**⊙ Aksi :** `Global Banned Canceled`"
    )


CMD_HELP.update({
    "globalban":
    "⚡𝘾𝙈𝘿⚡: `.gbans`\
\n↳ : Melakukan Banned Secara Global Ke Semua Grup Dimana Anda Sebagai Admin.\
\n\n⚡𝘾𝙈𝘿⚡: `.ungbans`\
\n↳ : Membatalkan Banned Secara Global."})

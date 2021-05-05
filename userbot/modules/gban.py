from userbot import ALIVE_NAME, CMD_HELP, bot
from userbot.events import register

from telethon.events import ChatAction
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import MessageEntityMentionName

from userbot.modules.sql_helper import gban_sql


async def get_full_user(event):
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
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
            await event.edit("`Terjadi Kesalahan... Silahkan Hubungi` @VckyouuBitch", str(err))
            return
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
        user = await tele.get_user()
        chat = await tele.get_chat()
        if gban_sql.is_gbanned(user.id):
            if chat.admin_rights:
                try:
                    await tele.client.edit_permissions(
                        chat.id, user.id, view_messages=False
                    )
                    await tele.reply(
                        f"**Pengguna Gban Telah Bergabung**\n"
                        f"**User** : [{user.first_name}](tg://user?id={user.id})\n"
                        f"**Aksi** : `Banned`"
                    )
                except BaseException:
                    pass


@register(outgoing=True, pattern="^.gbans(?: |$)(.*)")
async def gben(event):
    if event.fwd_from:
        return
    geez = await event.edit("`Melakukan Global Ban pada Pengguna ini...`")
    chats = 0
    if event.is_private:
        userid = (await event.get_chat()).id
    elif event.reply_to_msg_id:
        userid = (await event.get_reply_message()).sender_id
    elif event.pattern_match.group(1):
        if (event.pattern_match.group(1)).isdigit():
            try:
                userid = (await event.client.get_entity(int(event.pattern_match.group(1)))).id
            except ValueError as verr:
                return await geez.edit(f"{str(verr)}")
        else:
            try:
                userid = (await event.client.get_entity(str(event.pattern_match.group(1)))).id
            except ValueError as verr:
                return await geez.edit(f"{str(verr)}")
    else:
        return await geez.edit("Balas sebuah pesan atau tambahkan id user")
    name = (await event.client.get_entity(userid)).first_name
    if userid == (await event.client.get_me()).id:
        await geez.edit("Apakah saya harus ban diri saya sendiri?")
        return
    if gban_sql.is_gbanned(userid):
        await geez.edit(f"[user](tg://user?id={userid}) sudah di global banned sebelumnya")
    async for gban in event.client.iter_dialogs():
        if gban.is_group or gban.is_channel:
            try:
                await event.client.edit_permissions(gban.id, userid, view_messages=False)
                chats += 1
            except BaseException:
                pass
    gban_sql.freakgban(userid)
    await geez.edit(
        f"`Gbanned` [{name}](tg://user?id={userid}) didalam {chats} grup"
    )


@register(outgoing=True, pattern="^.ungbans(?: |$)(.*)")
async def gunben(event):
    if event.fwd_from:
        return
    geez = await event.edit("`Melakukan UnGlobal Ban pada Pengguna ini...`")
    chats = 0
    if event.is_private:
        userid = (await event.get_chat()).id
    elif event.reply_to_msg_id:
        userid = (await event.get_reply_message()).sender_id
    elif event.pattern_match.group(1):
        if (event.pattern_match.group(1)).isdigit():
            try:
                userid = (await event.client.get_entity(int(event.pattern_match.group(1)))).id
            except ValueError as verr:
                return await geez.edit(f"{str(verr)}")
        else:
            try:
                userid = (await event.client.get_entity(str(event.pattern_match.group(1)))).id
            except ValueError as verr:
                return await geez.edit(f"{str(verr)}")
    else:
        return await geez.edit("Balas sebuah pesan atau tambahkan id user")
    name = (await event.client.get_entity(userid)).first_name
    if userid == (await event.client.get_me()).id:
        await geez.edit("Apakah saya harus UnGban diri saya sendiri?")
        return
    if not gban_sql.is_gbanned(userid):
        await geez.edit(f"[user](tg://user?id={userid}) tidak di gban")
    async for gban in event.client.iter_dialogs():
        if gban.is_group or gban.is_channel:
            try:
                await event.client.edit_permissions(gban.id, userid, view_messages=True)
                chats += 1
            except BaseException:
                pass
    gban_sql.freakungban(userid)
    await geez.edit(
        f"`Gbanned` [{name}](tg://user?id={userid}) didalam {chats} grup"
    )


CMD_HELP.update({
    "globalban":
    "⚡𝘾𝙈𝘿⚡: `.gbans`\
\n↳ : Melakukan Banned Secara Global Ke Semua Grup Dimana Anda Sebagai Admin.\
\n\n⚡𝘾𝙈𝘿⚡: `.ungbans`\
\n↳ : Membatalkan Banned Secara Global."})

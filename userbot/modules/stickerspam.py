from telethon import utils
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID, InputStickerSetShortName

from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern="^.sspam(?: |$)(.*)")
async def _(e):
    x = await e.get_reply_message()
    if not (x and x.media and hasattr(x.media, "document")):
        return await event.reply("`Reply To Sticker Only`")
    set = x.document.attributes[1]
    sset = await bot(
        GetStickerSetRequest(
            InputStickerSetID(
                id=set.stickerset.id,
                access_hash=set.stickerset.access_hash,
            )
        )
    )
    pack = sset.set.short_name
    docs = [
        utils.get_input_document(x)
        for x in (
            await bot(GetStickerSetRequest(InputStickerSetShortName(pack)))
        ).documents
    ]
    for xx in docs:
        await e.respond(file=(xx))


CMD_HELP.update({
    "stickerspam": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sspam`\
    \nUsage : Balas Sticker Untuk Spam Sticker"})

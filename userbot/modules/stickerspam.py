from telethon import utils
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID, InputStickerSetShortName

from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=r"^\.sspam")
async def _(event):
    x = await event.get_reply_message()
    if not (x and x.media and hasattr("document")):
        return await event.edit("`Reply To Sticker Only`")
    set = x.document.attributes[1]
    sset = await bot(
        GetStickerSetRequest(
            InputStickerSetID(
                id=set.stickerset.id,
                access_hash=stickerset_attr.stickerset.access_hash,
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
        await event.respond(file=(xx))


CMD_HELP.update(
    {
        "sspam": "`.sspam`\
    \nUsage : Balas Ke Sticker."
    })

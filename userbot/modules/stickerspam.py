# Port By @VckyouuBitch From GeezProject

from telethon import utils
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID, InputStickerSetShortName

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.sspam (.*)")
async def _(event):
    x = await event.get_reply_message()
    if not (x and x.media and hasattr(x.media, "document")):
        return await event.edit("`Reply To Sticker Only`")
    set = x.document.attributes[1]
    sset = await event_bot(
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
            await event_bot(GetStickerSetRequest(InputStickerSetShortName(pack)))
        ).documents
    ]
    for xx in docs:
        await event.respond(file=(xx))


CMD_HELP.update({"sspam": "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sspam` <kota>"
                 "\n↳ : Balas Pesan Ke sticker."})

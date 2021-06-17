# Special thanks to Ultroid
# Ported By @VckyouuBitch From Geez - Project
# Copyright (c) Geez - Project
#
# https://github.com/Vckyou/Geez-UserBot


from telethon import utils
from telethon.errors import PackShortNameOccupiedError

from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=r"^\.stkrinfo$", disable_errors=True)
async def pack_kangish(_):
    _e = await _.get_reply_message()
    if not _e:
        return await _.edit("`Reply to Sticker.`")
    if len(_.text) > 9:
        _packname = _.text.split(" ", maxsplit=1)[1]
    else:
        _packname = f"Geez Stickers Kang By {_.sender_id}"
    if _e and _e.media and _e.media.document.mime_type == "image/webp":
        _id = _e.media.document.attributes[1].stickerset.id
        _hash = _e.media.document.attributes[1].stickerset.access_hash
        _get_stiks = await bot(
            functions.messages.GetStickerSetRequest(
                stickerset=types.InputStickerSetID(id=_id, access_hash=_hash)
            )
        )
        stiks = []
        for i in _get_stiks.documents:
            x = utils.get_input_document(i)
            stiks.append(
                types.InputStickerSetItem(
                    document=x,
                    emoji=(i.attributes[1]).alt,
                )
            )
        try:
            eval(udB.get("PACKKANG"))
        except BaseException:
            udB.set("PACKKANG", "{}")
        ok = eval(udB.get("PACKKANG"))
        try:
            pack = ok[_.sender_id] + 1
        except BaseException:
            pack = 1
        try:
            _r_e_s = await asst(
                functions.stickers.CreateStickerSetRequest(
                    user_id=_.sender_id,
                    title=_packname,
                    short_name=f"ult_{_.sender_id}_{pack}_by_{(await tgbot.get_me()).username}",
                    stickers=stiks,
                )
            )
            ok.update({_.sender_id: pack})
            udB.set("PACKKANG", str(ok))
        except PackShortNameOccupiedError:
            time.sleep(1)
            pack += 1
            _r_e_s = await asst(
                functions.stickers.CreateStickerSetRequest(
                    user_id=_.sender_id,
                    title=_packname,
                    short_name=f"ult_{_.sender_id}_{pack}_by_{(await tgbot.get_me()).username}",
                    stickers=stiks,
                )
            )
            ok.update({_.sender_id: pack})
            udB.set("PACKKANG", str(ok))
        await _.edit(f"Pack Kanged Successfully.\nKanged Pack: [link](https://t.me/addstickers/{_r_e_s.set.short_name})",
                     )
    else:
        await _.edit("Unsupported File")


CMD_HELP.update({
    "packkang":
        "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.packkang <balas di sticker>`\
          \n📌 : Kang set stiker Lengkap (dengan nama custom)."
})

# Geez - UserBot
# Copyright (C) 2021 TeamUltroid
#
# PLease read the GNU Affero General Public License in
# This file is a part of < Https://github.com/vckyou/Geez-UserBot/ >
# <https://www.github.com/Vckyou/Geez-UserBot/blob/Geez-UserBot/LICENSE/>
#
# Ported By Vicky <viicky.auliaz@gmail.com>


import glob
import os
import random

from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterPhotos

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node


@register(outgoing=True, pattern=r"^\.logo(?: |$)(.*)", disable_errors=True)
async def logo_gen(event):
    await event.edit(get_string("com_1"))
    name = event.pattern_match.group(1)
    if not name:
        await event.edit("`Give a name too!`")
    bg_, font_ = "", ""
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            if hasattr(temp.media, "document"):
                if "font" in temp.file.mime_type:
                    font_ = await temp.download_media()
                elif (".ttf" in temp.file.name) or (".otf" in temp.file.name):
                    font_ = await temp.download_media()
            elif "pic" in mediainfo(temp.media):
                bg_ = await temp.download_media()
    else:
        pics = []
        async for i in event.client.iter_messages(
            "@UltroidLogos", filter=InputMessagesFilterPhotos
        ):
            pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download_media()
        fpath_ = glob.glob("resources/fonts/*")
        font_ = random.choice(fpath_)
    if not bg_:
        pics = []
        async for i in event.client.iter_messages(
            "@UltroidLogos", filter=InputMessagesFilterPhotos
        ):
            pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download_media()
    if not font_:
        fpath_ = glob.glob("resources/fonts/*")
        font_ = random.choice(fpath_)
    if len(name) <= 8:
        fnt_size = 150
        strke = 10
    elif len(name) >= 9:
        fnt_size = 50
        strke = 5
    else:
        fnt_size = 130
        strke = 20
    img = Image.open(bg_)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_, fnt_size)
    w, h = draw.textsize(name, font=font)
    h += int(h * 0.21)
    image_width, image_height = img.size
    draw.text(
        ((image_width - w) / 2, (image_height - h) / 2),
        name,
        font=font,
        fill=(255, 255, 255),
    )
    x = (image_width - w) / 2
    y = (image_height - h) / 2
    draw.text((x, y), name, font=font, fill="white",
              stroke_width=strke, stroke_fill="black")
    flnme = f"ultd.png"
    img.save(flnme, "png")
    await event.edit("`Done!`")
    if os.path.exists(flnme):
        await event.client.send_file(
            event.chat_id,
            file=flnme,
            caption=f"Logo by [{DEFAULTUSER}](tg://user?id={DEFAULTUSER})",
            force_document=True,
        )
        os.remove(flnme)
        await event.delete()
    if os.path.exists(bg_):
        os.remove(bg_)
    if os.path.exists(font_):
        if not font_.startswith("resources/fonts"):
            os.remove(font_)


CMD_HELP.update({
    "logo":
        "𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `.logo <text>`\
          \nUsage : __Hasilkan logo dari Teks atau Balas Ke gambar yang diberikan, untuk menulis teks Anda di atasnya. Atau Balas Ke File Font, Untuk menulis dengan font itu.__."
})

# Port By @VckyouuBitch From Geez - Projects
# Credits © Geez - Projects
import os
import random

from carbonnow import Carbon

from userbot import CMD_HELP, bot
from userbot.events import register

all_col = [
    "Black",
    "Navy",
    "DarkBlue",
    "MediumBlue",
    "Blue",
    "DarkGreen",
    "Green",
    "Teal",
    "DarkCyan",
    "DeepSkyBlue",
    "DarkTurquoise",
    "MediumSpringGreen",
    "Lime",
    "SpringGreen",
    "Aqua",
    "Cyan",
    "MidnightBlue",
    "DodgerBlue",
    "LightSeaGreen",
    "ForestGreen",
    "SeaGreen",
    "DarkSlateGray",
    "DarkSlateGrey",
    "LimeGreen",
    "MediumSeaGreen",
    "Turquoise",
    "RoyalBlue",
    "SteelBlue",
    "DarkSlateBlue",
    "MediumTurquoise",
    "Indigo  ",
    "DarkOliveGreen",
    "CadetBlue",
    "CornflowerBlue",
    "RebeccaPurple",
    "MediumAquaMarine",
    "DimGray",
    "DimGrey",
    "SlateBlue",
    "OliveDrab",
    "SlateGray",
    "SlateGrey",
    "LightSlateGray",
    "LightSlateGrey",
    "MediumSlateBlue",
    "LawnGreen",
    "Chartreuse",
    "Aquamarine",
    "Maroon",
    "Purple",
    "Olive",
    "Gray",
    "Grey",
    "SkyBlue",
    "LightSkyBlue",
    "BlueViolet",
    "DarkRed",
    "DarkMagenta",
    "SaddleBrown",
    "DarkSeaGreen",
    "LightGreen",
    "MediumPurple",
    "DarkViolet",
    "PaleGreen",
    "DarkOrchid",
    "YellowGreen",
    "Sienna",
    "Brown",
    "DarkGray",
    "DarkGrey",
    "LightBlue",
    "GreenYellow",
    "PaleTurquoise",
    "LightSteelBlue",
    "PowderBlue",
    "FireBrick",
    "DarkGoldenRod",
    "MediumOrchid",
    "RosyBrown",
    "DarkKhaki",
    "Silver",
    "MediumVioletRed",
    "IndianRed ",
    "Peru",
    "Chocolate",
    "Tan",
    "LightGray",
    "LightGrey",
    "Thistle",
    "Orchid",
    "GoldenRod",
    "PaleVioletRed",
    "Crimson",
    "Gainsboro",
    "Plum",
    "BurlyWood",
    "LightCyan",
    "Lavender",
    "DarkSalmon",
    "Violet",
    "PaleGoldenRod",
    "LightCoral",
    "Khaki",
    "AliceBlue",
    "HoneyDew",
    "Azure",
    "SandyBrown",
    "Wheat",
    "Beige",
    "WhiteSmoke",
    "MintCream",
    "GhostWhite",
    "Salmon",
    "AntiqueWhite",
    "Linen",
    "LightGoldenRodYellow",
    "OldLace",
    "Red",
    "Fuchsia",
    "Magenta",
    "DeepPink",
    "OrangeRed",
    "Tomato",
    "HotPink",
    "Coral",
    "DarkOrange",
    "LightSalmon",
    "Orange",
    "LightPink",
    "Pink",
    "Gold",
    "PeachPuff",
    "NavajoWhite",
    "Moccasin",
    "Bisque",
    "MistyRose",
    "BlanchedAlmond",
    "PapayaWhip",
    "LavenderBlush",
    "SeaShell",
    "Cornsilk",
    "LemonChiffon",
    "FloralWhite",
    "Snow",
    "Yellow",
    "LightYellow",
    "Ivory",
    "White",
]


@register(outgoing=True, pattern=r"^\.carbon")
async def crbn(event):
    xxxx = await event.edit(get_string("com_1"))
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            b = await bot.download_media(temp)
            a = open(b)
            code = a.read()
            a.close()
            os.remove(b)
        else:
            code = temp.message
    else:
        code = event.text.split(" ", maxsplit=1)[1]
    carbon = Carbon(code=code)
    xx = await carbon.save("geez_carbon")
    await xxxx.delete()
    await bot.send_file(
        event.chat_id,
        xx,
        caption=f"Carbonised by [{OWNER_NAME}](tg://user?id={OWNER_ID})",
        force_document=True,
    )
    os.remove(xx)


@register(outgoing=True, pattern=r"^\.rcarbon$")
async def crbn(event):
    xxxx = await event.edit("Processing")
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            b = await bot.download_media(temp)
            a = open(b)
            code = a.read()
            a.close()
            os.remove(b)
        else:
            code = temp.message
    else:
        code = event.text.split(" ", maxsplit=1)[1]
    col = random.choice(all_col)
    carbon = Carbon(code=code, background=col)
    xx = await carbon.save("geez_carbon")
    await xxxx.delete()
    await bot.send_file(
        event.chat_id,
        xx,
        caption=f"Carbonised by [{OWNER_NAME}](tg://user?id={OWNER_ID})",
        force_document=True,
    )
    os.remove(xx)


CMD_HELP.update(
    {
        "carbon": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.carbon` <text/reply to msg/reply to document>\
         \n↳ : `Carbonise the text with default settings.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.rcarbon` <text/reply to msg/reply to document>\
         \n↳ : `Carbonise the text, with random bg colours`"
    }
)

import json
import urllib.request


from userbot.events import register
from userbot import CMD_HELP


# Port By @VckyouuBitch From GeezProject
# Buat Kamu Yang Hapus Credits. Intinya Kamu Anjing:)
@register(outgoing=True, pattern="^.ip(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)

    adress = input_str

    token = "19e7f2b6fe27deb566140aae134dec6b"

    api = "http://api.ipstack.com/" + adress + "?access_key=" + token + "&format=1"

    result = urllib.request.urlopen(api).read()
    result = result.decode()

    result = json.loads(result)
    geez1 = result["type"]
    geez2 = result["country_code"]
    geez3 = result["region_name"]
    geez4 = result["city"]
    geez5 = result["zip"]
    geez6 = result["latitude"]
    geez7 = result["longitude"]
    await event.edit(
        f"<b><u>INFORMASI BERHASIL DIKUMPULKAN</b></u>\n\n<b>Ip type :-</b><code>{geez1}</code>\n<b>Country code:- </b> <code>{geez2}</code>\n<b>State name :-</b><code>{geez3}</code>\n<b>City name :- </b><code>{geez4}</code>\n<b>zip :-</b><code>{geez5}</code>\n<b>Latitude:- </b> <code>{geez6}</code>\n<b>Longitude :- </b><code>{geez7}</code>\n",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "fakeaddress": "**IP HACK**\
\n\n**Syntax : **`.ip <ip address>`\
\n**Usage :** Memberikan detail tentang alamat ip."
    }
)

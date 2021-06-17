from os import remove

from shazamio import Shazam

from userbot.events import register
from userbot import CMD_HELP

shazam = Shazam()


@register(outgoing=True, pattern="^.shazam$")
async def song_recog(event):
    if not event.reply_to_msg_id:
        return await event.edit("`Reply to a song file to recognise it!`", time=10)
    geez = await event.edit(get_string("com_1"))
    reply = await event.get_reply_message()
    t_ = mediainfo(reply.media)
    if t_ != "audio":
        return await event.edit("`Please use as reply to an audio file.`", time=5)
    await geez.edit("`Downloading...`")
    path_to_song = "./temp/shaazam_cache/unknown.mp3"
    await reply.download_media(path_to_song)
    await geez.edit("`Trying to identify the song....`")
    try:
        res = await shazam.recognize_song(path_to_song)
    except Exception as e:
        return await geez.edit(str(e), time=10)
    try:
        x = res["track"]
    except KeyError:
        return await geez.edit("`Couldn't identify song :(`", time=5)
    await geez.edit(f"**Song Recognised!**\nName: __{x['title']}__")
    remove(path_to_song)


CMD_HELP.update({
        "getjudul": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.getjudul`\
    \nUsage : Reply ke file lagu, untuk mengenali lagu tersebut.."
    }
)

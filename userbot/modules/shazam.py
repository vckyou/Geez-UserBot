# Ported By VICKY <@VckyouuBitch>
#
# Geez Projects UserBot
# Copyright (C) 2021 GeezProjects
#
# This file is a part of <https://github.com/vckyou/GeezProjects/>
# PLease read the GNU Affero General Public License in
# <https://github.com/vckyou/GeezProjects/blob/master/LICENSE>.


from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.shazam(?: |$)(.*)")
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await event.edit("```Membalas pesan audio.```")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                await event.edit("```Mengidentifikasi lagu```")
                start_msg = await conv.send_message("/start")
                response = await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio received"):
                    return await event.edit(
                        "Terjadi kesalahan saat mengidentifikasi lagu. Coba gunakan pesan audio berdurasi 5-10 detik."
                    )
                await event.edit("```Tunggu sebentar...```")
                result = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("```Mohon buka blokir (@auddbot) dan coba lagi```")
                return
            namem = f"**Judul : **{result.text.splitlines()[0]}\
        \n\n**Details : **__{result.text.splitlines()[2]}__"
            await event.edit(namem)
            await event.client.delete_messages(
                conv.chat_id, [start_msg.id, send_audio.id, check.id, result.id, response.id]
            )
    except TimeoutError:
        return await event.edit("`Error: `@auddbot` tidak merespons, coba lagi nanti")

CMD_HELP.update(
    {
        "shazam": ">`.shazam <reply to voice/audio>"
        "\nUsage: Reverse search audio file using (@auddbot)"
    }
)

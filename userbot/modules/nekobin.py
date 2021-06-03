import os
from datetime import datetime

import requests

from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=r"^\.(\w+)nekos (.*)")
async def _(event):
    if event.fwd_from:
        return
    datetime.now()
    if not os.path.isdir(TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TMP_DOWNLOAD_DIRECTORY)
    input_str = event.pattern_match.group(1)
    message = "SYNTAX: `.neko <long text to include>`"
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await bot.download_media(
                previous_message,
                TMP_DOWNLOAD_DIRECTORY,
                progress_callback=progress,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                # message += m.decode("UTF-8") + "\r\n"
                message += m.decode("UTF-8")
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = "SYNTAX: `.neko <long text to include>`"
    if downloaded_file_name.endswith(".py"):
        py_file = ""
        py_file += ".py"
        data = message
        key = (requests.post("https://nekobin.com/api/documents",
                             json={"content": data}) .json() .get("result") .get("key"))
        url = f"https://nekobin.com/{key}{py_file}"
    else:
        data = message
        key = (requests.post("https://nekobin.com/api/documents",
                             json={"content": data}) .json() .get("result") .get("key"))
        url = f"https://nekobin.com/{key}"

    reply_text = f"Pasted to Nekobin : [neko]({url})"
    await edit_or_reply(event, reply_text)


CMD_HELP.update(
    {
        "nekos": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.nekos`"
        "\n• : Buat tempel atau url singkat menggunakan dogbin"
    }
)

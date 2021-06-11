# Ported By VCKYOU @VckyouuBitch
# Credits © Geez-Project
# Ya gitu deh:')

import os
from shutil import rmtree

import requests

@register(outgoing=True, pattern="^.img (.*)")
async def goimg(event):
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("`Give something to search...`")
    geez = await event.edit("`Processing Keep Patience...`")
    if ";" in query:
        try:
            lmt = int(query.split(";")[1])
            query = query.split(";")[0]
        except BaseExceptaion:
            lmt = 5
    else:
        lmt = 5
    gi = googleimagesdownload()
    args = {
        "keywords": query,
        "limit": lmt,
        "format": "jpg",
        "output_directory": "./downloads/",
    }
    pth = gi.download(args)
    ann = pth[0][query]
    await event.client.send_file(event.chat_id, ann, caption=query, album=True)
    rmtree(f"./downloads/{query}/")
    await geez.delete()

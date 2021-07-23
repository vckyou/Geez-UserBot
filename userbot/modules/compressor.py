# Thanks Full To Team Ultroid
#
# Geez - Projects <https://github.com/Vckyou/Geez-UserBot/>
# Ported By Vcky @VckyouuBitch
# Copyright (c) 2021 Geez - Projects
#
# Geez - UserBot <
# https://github.com/vckyou/Geez-UserBot/blob/Geez-UserBot/LICENSE/ >

import asyncio
import os
import re
import time
from datetime import datetime as dt

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from telethon.tl.types import DocumentAttributeVideo

from userbot.events import register
from userbot import CMD_HELP


async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err


async def downloader(filename, file, event, taime, msg):
    with open(filename, "wb") as fk:
        result = await downloadable(
            client=event.client,
            location=file,
            out=fk,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d,
                    t,
                    event,
                    taime,
                    msg,
                ),
            ),
        )
    return result


async def uploader(file, name, taime, event, msg):
    with open(file, "rb") as f:
        result = await uploadable(
            client=event.client,
            file=f,
            name=name,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d,
                    t,
                    event,
                    taime,
                    msg,
                ),
            ),
        )
    return result


async def updateme_requirements():
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join(
                [sys.executable, "-m", "pip", "install", "--no-cache-dir", "-r", reqs]
            ),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


async def dloader(e, host, file):
    selected = CMD_WEB[host].format(file)
    process = await asyncio.create_subprocess_shell(
        selected, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    os.remove(file)
    return await e.edit(f"`{stdout.decode()}`")


@register(outgoing=True, pattern="^.comp (.*)")
async def _(e):
    cr = e.pattern_match.group(1)
    crf = 27
    to_stream = False
    if cr:
        k = e.text.split()
        if len(k) == 2:
            crf = int(k[1]) if k[1].isdigit() else 27
        elif len(k) > 2:
            crf = int(k[1]) if k[1].isdigit() else 27
            to_stream = True if "stream" in k[2] else False
    vido = await e.get_reply_message()
    if vido and vido.media:
        if "video" in mediainfo(vido.media):
            if hasattr(vido.media, "document"):
                vfile = vido.media.document
                name = vido.file.name
            else:
                vfile = vido.media
                name = ""
            if not name:
                name = "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
            xxx = await event.edit("`Trying To Download...`")
            c_time = time.time()
            file = await downloader(
                "resources/downloads/" + name,
                vfile,
                xxx,
                c_time,
                "Downloading " + name + "...",
            )
            o_size = os.path.getsize(file.name)
            d_time = time.time()
            diff = time_formatter((d_time - c_time) * 1000)
            file_name = (file.name).split("/")[-1]
            out = file_name.replace(file_name.split(".")[-1], "compressed.mkv")
            await xxx.edit(
                f"`Downloaded {file.name} of {humanbytes(o_size)} in {diff}.\nNow Compressing...`"
            )
            x, y = await bash(
                f'mediainfo --fullscan """{file.name}""" | grep "Frame count"'
            )
            total_frames = x.split(":")[1].split("\n")[0]
            progress = "progress.txt"
            with open(progress, "w") as fk:
                pass
            proce = await asyncio.create_subprocess_shell(
                f'ffmpeg -hide_banner -loglevel quiet -progress {progress} -i """{file.name}""" -preset ultrafast -vcodec libx265 -crf {crf} """{out}""" -y',
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            while proce.returncode != 0:
                await asyncio.sleep(3)
                with open(progress, "r+") as fil:
                    text = fil.read()
                    frames = re.findall("frame=(\\d+)", text)
                    size = re.findall("total_size=(\\d+)", text)

                    if len(frames):
                        elapse = int(frames[-1])
                    if len(size):
                        size = int(size[-1])
                        per = elapse * 100 / int(total_frames)
                        time_diff = time.time() - int(d_time)
                        speed = round(elapse / time_diff, 2)
                        some_eta = (
                            (int(total_frames) - elapse) / speed) * 1000
                        text = f"`Compressing {file_name} at {crf} CRF.\n`"
                        progress_str = "`[{0}{1}] {2}%\n\n`".format(
                            "".join(["●" for i in range(math.floor(per / 5))]),
                            "".join(["" for i in range(20 - math.floor(per / 5))]),
                            round(per, 2),
                        )
                        e_size = (humanbytes(size) + " of ~" +
                                  humanbytes((size / per) * 100))
                        eta = "~" + time_formatter(some_eta)
                        try:
                            await xxx.edit(
                                text
                                + progress_str
                                + "`"
                                + e_size
                                + "`"
                                + "\n\n`"
                                + eta
                                + "`"
                            )
                        except MessageNotModifiedError:
                            pass
            os.remove(file.name)
            c_size = os.path.getsize(out)
            f_time = time.time()
            difff = time_formatter((f_time - d_time) * 1000)
            await xxx.edit(
                f"`Compressed {humanbytes(o_size)} to {humanbytes(c_size)} in {difff}\nTrying to Upload...`"
            )
            differ = 100 - ((c_size / o_size) * 100)
            caption = f"**Original Size: **`{humanbytes(o_size)}`\n"
            caption += f"**Compressed Size: **`{humanbytes(c_size)}`\n"
            caption += f"**Compression Ratio: **`{differ:.2f}%`\n"
            caption += f"\n**Time Taken To Compress: **`{difff}`"
            mmmm = await uploader(
                out,
                out,
                f_time,
                xxx,
                "Uploading " + out + "...",
            )
            if to_stream:
                metadata = extractMetadata(createParser(out))
                duration = metadata.get("duration").seconds
                hi, _ = await bash(f'mediainfo "{out}" | grep "Height"')
                wi, _ = await bash(f'mediainfo "{out}" | grep "Width"')
                height = int(hi.split(":")[1].split()[0])
                width = int(wi.split(":")[1].split()[0])
                attributes = [
                    DocumentAttributeVideo(
                        duration=duration,
                        w=width,
                        h=height,
                        supports_streaming=True)]
                await e.client.send_file(
                    e.chat_id,
                    mmmm,
                    thumb="resources/extras/geezlogo.png",
                    caption=caption,
                    attributes=attributes,
                    force_document=False,
                    reply_to=e.reply_to_msg_id,
                )
            else:
                await e.client.send_file(
                    e.chat_id,
                    mmmm,
                    thumb="resources/extras/geezlogo.png",
                    caption=caption,
                    force_document=True,
                    reply_to=e.reply_to_msg_id,
                )
            await xxx.delete()
            os.remove(out)
        else:
            await e.edit("`Reply To Video File Only`")
    else:
        await e.edit("`Reply To Video File Only`")

CMD_HELP.update(
    {
        "compress": "`.comp`<reply to video>`\
    \n\nExample: `kompres 27 aliran` atau `kompres 28`
      Encode video yang dibalas sesuai dengan nilai CRF.
        Lebih sedikit CRF == Kualitas Tinggi, Lebih Banyak Ukuran
        Lebih banyak CRF == Kualitas Rendah, Ukuran Lebih Kecil
        Rentang CRF=20 - 51
        Standar=27"
    }
)

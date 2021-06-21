# Thanks Full To Ultroid
# Ported By @VckyouuBitch
# Copyright (c) 2021 Geez - Projects
# Geez - Projects https://github.com/Vckyou/Geez-UserBot

import json
import os
import random
import time

from lyrics_extractor import SongLyrics as sl
from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (ContentTooShortError, DownloadError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
from youtubesearchpython import SearchVideos

from userbot.events import register
from userbot import CMD_HELP, ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node


@register(outgoing=True, pattern=r"^\.song (.*)")
async def download_video(event):
    a = event.text
    if len(a) >= 5 and a[5] == "s":
        return
    await event.edit("`Sedang Memproses Musik, Mohon Tunggu Sebentar...`")
    url = event.pattern_match.group(1)
    if not url:
        return await event.edit("**List Error**\nCara Penggunaan : -`.musik <Judul Lagu>`")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await event.edit("`Tidak Dapat Menemukan Musik...`")
    type = "audio"
    await event.edit(f"`Persiapan Mendownload {url}...`")
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
    try:
        await event.edit("`Mendapatkan Info Musik...`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await event.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await event.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await event.edit("`Video is not available from your geographic location due to"
                         + " geographic restrictions imposed by a website.`"
                         )
        return
    except MaxDownloadsReached:
        await event.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await event.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await event.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        return await event.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await event.edit("`There was an error during info extraction.`")
    except Exception as e:
        return await event.edit(f"{str(type(e)): {str(e)}}")
    dir = os.listdir()
    if f"{rip_data['id']}.mp3.jpg" in dir:
        thumb = f"{rip_data['id']}.mp3.jpg"
    elif f"{rip_data['id']}.mp3.webp" in dir:
        thumb = f"{rip_data['id']}.mp3.webp"
    else:
        thumb = None
    upteload = """
Connected to server...
• {}
• By - {}
""".format(
        rip_data["title"], rip_data["uploader"]
    )
    await event.edit(f"`{upteload}`")
    CAPT = f"╭┈────────────────┈\n➥ {rip_data['title']}\n➥ Uploader - {rip_data['uploader']}\n╭┈────────────────┈╯\n➥ By : {DEFAULTUSER}\n╰┈────────────────┈➤"
    await event.client.send_file(
        event.chat_id,
        f"{rip_data['id']}.mp3",
        thumb=thumb,
        supports_streaming=True,
        caption=CAPT,
        attributes=[
            DocumentAttributeAudio(
                duration=int(rip_data["duration"]),
                title=str(rip_data["title"]),
                performer=str(rip_data["uploader"]),
            )
        ],
    )
    await event.delete()
    os.remove(f"{rip_data['id']}.mp3")
    try:
        os.remove(thumb)
    except BaseException:
        pass


@register(outgoing=True, pattern=r"^\.vsongs (.*)")
async def download_vsong(event):
    x = await event.edit("Processing..")
    url = event.pattern_match.group(1)
    if not url:
        return await x.edit("**Error**\nUsage - `.vsong <song name>`")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await x.edit("`No matching songs found...`")
    type = "audio"
    await x.edit("`Preparing to download...`")
    if type == "audio":
        opts = {
            "format": "best",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
            ],
            "outtmpl": "%(id)s.mp4",
            "logtostderr": False,
            "quiet": True,
        }
    try:
        await x.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        return await x.edit(f"`{str(DE)}`")
    except ContentTooShortError:
        return await x.edit("`The download content was too short.`")
    except GeoRestrictedError:
        return await x.edit(
            "`Video is not available from your geographic location due to"
            + " geographic restrictions imposed by a website.`"
        )
    except MaxDownloadsReached:
        return await x.edit("`Max-downloads limit has been reached.`")
    except PostProcessingError:
        return await x.edit("`There was an error during post processing.`")
    except UnavailableVideoError:
        return await x.edit("`Media is not available in the requested format.`")
    except XAttrMetadataError as XAME:
        return await x.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await x.edit("`There was an error during info extraction.`")
    except Exception as e:
        return await x.edit(f"{str(type(e)): {str(e)}}")
    tail = time.time()
    ttt = await uploader(
        rip_data["id"] + ".mp4",
        rip_data["title"] + ".mp4",
        tail,
        x,
        "Uploading " + rip_data["title"],
    )
    CAPT = f"⫸ Song - {rip_data['title']}\n⫸ By - {rip_data['uploader']}\n"
    await event.client.send_file(
        event.chat_id,
        ttt,
        supports_streaming=True,
        caption=CAPT,
    )
    os.remove(f"{rip_data['id']}.mp4")
    await x.delete()


@register(outgoing=True, pattern=r"^\.lirik (.*)")
async def original(event):
    if not event.pattern_match.group(1):
        return await event.edit("Beri Saya Sebuah Judul Lagu Untuk Mencari Lirik.\n**Contoh** : `.lirik` <Judul Lagu>")
    geez = event.pattern_match.group(1)
    event = await event.edit("`Sedang Mencari Lirik Lagu...`")
    dc = random.randrange(1, 3)
    if dc == 1:
        piki = "AIzaSyAyDBsY3WRtB5YPC6aB_w8JAy6ZdXNc6FU"
    if dc == 2:
        piki = "AIzaSyBF0zxLlYlPMp9xwMQqVKCQRq8DgdrLXsg"
    if dc == 3:
        piki = "AIzaSyDdOKnwnPwVIQ_lbH5sYE4FoXjAKIQV0DQ"
    extract_lyrics = sl(f"{piki}", "15b9fb6193efd5d90")
    sh1vm = extract_lyrics.get_lyrics(f"{geez}")
    a7ul = sh1vm["lyrics"]
    await event.client.send_message(event.chat_id, a7ul, reply_to=event.reply_to_msg_id)
    await event.delete()


CMD_HELP.update(
    {
        "musikdownload": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.song <Penyanyi atau Band - Judul Lagu>`\
         \n↳ : Mengunduh Sebuah Lagu Yang Diinginkan.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vsong` `<judul lagu>`\
         \n↳ : `unggah video lagu.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.lirik` <Penyanyi atau Band - Judul Lagu>`\
         \n↳ : Mencari Lirik Lagu Yang Diinginkan."
    }
)

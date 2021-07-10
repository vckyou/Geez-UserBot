# Coded By Abdul <https://github.com/DoellBarr>
# Ported By VckyAuliaZulfikar @VckyouuBitch
#
# Geez Projects UserBot
# Copyright (C) 2021 GeezProjects
#
# This file is a part of <https://github.com/vckyou/GeezProjects/>
# PLease read the GNU Affero General Public License in
# <https://github.com/vckyou/GeezProjects/blob/master/LICENSE>.

import asyncio
import csv
import random

from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserPrivacyRestrictedError,
    UserNotMutualContactError
)

from userbot.events import register
from userbot import CMD_HELP
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser


@register(outgoing=True, pattern=r"^\.getmemb$")
async def scrapmem(event):
    chat = event.chat_id
    await event.edit("`Mohon tunggu...`")
    event.client
    members = await event.client.get_participants(chat, aggressive=True)

    with open("members.csv", "w", encoding="UTF-8") as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        writer.writerow(["user_id", "hash"])
        for member in members:
            writer.writerow([member.id, member.access_hash])
    await event.edit("`Berhasil Mengumpulkan Member..`")


@register(outgoing=True, pattern=r"^\.addmemb$")
async def admem(event):
    await event.edit("`Proses Menambahkan 0 Member...`")
    chat = await event.get_chat()
    event.client
    users = []
    with open("members.csv", encoding="UTF-8") as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {'id': int(row[0]), 'hash': int(row[1])}
            users.append(user)
    n = 0
    for user in users:
        n += 1
        if n % 30 == 0:
            await event.edit(f"`Mencapai 30 anggota, tunggu selama {900/60} menit`")
            await asyncio.sleep(900)
        try:
            userin = InputPeerUser(user['id'], user['hash'])
            await event.client(InviteToChannelRequest(chat, [userin]))
            await asyncio.sleep(random.randrange(5, 7))
            await event.edit(f"`Prosess Menambahkan {n} Member...`")
        except TypeError:
            n -= 1
            continue
        except UserAlreadyParticipantError:
            n -= 1
            continue
        except UserPrivacyRestrictedError:
            n -= 1
            continue
        except UserNotMutualContactError:
            n -= 1
            continue


CMD_HELP.update({
    "scraper":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.getmemb`\
   \nUsage : Mengumpulkan Anggota dari Obrolan\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.addmemb`\
   \nUsage : Menambahkan Anggota ke Obrolan\
   \nTata Cara Menggunakannya:  Pertama, Anda harus melakukan .getmemb terlebih dahulu dari Obrolan. Lalu buka grup Anda dan ketik .addmemb untuk menambahkan mereka ke grup Anda."
})

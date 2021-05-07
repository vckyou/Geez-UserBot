import asyncio

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register
from platform import uname

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.deploy ?(.*)")
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 10

    animation_ttl = range(0, 22)

   # input_str = event.pattern_match.group(1)

    await event.edit("Deploying...")

    animation_chars = [

        "Heroku Connecting To Latest Github Build (Vckyou/Geez-UserBot)",
        f"Build started by user `{DEFAULTUSER}`",
        f"Deploy `535a74f0` by user `{DEFAULTUSER}`",
        "`Restarting Heroku Server...`",
        "State changed from up to starting...",
        "Stopping all processes with **SIGTERM**",
        "Process exited with `status 143`",
        "Starting process with command\n`[''python3'',''-m'',''userbot'']`",
        "State changed from starting to up...",
        "telethon.network.mtprotosender -\nINFO - Connecting to 91.108.56.170:443/TcpFull...",
        "telethon.network.mtprotosender -\nINFO - Connection to 91.108.56.170:443/TcpFull complete!",
        "telethon.network.mtprotosender -\nINFO - Disconnection from 91.108.56.146:443/TcpFull complete!",
        "telethon.network.mtprotosender -\nINFO - Disconnecting from 91.108.56.146:443/TcpFull...",
        "INFO - Modules to load :\n ['__help', 'admin', 'adzan', 'afk', 'allscrapers', 'android', 'anilist', 'animasi', 'anime', 'anti_spambot', 'antiflood', 'aria', 'ascii', 'bitly', 'blacklist', 'carbon', 'chat', 'coolprofilepics', 'covid', 'create', 'createstickers', 'dbs', 'deepfry', 'deezloader', 'detection', 'emojigames', 'eval', 'fakegban', 'federasi', 'figlet', 'filemanager', 'filter', 'games', 'gban', 'gcast', 'gdrive', 'get_user_id', 'getmusic', 'gid', 'gitcommit', 'github', 'glitcher', 'globalban', 'googlephotos', 'gps', 'hack', 'hash', 'help', 'hentai', 'herokuapp', 'igsaver', 'imgmemes', 'imp', 'kekuatan', 'geez', 'kenzogans', 'kenzogans24', 'lastfm', 'lock', 'lynxae', 'lynxhelper', 'lynxhz', 'lynxmemes', 'lynxmisc', 'lynxtt', 'lynxwc', 'lyrics', 'mega_downloads', 'memes', 'memify', 'mentions', 'messages', 'misc', 'nekobot', 'notes', 'offline', 'oi', 'phreaker', 'pms', 'profile', 'quotly', 'rastick', 'resi', 'reverse', 'salam', 'sangmata', 'santet', 'sed', 'snips', 'spam', 'spotifynow', 'ss_video', 'statme', 'stext', 'stickers', 'stickers_v2', 'system_stats', 'tag_all', 'telegraph', 'tempmail', 'time_date', 'tiny', 'torrentsearch', 'transform', 'updater', 'upload_download', 'waifu','transform', 'updater', 'upload_download', 'waifu', 'wallpaper', 'weather', 'webupload', 'welcomes', 'whois', 'www', 'xiaomi', 'zipfile']",
        "telethon.network.mtprotosender -\nINFO - Connecting to 91.108.56.146:443/TcpFull...",
        "telethon.network.mtprotosender -\nINFO - Connection to 91.108.56.146:443/TcpFull complete!",
        "telethon.network.mtprotosender -\nINFO - Received response without parent request",
        "INFO - Geez-Project: Logged in as 557667062",
        "INFO - Geez-Project: Successfully...",
        "919852+00:00 app[worker.1]: 919 - Geez-Project -",
        "INFO - ⚡ Geez-Project⚡ ⚙️ V5.0 [TELAH DIAKTIFKAN!]",
        "**Build Succeeded**"

    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 22])


CMD_HELP.update({
    "deploy": ": `.deploy`"
    "\n↳ : Untuk Deploy ke Heroku.. <Animasi> :v haha"})

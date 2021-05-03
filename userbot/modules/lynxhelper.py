""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Halo Yang Mulia {DEFAULTUSER} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/SyndicateTwenty4)"
        "\n[Repo](https://github.com/KENZO-404/Lynx-Userbot)"
        "\n[Instagram](instagram.com/si_axeell)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/KENZO-404/Lynx-Userbot/Lynx-Userbot/varshelper.txt)")


CMD_HELP.update({
    "lynxhelper":
    "`.lhelp`\
\nUsage: Bantuan Untuk Lynx-Userbot.\
\n`.vars`\
\nUsage: Melihat Daftar Vars."
})

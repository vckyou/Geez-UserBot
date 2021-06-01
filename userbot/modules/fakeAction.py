from userbot.events import register
from userbot import CMD_HELP
import asyncio

# Port By @VckyouuBitch From Geez-Projects


@register(outgoing=True, pattern="^.ftyping(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await ban_time(t)
            except BaseException:
                return await event.edit(f"`Incorrect Format`")
    await event.edit(f"`Starting Fake Typing For` {t} `sec.`")
    async with event.client.conversation(event.chat_id, "typing"):
        await asyncio.sleep(t)

CMD_HELP.update(
    {
        "fakeaction": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ftyping <jumlah text>`"
        "\n• : Fake typing ini Berfungsi dalam group"
    }
)

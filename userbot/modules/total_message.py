from userbot.events import register
from userbot import CMD_HELP, bot


# Port By @VckyouuBitch From GeezProject
# Untuk Siapapun Yang Hapus Credits Ini, Kamu Anjing:)
@register(outgoing=True, pattern=r"^\.tmsg (.*)")
async def _(event):
    k = await event.get_reply_message()
    if k:
        a = await event.client.get_messages(chat_id, 0, from_user=k.sender_id)
        return await event.edit(f"Total msgs of {u} here = {a.total}")
    u = event.pattern_match.group(1)
    if not u:
        u = "me"
    a = await event.client.get_messages(chat_id, 0, from_user=u)
    await event.edit(f'Total msgs of {u} here={a.total}")

CMD_HELP.update(
    {
        "totalmessage": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tmsg` | `.tmsg` <username>\
    \n↳ : Returns your total msg count in current chat Or Returns total msg count of user in current chat."
    }
)

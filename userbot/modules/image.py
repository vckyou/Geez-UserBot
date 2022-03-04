# Ported By VCKYOU @VckyouuBitch
# Credits © Geez-Project
# Ya gitu deh:')

from shutil import rmtree
from userbot.events import register
from userbot import CMD_HELP
from userbot.utils import googleimagesdownload


@register(outgoing=True, pattern="^.img (.*)")
async def img_sampler(event):
    """For .img command, search and return images matching the query."""
    await event.edit("`Sedang Mencari Gambar Yang Anda Cari...`")
    query = event.pattern_match.group(1)
    lim = findall(r"lim=\d+", query)
    try:
        lim = lim[0]
        lim = lim.replace("lim=", "")
        query = query.replace("lim=" + lim[0], "")
    except IndexError:
        lim = 15
    response = googleimagesdownload()

    # creating list of arguments
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory",
    }

    # passing the arguments to the function
    paths = response.download(arguments)
    lst = paths[0][query]
    await event.client.send_file(
        await event.client.get_input_entity(event.chat_id), lst
    )
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await event.delete()

CMD_HELP.update(
    {
        "img": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.img <search_query>`\
         \n↳ : Does an image search on Google and shows 5 images."
    }
)

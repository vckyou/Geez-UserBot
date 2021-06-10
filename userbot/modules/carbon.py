import os
import asyncio
from selenium import webdriver
from userbot.utils.tools import deEmojify
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote_plus
from userbot import CHROME_DRIVER, GOOGLE_CHROME_BIN, CMD_HELP
from userbot.events import register


CARBONLANG = "auto"


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return get_emoji_regexp().sub("", inputString)


@register(outgoing=True, pattern="^.carbon (.*)")
async def carbon_api(event):
    """A Wrapper for carbon.now.sh"""
    await event.edit("`Processing..`")
    CARBON = "https://carbon.now.sh/?l={lang}&code={code}"
    textx = await event.get_reply_message()
    pcode = event.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)
    pcode = deEmojify(pcode)
    code = quote_plus(pcode)
    await event.edit("`Carbonizing...\n25%`")
    if os.path.isfile("/root/userbot/.bin/carbon.png"):
        os.remove("/root/userbot/.bin/carbon.png")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "/root/userbot/.bin"}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path=CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    await event.edit("`Be Patient...\n50%`")
    download_path = "/root/userbot/.bin"
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_path},
    }
    driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()

    await event.edit("`Processing..\n75%`")

    await asyncio.sleep(2)
    await event.edit("`Processing Done...\n100%`")
    file = "/root/userbot/.bin/carbon.png"
    await event.edit("`Uploading..`")
    await event.client.send_file(
        event.chat_id,
        file,
        caption="Here's your carbon",
        force_document=True,
        reply_to=event.message.reply_to_msg_id,
    )
    os.remove("/root/userbot/.bin/carbon.png")
    driver.quit()

    await event.delete()


CMD_HELP.update({
    "carbon":
    "`.carbon`\
        \nUsage:reply or type."
})

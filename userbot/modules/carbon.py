import os
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote_plus
from userbot import CHROME_DRIVER, CHROME_BIN, CMD_HELP
from userbot.events import register


CARBONLANG = "auto"


@register(outgoing=True, pattern="^.crblang (.*)")
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
    geez = await event.edit("`Carbonizing...\n25%`")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path=CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    await geez.edit("`Be Patient...\n50%`")
    download_path = "./"
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

    await geez.edit("`Processing..\n75%`")

    await asyncio.sleep(2)
    await geez.edit("`Processing Done...\n100%`")
    file = "./carbon.png"
    await geez.edit("`Uploading..`")
    await event.client.send_file(
        event.chat_id,
        file,
        caption="Here's your carbon",
        force_document=True,
        reply_to=event.message.reply_to_msg_id,
    )
    os.remove("./carbon.png")
    driver.quit()

    await geez.delete()


CMD_HELP.update({
    "carbon":
    "`.carbon`value <values=1,2,3,4,5>\
        \nUsage:reply or type .carbon1 or 2,3,4,5 value and beautify your text."
})

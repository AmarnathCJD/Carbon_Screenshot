from telethon import TelegramClient, events
import sys, os

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

TOKEN = os.environ.get("TOKEN")
API_KEY = os.environ.get("API_KEY")
API_HASH = os.environ.get("API_HASH")

tbot = TelegramClient(None, API_KEY, API_HASH)

try:
 tbot.start(bot_token=TOKEN)
except:
 sys.exit()

CHROME = "/app/.apt/usr/bin/google-chrome"
WEBDRIVER = "/app/.chromedriver/bin/chromedriver"

@tbot.on(events.NewMessage(pattern="^/carbon ?(.*)"))
async def carbon(event):
 try:
    code = event.text.split(None, 1)[1]
    CARBON = "https://carbon.now.sh/?bg=rgba(239%2C40%2C44%2C1)&t=one-light&wt=none&l=application%2Ftypescript&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=2x&wm=false&code={code}"
    url = CARBON.format(code=code, lang="en")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = CHROME
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path=WEBDRIVER,
        options=chrome_options)
    print("k")
    driver.get(url)
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": "./"},
    }
    command_result = driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    await event.reply(file="carbon.png")
 except Exception as e:
  await event.reply(str(e))

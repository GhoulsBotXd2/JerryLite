from os import getenv
from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAOyJeHvMbg5tjuXkbUkDsYZCOnj8q9uyBkjA88f0XUp6s8VncoTW8wC0AsNpG1tzRK7YFB8q5tLaD4GljF0f_xz-woncfUpjv15p6g99q8bRA6rLB4BqK_ISyMOW37MhtBPLSIciZ1TGkze5NgpqPH8EoEFr566b0dZLCusz8Mx_vaMzXw8KHS4NFeKYzXSH6ywCiyFAKhbi4EfY6LiusTsfTwcvP_Ob7g0kxrpkuCLLE7B8M92sbqZmaGBQ6E1RCem0H5viozEKyUsf3u_o3HQX_dt9ElvYN7No6ia9H57cm1RwDztyHODUvDlEN6Dpc3hNYNpbc7wmgOuijCu3DlAAAAATslPdEA")
BOT_TOKEN = getenv("6192180909:AAFD3RuFOOBv3lOTswHQwWGHkViLilusmKE")
BOT_NAME = getenv("Uta")
BOT_USERNAME = getenv("UtaXDivaMusicBot")
ASSID = int(getenv("5287263697"))
ASSNAME = getenv("Uta The Diva")
ASSUSERNAME = getenv("UtaMusicAssistant")
BOT_ID = int(getenv("BOT_ID"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("mongodb+srv://musicrobot:musicrobot@cluster0.l54hfu9.mongodb.net/?retryWrites=true&w=majority")
API_ID = int(getenv("26019444"))
API_HASH = getenv("a308fac723905cdbd836414b18f3b3d6")
OWNER_ID = int(getenv("6046532356"))
UPDATE = getenv("UPDATE", "RealmBotUpdates")
SUPPORT = getenv("SUPPORT", "RealmBotSupport")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9999"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/f2a2d31f60a9e0f3dbe94.png")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5860097723 5925926828").split()))
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/2941b97ce13e2347bac8f.jpg")
OWNER_USERNAME = getenv("MonsterKatakuri")
IMG_1 = "https://te.legra.ph/file/7bc14726121586044b18b.jpg"

import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Bu dəyəri əldə edin my.telegram.org/apps
API_ID = int(getenv("API_ID", "24066716"))
API_HASH = getenv("API_HASH", "09e30e6e0b1a4c71e43a055979c51b3b")

# Tokeninizi Telegram-da @BotFather -dən əldə edin.
BOT_TOKEN = getenv("BOT_TOKEN", "5919471465:AAFtkb9ZADjzxEuk7bGcH1DsISbsRAVl_r8")

# Mongo URL-nizi buradan əldə edin cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://nesirovq1997:qadir1997@cluster0.pavador.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Botun fəaliyyətlərini qeyd etmək üçün qrupun chat id-si
LOGGER_ID = int(getenv("LOGGER_ID", "-1001877272331"))

# Bu dəyəri Telegram-da @oTo_Ro_BoT dan /id ilə əldə edin
OWNER_ID = int(getenv("OWNER_ID", "6184936428"))

## Heroku-da yerləşdirirsinizsə, bu dəyişənləri doldurun.
# Heroku tətbiqinizin adı
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Ondan alın http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Qadirnesirov/MusicOtoQadir",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Yuxarıdakı repozitorunuz özəldirsə, bu dəyişəni doldurun

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/otobotblog")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/aurachatpg")

# Əgər köməkçinin fasilədən sonra söhbətləri avtomatik tərk etməsini istəyirsinizsə, bunu Doğru olaraq təyin edin
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", None))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "5400"))
# Bu etimadnaməsini əldə edin https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "-1001995040571")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "-1001995040571")


# Pleylist trekini youtube, spotify, apple linklərindən əldə etmək üçün maksimum limit.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio və video fayl ölçüsü limiti (baytla)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Mb-ni bayta çevirmək üçün https://www.gbmb.org/mb-to-bytes yoxlayın


# Telegram-da @otosessionbot dan Pyrogram v2 Simli Sessiya Əldə Edin.
STRING1 = getenv("STRING_SESSION", "AgFvOpwApe558f6oLQ5sp9SLBSq-VyHAVaTCZaDtY1ArNivBjjjQyeFU0NIGc83Lis8EvxtwPiSdDzQQ93253oZ2BpjbP54kI8dha47DhCkzN9wQMFTprrbPdhCzLqJBY0JTCilVpXu0WANNZjBlNCLvuf_K8_YkOL8x5H3DGZ4vFtTLfRungMsAumOEKIrCFu8bqUYr2flXt7_J8n-Lejlb1vxPhbpdl-Nm_W398qQNdzc0sfJTg8t7_8V5ndad7TGki9hAc8FBGt5f4UNFLYrdEHio2w0kMLnyVcJnK0orr0xeWrYPMEHW76CtNQxVYplclazgq_iasnIk6OAgGajBS3aWYQAAAAFZvEdgAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/79d1c45a428cc6a37feca.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/9bb910b3dc29fb8a23d47.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/9bb910b3dc29fb8a23d47.jpg"
STATS_IMG_URL = "https://telegra.ph/file/9bb910b3dc29fb8a23d47.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/9bb910b3dc29fb8a23d47.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/9bb910b3dc29fb8a23d47.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/9bb910b3dc29fb8a23d47.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/9bb910b3dc29fb8a23d47.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/9bb910b3dc29fb8a23d47.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/9bb910b3dc29fb8a23d47.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/9bb910b3dc29fb8a23d47.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/9bb910b3dc29fb8a23d47.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://otobotblog", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://otobotsport", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
      

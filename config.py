import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()


API_ID = 21968859

API_HASH = "21a59d21687f01d448530ee88a26b1eb"

BOT_TOKEN = "8173984202:AAEikrxjAVqf0FQJHjveBs6ORfi5doVEr0A"

BOT_ID = 8173984202

BOT_USERNAME = "@BoaMusixbot"

OWNER_USERNAME = "@Veron_seller"

BOT_NAME = "˹𝐌𝐨𝐦𝐨𝐂𝐡𝐚𝐧 ꭙ 𝐌ᴜsɪᴄ˼™"

ASSUSERNAME = "@boaassistant"

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://thebiggestcomebackever:EREN1234@cluster0.7q7ri.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = 500000

LOGGER_ID = int(getenv("LOGGER_ID", "-1002485775078")) 

DISASTER_LOG = -1002485775078

OWNER_ID = 6356050482

SPECIAL_USER = 7774827065

HEROKU_APP_NAME = "vipppp"

HEROKU_API_KEY = "HRKU-3a48d735-445f-49c4-a6cf-fea438f945ef"

UPSTREAM_REPO = "https://github.com/paradox-zenu/test"

UPSTREAM_BRANCH = "master"

GIT_TOKEN = "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"

SUPPORT_CHANNEL = "https://t.me/VERON_BOTS"

SUPPORT_CHAT = "https://t.me/VERON_SUPPORTS"

AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = 9000

SPOTIFY_CLIENT_ID = "22b6125bfe224587b722d6815002db2b"

SPOTIFY_CLIENT_SECRET = "c9c63c6fbf2f467c8bc68624851e9773"

SERVER_PLAYLIST_LIMIT = 3000
PLAYLIST_FETCH_LIMIT = 25

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

SONG_DOWNLOAD_DURATION = 9999999
SONG_DOWNLOAD_DURATION_LIMIT = 9999999

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

STRING1 = getenv("STRING1", "BQGuXKQAYRQbjarXMlOZR1uzmNZqKPxYkiw4RZJUKp0VdkBCY8RX4JSsmo_q7gIf8qgW9mfu2pQUPbOkF4qQW9tBCluU-E25mjZIrkQL2FVAabypJcdpcoXD5XyaYblNjZ57t-MGi8cFVaCWAIod8liRRQNATZIOaIAJdgMyjZIIy0Kz0PFcuBXZtrLUyy39vWobIlSMJv8EXij2i7RzI6GM4cY3lc4mi_itO0W8KaMFg_6j_YWNWbx1YHpFidtKz_mm5v9sNLyu2ekyzSGx6TboIZkeOTKRJHb2Ajx6JbsQnLn_wxGbMaaoITWI0x0azWqClVwEQESJFz3m9Cd1JQHINpxUQwAAAAGxMMFeAA")
STRING2 = getenv("STRING2", None)
STRING3 = getenv("STRING3", None)
STRING4 = getenv("STRING4", None)
STRING5 = getenv("STRING5", None)
STRING6 = None
STRING7 = None


filter = filters.user()
BANNED_USERS = filter
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL =  "https://i.ibb.co/ZRr7RzhD/photo-2025-08-02-14-03-04-7533988479659671576.jpg"
PLAYLIST_IMG_URL = "https://i.ibb.co/ZRr7RzhD/photo-2025-08-02-14-03-04-7533988479659671576.jpg"
STATS_IMG_URL = "https://i.ibb.co/ZRr7RzhD/photo-2025-08-02-14-03-04-7533988479659671576.jpg"
TELEGRAM_AUDIO_URL = "https://i.ibb.co/ZRr7RzhD/photo-2025-08-02-14-03-04-7533988479659671576.jpg"
TELEGRAM_VIDEO_URL = "https://i.ibb.co/ZRr7RzhD/photo-2025-08-02-14-03-04-7533988479659671576.jpg"
STREAM_IMG_URL = "https://i.ibb.co/ZRr7RzhD/photo-2025-08-02-14-03-04-7533988479659671576.jpg"
SOUNCLOUD_IMG_URL = "https://i.ibb.co/ZRr7RzhD/photo-2025-08-02-14-03-04-7533988479659671576.jpg"
YOUTUBE_IMG_URL = "https://i.ibb.co/ZRr7RzhD/photo-2025-08-02-14-03-04-7533988479659671576.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://i.ibb.co/ZRr7RzhD/photo-2025-08-02-14-03-04-7533988479659671576.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://i.ibb.co/ZRr7RzhD/photo-2025-08-02-14-03-04-7533988479659671576.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://i.ibb.co/ZRr7RzhD/photo-2025-08-02-14-03-04-7533988479659671576.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

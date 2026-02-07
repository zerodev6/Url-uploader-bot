import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram API credentials
    APP_ID = ""
    API_HASH = ""
    BOT_TOKEN = ""
    BOT_USERNAME = "@"
    
    # Database
    DATABASE_URL = ""
    
    # Logging
    LOG_CHANNEL = ""
    
    # Owner
    OWNER_ID = ""
    
    # Session for user bot (if needed)
    SESSION_STR = os.environ.get("SESSION_STR", "")
    
    # Update channel
    UPDATE_CHANNEL = "https://t.me/zerodev2"
    DEVELOPER = "@Zeroboy216"
    BOTUSERNAME = "@U"
    
    # Download/Upload settings
    MAX_FILE_SIZE = 4 * 1024 * 1024 * 1024  # 4 GB
    SPEED_LIMIT = 500 * 1024 * 1024  # 500 MB/s (SUPER FAST!)
    CHUNK_SIZE = 2 * 1024 * 1024  # 2 MB chunks for maximum speed
    
    # Download directory
    DOWNLOAD_DIR = "downloads"
    
    # Torrent settings
    TORRENT_DOWNLOAD_PATH = "downloads/torrents"
    TORRENT_SEED_TIME = 0  # Don't seed after download
    
    # Welcome message
    START_MESSAGE = """ʜᴇʏ {name}**, 
ɪ ᴀᴍ ᴛʜᴇ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟ ᴀᴜᴛᴏ ᴜʀʟ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🚀
ɪ ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ᴍᴏᴠɪᴇs ᴀɴᴅ ᴍᴏʀᴇ — ᴊᴜsᴛ ᴘᴀsᴛᴇ ᴀ ᴜʀʟ ᴏʀ ᴀ ᴍᴀɢɴᴇᴛ/ᴛᴏʀʀᴇɴᴛ ✨"""
    HELP_MESSAGE = """
**Hᴏᴡ Tᴏ Usᴇ Tʜɪs Bᴏᴛ** 🤔
   
𖣔 Fɪʀsᴛ ɢᴏ ᴛᴏ ᴛʜᴇ /settings ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴇ ʙᴏᴛ ʙᴇʜᴀᴠɪᴏʀ ᴀs ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ.

𖣔 Sᴇɴᴅ ᴍᴇ ᴛʜᴇ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴛᴏ sᴀᴠᴇ ɪᴛ ᴘᴇʀᴍᴀɴᴇɴᴛʟʏ.

𖣔 **Sᴇɴᴅ ᴜʀʟ | Nᴇᴡ ɴᴀᴍᴇ.ᴍᴋᴠ**

𖣔 Sᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇsɪʀᴇᴅ ᴏᴘᴛɪᴏɴ.

𖣔 Usᴇ `/caption` ᴛᴏ sᴇᴛ ᴄᴀᴘᴛɪᴏɴ ᴀs Rᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ

"""
    ABOUT_MESSAGE ="""
╭───────────⍟
├📛 **Mʏ Nᴀᴍᴇ** : URL Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ
├📢 **Fʀᴀᴍᴇᴡᴏʀᴋ** : <a href=https://docs.pyrogram.org/>PʏʀᴏBʟᴀᴄᴋ 2.7.4</a>
├💮 **Lᴀɴɢᴜᴀɢᴇ** : <a href=https://www.python.org>Pʏᴛʜᴏɴ 3.13.7</a>
├💾 **Dᴀᴛᴀʙᴀsᴇ** : <a href=https://cloud.mongodb.com>MᴏɴɢᴏDB</a>
├🚨 **Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ** : <a href=https://t.me/zerodevsupport> Zᴇʀᴏ Sᴜᴘᴘᴏʀᴛ</a>
├🥏 **Cʜᴀɴɴᴇʟ** : <a href=https://t.me/zerodevbro> Zᴇʀᴏ Dᴇᴠ </a>
├👨‍💻 **Cʀᴇᴀᴛᴇʀ** :  @Zeroboy216
├🧬 **Bᴜɪʟᴅ Sᴛᴀᴛᴜs** :  ᴠ1.4 [ ꜱᴛᴀʙʟᴇ ]
╰───────────────⍟
"""

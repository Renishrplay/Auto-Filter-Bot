import re, logging
from os import environ
from Script import script

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

# Bot information
API_ID = environ.get('API_ID', '')
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
PORT = int(environ.get('PORT', '8080'))

# Bot pics
PICS = (environ.get('PICS', 'https://graph.org/file/1aabc32de4442dbc5a2a0.jpg https://graph.org/file/9458bd38633097021468e.jpg https://graph.org/file/b352b109ff6ab64a0dec5.jpg https://graph.org/file/1e58ec7e88373d43fe698.jpg https://graph.org/file/e29fe074270cda1833462.jpg https://graph.org/file/ce952c92d4c42fd588213.jpg https://graph.org/file/5ee19f028c4585af12b6c.jpg https://graph.org/file/41dfb4d472208520d0314.jpg https://graph.org/file/ca6de43379db0999546ad.jpg https://graph.org/file/2212ca8121a17edb5a2e7.jpg')).split()

# Bot Admins
ADMINS = environ.get('ADMINS', '')

# Channels
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '').split()]
AUTH_CHANNEL = [int(auth_channels) for auth_channels in environ.get('AUTH_CHANNEL', '').split()]
LOG_CHANNEL = environ.get('LOG_CHANNEL', '-1001986722664')    
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '')    
OPENAI_API = environ.get('OPENAI_API', '')

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "ANUSHKA")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://telegram.dog/Technical_Discussion_Group')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://telegram.dog/ANUSHKA_SEN_CHANNEL')
FILMS_LINK = environ.get('FILMS_LINK', 'https://telegram.dog/ANUSHKA_SEN_GROUP')

# Bot settings
AUTO_FILTER = is_enabled((environ.get('AUTO_FILTER', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK", "True"), True)
SHORTLINK = is_enabled((environ.get('SHORTLINK', "False")), False)
DELETE_TIME = int(environ.get('DELETE_TIME', 3600)) # Add time in seconds
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
WELCOME = is_enabled((environ.get('WELCOME', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
LINK_MODE = is_enabled(environ.get("LINK_MODE", "True"), True)
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 10))
LANGUAGES = [language.lower() for language in environ.get('LANGUAGES', 'english hindi telugu tamil kannada malayalam').split()]

# Other
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "mdiskshortner.link")
SHORTLINK_API = environ.get("SHORTLINK_API", "36f1ae74ba1aa01e5bd73bdd0bc22aa915443501")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = is_enabled(environ.get("IS_VERIFY", "False"), False)
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
TUTORIAL = environ.get("TUTORIAL", "https://t.me/jenna_movie/48")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/jenna_movie/48")
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]

# stream features vars
BIN_CHANNEL = environ.get("BIN_CHANNEL", LOG_CHANNEL)
URL = environ.get("URL", "")

# Your Telegram bot token.
BOT_TOKEN = "6400875825:AAFK6Pw_g1ZqC6kWWhMLe2gS8lKRMLSnA0Q"

# Telegram API ID and Hash. This is NOT your bot token and shouldn't be changed.
API_ID = 28665962
API_HASH = "d4808928e6432422874dc99b2c89da0d"

# Chat used for logging errors.
LOG_CHAT = -1001820588722


# Chat used for logging user actions (like buy, gift, etc).
ADMIN_CHAT = -1001820588722


# How many updates can be handled in parallel.
# Don't use high values for low-end servers.
WORKERS = 20

# Admins can access panel and add new materials to the bot.
ADMINS = [5703174005]

# Sudoers have full access to the server and can execute commands.
SUDOERS = [5703174005]

# All sudoers should be admins too
ADMINS.extend(SUDOERS)

GIFTERS = []
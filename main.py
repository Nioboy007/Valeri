from modules._config import TOKEN, bot, OWNER_ID
from modules._helpers import __load_modules

bot.start(bot_token=TOKEN)
if not OWNER_ID == 1833850637:
 exit(69) # huehue

__load_modules()

bot.run_until_disconnected()

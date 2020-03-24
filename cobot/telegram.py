from telegram.ext import Updater, CommandHandler

from cobot.bot import Bot
from cobot.questionnaire import Questionnaire


class Telegram:
    def __init__(self):
        self.token = None

        with open("secrets/token.txt") as f:
            self.token = f.readline()[:-1]

    def __call__(self):
        updater = Updater(self.token, use_context=True)

        updater.dispatcher.add_handler(CommandHandler("help", _Adapter("help")))
        updater.dispatcher.add_handler(CommandHandler("hello", _Adapter("hello")))
        updater.dispatcher.add_handler(CommandHandler("ask", Questionnaire()))

        print("Start polling.")
        updater.start_polling()
        updater.idle()


class _Adapter:
    """
    Restore the bot for every incoming message (per user).
    """

    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __call__(self, update, context):
        bot = Bot(update.message.from_user.first_name)

        # Dynamically call a predefined method.
        fun = getattr(bot, self.attr_name)
        ret = fun()

        update.message.reply_text(ret)

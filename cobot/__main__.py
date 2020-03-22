from telegram.ext import Updater, CommandHandler
from cobot.hello import Hello
from cobot.questionnaire import Questionnaire

if __name__ == "__main__":
    with open("secrets/token.txt") as f:
        token = f.readline()[:-1]

        updater = Updater(token, use_context=True)

        updater.dispatcher.add_handler(CommandHandler("hello", Hello()))
        updater.dispatcher.add_handler(CommandHandler("ask", Questionnaire()))

        updater.start_polling()
        updater.idle()

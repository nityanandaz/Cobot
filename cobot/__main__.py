import argparse
# import curses

from telegram.ext import Updater, CommandHandler

from cobot.hello import Hello
from cobot.questionnaire import Questionnaire


class Telegram:
    def __init__(self):
        self.token = None

        with open("secrets/token.txt") as f:
            self.token = f.readline()[:-1]

    def __call__(self):
        updater = Updater(self.token, use_context=True)

        updater.dispatcher.add_handler(CommandHandler("hello", Hello()))
        updater.dispatcher.add_handler(CommandHandler("ask", Questionnaire()))

        print("Start polling.")
        updater.start_polling()
        updater.idle()


class CLI:
    def __init__(self, username):
        self.username = username

    def __call__(self):
        print(self.username)


if __name__ == "__main__":
    # https://docs.python.org/3/library/argparse.html?highlight=namespace#module-argparse
    parser = argparse.ArgumentParser(
        prog="cobot",
        usage="Either start the telegram bot or the CLI.",
        description="Cobot - a COVID-19 helper.",
    )
    subparsers = parser.add_subparsers()

    # subcommand telegram
    telegram_parser = subparsers.add_parser("telegram", help="Start the telegram bot.")
    telegram_parser.add_argument(
        "--start", action="store_true", help="Flag for starting."
    )

    # subcommand cli
    cli_parser = subparsers.add_parser("cli", help="Start the CLI.")
    cli_parser.add_argument(
        "username", type=str, help="Your local username.",
    )

    # https://docs.python.org/3/library/argparse.html?highlight=namespace#argparse.Namespace
    args = vars(parser.parse_args())

    if args.get("start"):
        telegram = Telegram()
        telegram()
        exit()

    username = args.get("username")
    if username != None:
        cli = CLI(username)
        cli()
        exit()

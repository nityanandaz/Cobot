class Hello:
    def __call__(self, update, context):
        update.message.reply_text(
            "Hello {}".format(update.message.from_user.first_name)
        )

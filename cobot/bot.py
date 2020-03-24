class Bot:
    def __init__(self, username):
        # Talking to...
        self.username = username

    def help(self):
        return "I am here to help."

    def hello(self):
        return f"Hello there {self.username}."

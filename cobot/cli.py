import curses

# import itertools
# import functools
# import random
# import operator


def cli(username):
    cli = _CLI(username)
    curses.wrapper(cli)


class _CLI:
    def __init__(self, username):
        self.username = username

    def __call__(self, stdscr):
        # https://docs.python.org/3/howto/curses.html#curses-howto
        stdscr.clear()

        y = 0

        stdscr.addstr(y, 0, f"Hello there {self.username}.")

        stdscr.refresh()
        stdscr.getkey()

        return

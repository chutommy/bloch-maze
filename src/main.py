import os

# TODO: remove main file, unite ' and "

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from app import App

if __name__ == '__main__':
    App('config.json').run()

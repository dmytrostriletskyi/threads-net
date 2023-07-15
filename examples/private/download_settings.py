"""
Provide example of downloading settings for private Threads API.
"""
import os

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')


if __name__ == '__main__':
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)
    threads.download_settings(path='/Users/dmytrostriletskyi/projects/threads/settings.json')

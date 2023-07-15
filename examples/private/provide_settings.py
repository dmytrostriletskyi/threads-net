"""
Provide example of providing settings for private Threads API.
"""
import os

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')
INSTAGRAM_AUTH_TOKEN = os.environ.get('INSTAGRAM_AUTH_TOKEN')


if __name__ == '__main__':
    # Settings are specified as a dictionary.
    settings = {
        'authentication': {
            'token': INSTAGRAM_AUTH_TOKEN,
        },
        'timezone': {
            'offset': -14400,
        },
        'device': {
            'id': 'android-cb0d81d0e326cb42',
            'manufacturer': 'OnePlus',
            'model': 'ONEPLUS+A3010',
            'android_version': 25,
            'android_release': '7.1.1',
        }
    }

    threads = Threads(settings=settings, username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    # Settings are specified as a path to JSON file which was downloaded.
    threads = Threads(
        settings='/Users/dmytrostriletskyi/projects/threads/settings.json',
        username=INSTAGRAM_USERNAME,
        password=INSTAGRAM_PASSWORD,
    )

    # Settings are not specified.
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

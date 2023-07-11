"""
Provide example of creating and deleting a thread from private Threads API.
"""
import os
import json

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')


if __name__ == '__main__':
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    created_thread = threads.private_api.create_thread(
        caption='Hello, world!',
    )

    created_thread = threads.private_api.create_thread(
        caption='Hello, world!',
        url='https://www.youtube.com/watch?v=lc4qU6BakvE'
    )

    created_thread = threads.private_api.create_thread(
        caption='Hello, world!',
        image_url='https://raw.githubusercontent.com/dmytrostriletskyi/threads-net/main/assets/picture.png',
    )

    created_thread = threads.private_api.create_thread(
        caption='Hello, world!',
        image_url='/Users/dmytrostriletskyi/projects/threads/assets/picture.png',
    )

    created_thread = threads.private_api.create_thread(
        caption='Hello, world!',
        image_url='https://raw.githubusercontent.com/dmytrostriletskyi/threads-net/main/assets/picture.png',
        reply_to=3141055616164096839,
    )

    print(json.dumps(created_thread, indent=4))

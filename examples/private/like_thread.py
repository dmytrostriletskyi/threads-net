"""
Provide example of liking and unliking a thread from private Threads API.
"""
import os
import json

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')


if __name__ == '__main__':
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    liking = threads.private_api.like_thread(id=3141055616164096839)
    print(json.dumps(liking, indent=4))

    unliking = threads.private_api.unlike_thread(id=3141055616164096839)
    print(json.dumps(unliking, indent=4))

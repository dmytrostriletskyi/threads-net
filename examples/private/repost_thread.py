"""
Provide example of reposting and unreposting a thread from private Threads API.
"""
import os
import json

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')


if __name__ == '__main__':
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    reposting = threads.private_api.repost_thread(id=3141055616164096839)
    print(json.dumps(reposting, indent=4))

    unreposting = threads.private_api.unrepost_thread(id=3141055616164096839)
    print(json.dumps(unreposting, indent=4))

"""
Provide example of quoting a thread from private Threads API.
"""
import os
import json

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')


if __name__ == '__main__':
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    quoting = threads.private_api.quote_thread(id=3141055616164096839, caption='Hello, world!')
    print(json.dumps(quoting, indent=4))

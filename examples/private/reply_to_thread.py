"""
Provide example of replying a thread from private Threads API.
"""
import os
import json

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')


if __name__ == '__main__':
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    created_reply = threads.private_api.reply_to_thread(id=3141055616164096839, caption='Nice thread, by the way!')
    print(json.dumps(created_reply, indent=4))

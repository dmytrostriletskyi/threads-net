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

    created_thread = threads.private_api.create_thread(caption='Hello, world!')
    print(json.dumps(created_thread, indent=4))

    deletion = threads.private_api.delete_thread(id=3141055616164096839)
    print(json.dumps(deletion, indent=4))

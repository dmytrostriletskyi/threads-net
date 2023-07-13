"""
Provide example of blocking and unblocking a user from private Threads API.
"""
import os
import json

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')


if __name__ == '__main__':
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    blocking = threads.private_api.block_user(id=314216)
    print(json.dumps(blocking, indent=4))

    unblocking = threads.private_api.unblock_user(id=314216)
    print(json.dumps(unblocking, indent=4))

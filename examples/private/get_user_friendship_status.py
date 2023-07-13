"""
Provide example of getting a friendship status with a user from private Threads API.
"""
import os
import json

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')


if __name__ == '__main__':
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    friendship_status = threads.private_api.get_friendship_status(id=314216)
    print(json.dumps(friendship_status, indent=4))

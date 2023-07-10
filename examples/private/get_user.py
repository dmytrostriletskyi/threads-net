"""
Provide example of getting a user from private Threads API.
"""
import os
import json

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')


if __name__ == '__main__':
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    user_id = threads.private_api.get_user_id(username='zuck')
    print(user_id)

    user = threads.private_api.get_user(id=user_id)
    print(json.dumps(user, indent=4))

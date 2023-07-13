"""
Provide example of restricting and unrestricting a user from private Threads API.
"""
import os
import json

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')


if __name__ == '__main__':
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    restricting = threads.private_api.restrict_user(id=314216)
    print(json.dumps(restricting, indent=4))

    unrestricting = threads.private_api.unrestrict_user(id=314216)
    print(json.dumps(unrestricting, indent=4))

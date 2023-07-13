"""
Provide example of following and unfollowing a user from private Threads API.
"""
import os
import json

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')


if __name__ == '__main__':
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    following = threads.private_api.follow_user(id=314216)
    print(json.dumps(following, indent=4))

    unfollowing = threads.private_api.unfollow_user(id=314216)
    print(json.dumps(unfollowing, indent=4))

"""
Provide example of getting recommended users from private Threads API.
"""
import os
import json

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')


if __name__ == '__main__':
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    recommended_users = threads.private_api.get_recommended_users()
    print(json.dumps(recommended_users, indent=4))

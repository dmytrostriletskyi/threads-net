"""
Provide example of muting and unmuting a user from private Threads API.
"""
import os
import json

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')


if __name__ == '__main__':
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    muting = threads.private_api.mute_user(id=314216)
    print(json.dumps(muting, indent=4))

    unmuting = threads.private_api.unmute_user(id=314216)
    print(json.dumps(unmuting, indent=4))

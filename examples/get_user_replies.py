"""
Provide example of getting user's replies implementation.
"""
import os
import json

from threads import Threads


if __name__ == '__main__':
    threads = Threads()
    threads.load_settings('session.json')
    threads.login(os.environ.get('INSTAGRAM_USERNAME'), os.environ.get('INSTAGRAM_PASSWORD'))

    user_replies = threads.get_user_replies(id=314216)
    print(json.dumps(user_replies, indent=4))

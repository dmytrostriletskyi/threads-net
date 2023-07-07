"""
Provide example of getting a user's threads implementation.
"""
import os
import json

from threads import Threads


if __name__ == '__main__':
    threads = Threads()
    threads.load_settings('session.json')
    threads.login(os.environ.get('INSTAGRAM_USERNAME'), os.environ.get('INSTAGRAM_PASSWORD'))

    user_threads = threads.get_user_threads(id=314216)
    print(json.dumps(user_threads, indent=4))

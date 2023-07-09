"""
Provide example of getting a user implementation.
"""
import os
import json

from threads import Threads


if __name__ == '__main__':
    threads = Threads()
    threads.load_settings('session.json')
    threads.login(os.environ.get('INSTAGRAM_USERNAME'), os.environ.get('INSTAGRAM_PASSWORD'))

    user_id = threads.get_user_id(username='zuck')
    print(user_id)

    user = threads.get_user_by_id(id=user_id)
    print(json.dumps(user, indent=4))

"""
Provide example of getting a user's threads implementation.
"""
import json

from threads import Threads


if __name__ == '__main__':
    threads = Threads()

    # Get user threads by username
    user_threads = threads.get_user_threads('zuck')
    print(json.dumps(user_threads, indent=4))

    # Get user threads by user id
    user_threads = threads.get_user_threads(314216)
    print(json.dumps(user_threads, indent=4))

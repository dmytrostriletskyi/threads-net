"""
Provide example of getting user's replies implementation.
"""
import json

from threads import Threads


if __name__ == '__main__':
    threads = Threads()
    user_replies = threads.get_user_replies(id=314216)

    print(json.dumps(user_replies, indent=4))

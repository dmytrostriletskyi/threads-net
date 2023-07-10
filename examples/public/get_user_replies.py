"""
Provide example of getting user's replies from public Threads API.
"""
import json

from threads import Threads


if __name__ == '__main__':
    threads = Threads()

    user_replies = threads.public_api.get_user_replies(id=314216)
    print(json.dumps(user_replies, indent=4))

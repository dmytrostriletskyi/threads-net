"""
Provide example of getting a user's threads from public Threads API.
"""
import json

from threads import Threads


if __name__ == '__main__':
    threads = Threads()

    user_threads = threads.public_api.get_user_threads(id=314216)
    print(json.dumps(user_threads, indent=4))

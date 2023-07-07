"""
Provide example of getting a user implementation.
"""
import json

from threads import Threads


if __name__ == '__main__':
    threads = Threads()
    user = threads.get_user(id=314216)

    print(json.dumps(user, indent=4))

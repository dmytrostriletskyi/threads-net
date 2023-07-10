"""
Provide example of getting a user from public Threads API.
"""
import json

from threads import Threads


if __name__ == '__main__':
    threads = Threads()

    user_id = threads.public_api.get_user_id(username='zuck')
    print(user_id)

    user = threads.public_api.get_user(id=user_id)
    print(json.dumps(user, indent=4))

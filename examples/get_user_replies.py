"""
Provide example of getting user's replies implementation.
"""
import json

from threads import Threads


if __name__ == '__main__':
    threads = Threads()

    # get user's replies by username
    user_replies = threads.get_user_replies('zuck')
    print(json.dumps(user_replies, indent=4))

    # get user's replies by user id
    user_replies = threads.get_user_replies(314216) 
    print(json.dumps(user_replies, indent=4))
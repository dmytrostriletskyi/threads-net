"""
Provide example of getting a user's threads using pagination from private Threads API.
"""
import os

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')

if __name__ == '__main__':
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    from_max_id = None

    while True:
        user_threads = threads.private_api.get_user_threads(id=314216, limit=2, from_max_id=from_max_id)

        for thread in user_threads.get('threads'):
            items = thread.get('thread_items')

            for item in items:
                thread_id = item.get('post').get('pk')
                print(thread_id)

        from_max_id = user_threads.get('next_max_id')

        if from_max_id is None:
            break

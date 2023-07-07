"""
Provide example of getting a post implementation.
"""
import json
import os

from threads import Threads


if __name__ == '__main__':
    threads = Threads()
    threads.load_settings('session.json')
    threads.login(os.environ.get('INSTAGRAM_USERNAME'), os.environ.get('INSTAGRAM_PASSWORD'))

    post = threads.get_post(id=3141055616164096839)
    print(json.dumps(post, indent=4))

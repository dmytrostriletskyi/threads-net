"""
Provide example of making a login to Threads via Instagram implementation.
"""
import os

from threads import Threads


if __name__ == '__main__':
    threads = Threads()
    threads.login(os.environ.get('INSTAGRAM_USERNAME'), os.environ.get('INSTAGRAM_PASSWORD'))
    threads.dump_settings('session.json')

    threads = Threads()
    threads.load_settings('session.json')
    threads.login(os.environ.get('INSTAGRAM_USERNAME'), os.environ.get('INSTAGRAM_PASSWORD'))

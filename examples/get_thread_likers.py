"""
Provide example of getting a thread's likers implementation.
"""
import json

from threads import Threads


if __name__ == '__main__':
    threads = Threads()

    thread = threads.get_thread_likers(id=3141055616164096839)
    print(json.dumps(thread, indent=4))

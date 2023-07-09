"""
Provide example of getting a post's likers implementation.
"""
import json

from threads import Threads


if __name__ == '__main__':
    threads = Threads()

    post = threads.get_post_likers(id=3141055616164096839)
    print(json.dumps(post, indent=4))

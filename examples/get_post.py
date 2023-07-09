"""
Provide example of getting a post implementation.
"""
import json

from threads import Threads


if __name__ == '__main__':
    threads = Threads()

    post_id = threads.get_post_id(url_id='CuXFPIeLLod')
    print(post_id)

    post = threads.get_post(id=post_id)
    print(json.dumps(post, indent=4))

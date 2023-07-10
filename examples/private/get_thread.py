"""
Provide example of getting a thread from private Threads API.
"""
import os
import json

from threads import Threads

INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')


if __name__ == '__main__':
    threads = Threads(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)

    thread_id = threads.private_api.get_thread_id(url_id='CuXFPIeLLod')
    print(thread_id)

    thread = threads.private_api.get_thread(id=thread_id)
    print(json.dumps(thread, indent=4))

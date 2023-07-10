"""
Provide example of getting a thread from public Threads API.
"""
import json

from threads import Threads


if __name__ == '__main__':
    threads = Threads()

    thread_id = threads.public_api.get_thread_id(url_id='CuXFPIeLLod')
    print(thread_id)

    thread = threads.public_api.get_thread(id=thread_id)
    print(json.dumps(thread, indent=4))

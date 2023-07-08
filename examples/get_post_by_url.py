from threads import Threads
import requests
import json
import os

threads = Threads()
config = {
    'session_file_path': 'tmp/session.json',
}

if os.path.exists(config['session_file_path']): # If you have a session file
    print("Session file exists, loading...")
    threads.load_settings(config['session_file_path'])
    threads.login(os.environ.get('INSTAGRAM_USERNAME'),
                  os.environ.get('INSTAGRAM_PASSWORD'))
else: # If you don't have a session file
    print("Session file does not exist, creating...")
    print("More information: https://github.com/dmytrostriletskyi/threads-net#login")
    exit()

def find_post_id_url(url):
    """
    Retrieves the post ID from a given URL by making a GET request and parsing the response.

    Args:
        url (str): The URL of the post.

    Returns:
        str: The post ID.

    Raises:
        requests.exceptions.RequestException: If there was an error during the request.
        ValueError: If the post ID was not found in the response.

    """
    response = requests.get(url)
    response_text = response.text

    find_string = '{"post_id":"'
    start = response_text.find(find_string) + len(find_string)
    end = response_text.find('"}', start)

    if start == -1 or end == -1:
        raise ValueError("Post ID not found in the response.")

    post_id = response_text[start:end]
    return post_id

post_id = find_post_id_url('https://www.threads.net/t/CuZsgfWLyiI/')
print("Post ID: " + post_id)
post = threads.get_post(post_id)
print(json.dumps(post, indent=4))
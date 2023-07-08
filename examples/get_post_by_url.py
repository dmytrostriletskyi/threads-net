from threads import Threads
import requests
import json
import re
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

def get_post_id_from_url_re(post_url: str) -> str:
    """
    Retrieves the post ID from a given URL by making a GET request and parsing the response.

    Args:
        post_url (str): The URL of the post.

    Returns:
        str: The post ID.
    """
    response = requests.get(post_url)
    post_id = re.search(r'{"post_id":"(.*?)"}', response.text).group(1)
    return post_id if post_id else None

def  get_post_id_from_url(url) -> str:
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

# non-regex method
post_id = get_post_id_from_url('https://www.threads.net/t/CuZsgfWLyiI/')
# regex method
post_id_re = get_post_id_from_url_re('https://www.threads.net/t/CuZsgfWLyiI/')

print(f"{'No regex:':<10} {post_id}")
print(f"{'Regex':<10} {post_id_re}")
print(f"{'Equal:':<10} {post_id == post_id_re}")

print(json.dumps(threads.get_post(post_id), indent=4, sort_keys=True))
print(json.dumps(threads.get_post(post_id_re), indent=4, sort_keys=True))
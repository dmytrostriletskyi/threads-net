import requests
from threads import Threads

def find_user_by_username(username):
    # Construct the URL using the provided username
    url = f"https://www.instagram.com/{username}/"
    user_id = None
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response_text = response.text
        id_start_string = '"profilePage_'
        if id_start_string in response_text:
            # Extract the user ID from the response
            id_start = response_text.find(id_start_string) + len(id_start_string)
            id_end = response_text.find('"', id_start)
            user_id = int(response_text[id_start:id_end])
        else:
            pass  # User profile not found
    except Exception as e:
        print(f'{find_user_by_username.__name__} error: {e}')
    return user_id

if __name__ == '__main__':
    threads = Threads()

    # Find the user ID for the username 'threadsapp'
    user_id = find_user_by_username('threadsapp')

    # Get the user data using the retrieved user ID
    thread_user = threads.get_user(id=user_id)

    if thread_user['data'] is None:
        print("User data not found:", thread_user['errors'][0]['message'])
    else:
        user_data = thread_user['data']['userData']['user']

        selected_keys = [
            'full_name', 'biography',
            'is_private', 'is_verified',
            'follower_count', 'pk',
            'hd_profile_pic_versions'
        ]

        for key in selected_keys:
            user_data[key] = user_data[key]
            if isinstance(user_data[key], list):
                # Get the URL of the latest profile picture
                user_data[key] = user_data[key][-1]['url']
            print(f'{key:20}: {user_data[key]}')
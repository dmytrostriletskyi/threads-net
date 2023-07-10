"""
Provide implementation of abstract Threads API.
"""
import re

import requests


class AbstractThreadsApi:
    """
    Abstract API implementation.
    """

    def __init__(self):
        """
        Construct. the object.
        """
        self.fetch_html_headers = {
            'Authority': 'www.threads.net',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.threads.net',
            'Pragma': 'no-cache',
            'Referer': 'https://www.instagram.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
        }

    def get_user_id(self, username: str) -> int:
        """
        Get a user's identifier.

        Arguments:
            username (str): a user's username.

        Returns:
            The user's identifier as an integer.
        """
        response = requests.get(
            url=f'https://www.instagram.com/{username}',
            headers=self.fetch_html_headers,
        )

        user_id_key_value = re.search('"user_id":"(\d+)",', response.text).group()
        user_id = re.search('\d+', user_id_key_value).group()

        return int(user_id)

    def get_thread_id(self, url_id):
        """
        Get a thread' identifier by its URL's identifier.

        For instance, there is the URL — `https://www.threads.net/t/CuXFPIeLLod`.
        The URL's identifier would be `CuXFPIeLLod`.

        Args:
            url_id (str): a thread's URL identifier.

        Raises:
            ValueError: If the thread identifier has not been found.
        """
        response = requests.get(f'https://www.threads.net/t/{url_id}/')

        thread_id_start_key_position = response.text.find('{"post_id":"') + len('{"post_id":"')
        thread_id_end_key_position = response.text.find('"}', thread_id_start_key_position)

        if thread_id_start_key_position == -1 or thread_id_end_key_position == -1:
            raise ValueError(
                'Post identifier has not been found: '
                'please, create an issue — https://github.com/dmytrostriletskyi/threads-net/issues',
            )

        thread_id = int(response.text[thread_id_start_key_position:thread_id_end_key_position])
        return thread_id

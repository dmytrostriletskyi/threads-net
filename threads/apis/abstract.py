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
        Construct the object.
        """
        self.fetch_html_headers = {
            'Authority': 'www.threads.net',
            'Accept': (
                'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;'
                'q=0.8,application/signed-exchange;v=b3;q=0.7'
            ),
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
            'User-Agent': (
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
                'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'
            ),
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

        user_id_key_value = re.search('"user_id":"(\\d+)",', response.text).group()
        user_id = re.search('\\d+', user_id_key_value).group()

        return int(user_id)

    def get_thread_id(self, url_id: str) -> int:
        """
        Get a thread's identifier.

        `URL` identifier is a last part of a thread's URL. If the thread's URL is
        `https://www.threads.net/t/CuXFPIeLLod`, then it would be `CuXFPIeLLod`.

        Arguments:
            url_id (str): a thread's URL identifier.

        References:
            - https://github.com/dmytrostriletskyi/threads-net/pull/16#issuecomment-1627818886

        Returns:
            The thread's identifier as an integer.
        """
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'

        thread_id = 0

        for letter in url_id:
            thread_id = (thread_id * 64) + alphabet.index(letter)

        return thread_id

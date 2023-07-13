"""
Provide implementation of public Threads API.
"""
from __future__ import annotations

import json
import re

import requests

from threads.apis.abstract import AbstractThreadsApi


class PublicThreadsApi(AbstractThreadsApi):
    """
    Public Threads API implementation.

    Each unique API endpoint requires unique document ID which is just a constant predefined by API developers.
    """

    THREADS_API_URL = 'https://www.threads.net/api/graphql'

    def __init__(self: PublicThreadsApi) -> None:
        """
        Construct the object.
        """
        super().__init__()

        self.threads_api_token = self._get_threads_api_token()
        self.default_headers = {
            'Authority': 'www.threads.net',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.threads.net',
            'Pragma': 'no-cache',
            'Sec-Fetch-Site': 'same-origin',
            'X-ASBD-ID': '129477',
            'X-FB-LSD': self.threads_api_token,
            'X-IG-App-ID': '238260118697367',
        }

    def get_user_id(self: PublicThreadsApi, username: str) -> int:
        """
        Get a user's identifier.

        Arguments:
            username (str): a user's username.

        Returns:
            The user's identifier as an integer.
        """
        headers = self.fetch_html_headers | {
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

        response = requests.get(
            url=f'https://www.threads.net/@{username}',
            headers=headers,
        )

        user_id = re.search('"props":{"user_id":"(\\d+)"},', response.text).group(1)
        return int(user_id)

    def get_user(self: PublicThreadsApi, id: int) -> dict:
        """
        Get a user.

        Arguments:
            id (int): a user's identifier.

        Returns:
            The user as a dict.
        """
        headers = self.default_headers | {
            'X-FB-Friendly-Name': 'BarcelonaProfileRootQuery',
        }

        response = requests.post(
            url=self.THREADS_API_URL,
            headers=headers,
            data={
                'lsd': self.threads_api_token,
                'variables': json.dumps(
                    {
                        'userID': id,
                    },
                ),
                'doc_id': '23996318473300828',
            },
        )

        return response.json()

    def get_user_threads(self: PublicThreadsApi, id: int) -> dict:
        """
        Get a user's threads.

        Arguments:
            id (int): a user's identifier.

        Returns:
            The list of user's threads inside a dict.
        """
        headers = self.default_headers | {
            'X-FB-Friendly-Name': 'BarcelonaProfileThreadsTabQuery',
        }

        response = requests.post(
            url=self.THREADS_API_URL,
            headers=headers,
            data={
                'lsd': self.threads_api_token,
                'variables': json.dumps(
                    {
                        'userID': id,
                    },
                ),
                'doc_id': '6232751443445612',
            },
        )

        return response.json()

    def get_user_replies(self: PublicThreadsApi, id: int) -> dict:
        """
        Get a user's replies.

        Arguments:
            id (int): a user's identifier.

        Returns:
            The list of user's replies inside a dict.
        """
        headers = self.default_headers | {
            'X-FB-Friendly-Name': 'BarcelonaProfileRepliesTabQuery',
        }

        response = requests.post(
            url=self.THREADS_API_URL,
            headers=headers,
            data={
                'lsd': self.threads_api_token,
                'variables': json.dumps(
                    {
                        'userID': id,
                    },
                ),
                'doc_id': '6307072669391286',
            },
        )

        return response.json()

    def get_thread(self: PublicThreadsApi, id: int) -> dict:
        """
        Get a thread.

        Arguments:
            id (int): a thread's identifier.

        Returns:
            The thread as a dict.
        """
        headers = self.default_headers | {
            'X-FB-Friendly-Name': 'BarcelonaPostPageQuery',
        }

        response = requests.post(
            url=self.THREADS_API_URL,
            headers=headers,
            data={
                'lsd': self.threads_api_token,
                'variables': json.dumps(
                    {
                        'postID': id,
                    },
                ),
                'doc_id': '5587632691339264',
            },
        )

        return response.json()

    def get_thread_likers(self: PublicThreadsApi, id: int) -> dict:
        """
        Get a thread's likers.

        Arguments:
            id (int): a thread's identifier.

        Returns:
            The list of thread's likers inside a dict.
        """
        response = requests.post(
            url=self.THREADS_API_URL,
            headers=self.default_headers,
            data={
                'lsd': self.threads_api_token,
                'variables': json.dumps(
                    {
                        'mediaID': id,
                    },
                ),
                'doc_id': '9360915773983802',
            },
        )

        return response.json()

    def _get_threads_api_token(self: PublicThreadsApi) -> str:
        """
        Get a token for Threads API.

        It is called `lsd` internally and is required for any request.
        For anonymous users, it is just generated automatically from API's back-end and passed to front-end.

        Returns:
            The token for Threads API as a string.
        """
        response = requests.get(
            url='https://www.instagram.com/instagram',
            headers=self.fetch_html_headers,
        )

        token_key_value = re.search('LSD",\\[\\],{"token":"(.*?)"},\\d+\\]', response.text).group()
        token_key_value = token_key_value.replace('LSD",[],{"token":"', '')
        token = token_key_value.split('"')[0]

        return token

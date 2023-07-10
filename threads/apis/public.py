"""
Provide implementation of public Threads API.
"""
import requests
import json
import time
import re
from urllib.parse import quote

from threads.apis.abstract import AbstractThreadsApi
from threads.utils import generate_android_device_id


class PublicThreadsApi(AbstractThreadsApi):
    """
    Public Threads API implementation.

    Each unique API endpoint requires unique document ID which is just a constant predefined by API developers.
    """

    THREADS_API_URL = 'https://www.threads.net/api/graphql'

    def __init__(self):
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

    def _get_threads_api_token(self):
        """
        Get a token for Threads API.

        It is called `lsd` internally and is required for any request.
        For anonymous users, it is just generated automatically from API's back-end and passed to front-end.
        """
        response = requests.get(
            url=f'https://www.instagram.com/instagram',
            headers=self.fetch_html_headers,
        )

        token_key_value = re.search('LSD",\[\],{"token":"(.*?)"},\d+\]', response.text).group()
        token_key_value = token_key_value.replace('LSD",[],{"token":"', '')
        token = token_key_value.split('"')[0]

        return token

    def get_user(self, id: int):
        """
        Get a user.

        Arguments:
            id (int): a user's identifier.
        """
        headers = self.default_headers | {
            'X-FB-Friendly-Name': 'BarcelonaProfileRootQuery',
        }

        response = requests.post(
            url=self.THREADS_API_URL,
            headers=headers,
            data={
                'lsd': self.threads_api_token,
                'variables': json.dumps({
                    'userID': id,
                }),
                'doc_id': '23996318473300828',
            },
        )

        return response.json()

    def get_user_threads(self, id: int):
        """
        Get a user's threads.

        Arguments:
            id (int):
            a user's identifier.
        """
        headers = self.default_headers | {
            'X-FB-Friendly-Name': 'BarcelonaProfileThreadsTabQuery',
        }

        response = requests.post(
            url=self.THREADS_API_URL,
            headers=headers,
            data={
                'lsd': self.threads_api_token,
                'variables': json.dumps({
                    'userID': id,
                }),
                'doc_id': '6232751443445612',
            },
        )

        return response.json()

    def get_user_replies(self, id: int):
        """
        Get a user's replies.

        Arguments:
            id (int): a user's identifier.
        """
        headers = self.default_headers | {
            'X-FB-Friendly-Name': 'BarcelonaProfileRepliesTabQuery',
        }

        response = requests.post(
            url=self.THREADS_API_URL,
            headers=headers,
            data={
                'lsd': self.threads_api_token,
                'variables': json.dumps({
                    'userID': id,
                }),
                'doc_id': '6307072669391286',
            },
        )

        return response.json()

    def get_thread(self, id: int):
        """
        Get a thread.

        Arguments:
            id (int): a thread's identifier.
        """
        headers = self.default_headers | {
            'X-FB-Friendly-Name': 'BarcelonaPostPageQuery',
        }

        response = requests.post(
            url=self.THREADS_API_URL,
            headers=headers,
            data={
                'lsd': self.threads_api_token,
                'variables': json.dumps({
                    'postID': id,
                }),
                'doc_id': '5587632691339264',
            },
        )

        return response.json()

    def get_thread_likers(self, id: int):
        """
        Get a thread's likers.

        Arguments:
            id (int): a thread's identifier.
        """
        response = requests.post(
            url=self.THREADS_API_URL,
            headers=self.default_headers,
            data={
                'lsd': self.threads_api_token,
                'variables': json.dumps({
                    'mediaID': id,
                }),
                'doc_id': '9360915773983802',
            },
        )

        return response.json()

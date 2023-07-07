"""
Threads (threads.net) API wrapper implementation.
"""
import json

import requests


class Threads:
    """
    Threads (threads.net) API wrapper implementation.

    Each unique API endpoint requires unique document ID which is just a constant predefined by API developers.
    """

    API_URL = 'https://www.threads.net/api/graphql'

    def __init__(self):
        """
        Construct the object.
        """
        self.token = self._get_token()
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-IG-App-ID': '238260118697367',
            'X-FB-LSD': self.token,
            'Sec-Fetch-Site': 'same-origin',
        }

    def _get_token(self):
        """
        Get a token.

        It is called `lsd` internally and is required for any request.
        For anonymous users, it is just generated automatically from API's back-end and passed to front-end.
        """
        response = requests.get('https://www.threads.net/@instagram')

        token_key_position = response.text.find('\"token\"')
        token = response.text[token_key_position + 9:token_key_position + 31]

        return token

    def get_post(self, id: int):
        """
        Get a post.

        Arguments:
            id (int): a post's identifier.
        """
        response = requests.post(
            url=self.API_URL,
            headers=self.headers,
            data={
                'lsd': self.token,
                'variables': json.dumps({
                    'postID': id,
                }),
                'doc_id': '5587632691339264',
            },
        )

        return response.json()

    def get_user(self, id: int):
        """
        Get a user.

        Arguments:
            id (int): a user's identifier.
        """
        response = requests.post(
            url=self.API_URL,
            headers=self.headers,
            data={
                'lsd': self.token,
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
            id (int): a user's identifier.
        """
        response = requests.post(
            url=self.API_URL,
            headers=self.headers,
            data={
                'lsd': self.token,
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
        response = requests.post(
            url=self.API_URL,
            headers=self.headers,
            data={
                'lsd': self.token,
                'variables': json.dumps({
                    'userID': id,
                }),
                'doc_id': '6307072669391286',
            },
        )

        return response.json()

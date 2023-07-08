"""
Threads (threads.net) API wrapper implementation.
"""
import logging
import json
from urllib.parse import urlparse

import requests

from instagrapi.mixins.account import AccountMixin
from instagrapi.mixins.auth import LoginMixin
from instagrapi.mixins.bloks import BloksMixin
from instagrapi.mixins.challenge import ChallengeResolveMixin
from instagrapi.mixins.password import PasswordMixin
from instagrapi.mixins.private import PrivateRequestMixin
from instagrapi.mixins.public import (
    ProfilePublicMixin,
    PublicRequestMixin,
)
from instagrapi.mixins.user import UserMixin

DEFAULT_LOGGER = logging.getLogger('threads')


class Threads(
    PublicRequestMixin,
    ChallengeResolveMixin,
    PrivateRequestMixin,
    ProfilePublicMixin,
    LoginMixin,
    PasswordMixin,
    BloksMixin,
    UserMixin,
    AccountMixin,
):
    """
    Threads (threads.net) API wrapper implementation.

    Each unique API endpoint requires unique document ID which is just a constant predefined by API developers.
    """

    THREADS_API_URL = 'https://www.threads.net/api/graphql'

    def __init__(
        self,
        settings: dict = {},
        proxy: str = None,
        delay_range: list = None,
        logger=DEFAULT_LOGGER,
        **kwargs,
    ):
        """
        Construct the object.
        """
        super().__init__(**kwargs)

        self.settings = settings
        self.logger = logger
        self.delay_range = delay_range

        self.set_proxy(proxy)

        self.init()

        self.temporary_token = self._get_token()

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

    def get_user(self, username=None, id=None) -> dict:
        """
        Get a user.
        
        Arguments:
            username (str): a user's username.
            user_id (int): a user's identifier.
        """
        if not username and not id:
            raise ValueError('Either username or id must be specified.')

        if username:
            id = self.user_id_from_username(username)

        response = requests.post(
            url=self.THREADS_API_URL,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-IG-App-ID': '238260118697367',
                'X-FB-LSD': self.temporary_token,
                'Sec-Fetch-Site': 'same-origin',
            },
            data={
                'lsd': self.temporary_token,
                'variables': json.dumps({
                    'userID': id,
                }),
                'doc_id': '23996318473300828',
            }
        )

        return response.json()

    def get_user_threads(self, username=None, id: int = None) -> dict:
        """
        Get a user's threads.

        Arguments:
            username (str): a user's username.
            user_id (int): a user's identifier.
        """
        if not username and not id:
            raise ValueError('Either username or id must be specified.')
        
        if username:
            id = self.user_id_from_username(username)

        response = requests.post(
            url=self.THREADS_API_URL,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-IG-App-ID': '238260118697367',
                'X-FB-LSD': self.temporary_token,
                'Sec-Fetch-Site': 'same-origin',
            },
            data={
                'lsd': self.temporary_token,
                'variables': json.dumps({
                    'userID': id,
                }),
                'doc_id': '6232751443445612',
            },
        )

        return response.json()

    def get_user_replies(self, username=None, id: int = None):
        """
        Get a user's replies.

        Arguments:
            username (str): a user's username.
            user_id (int): a user's identifier.
        """
        if not username and not id:
            raise ValueError('Either username or id must be specified.')
        
        if username:
            id = self.user_id_from_username(username)

        response = requests.post(
            url=self.THREADS_API_URL,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-IG-App-ID': '238260118697367',
                'X-FB-LSD': self.temporary_token,
                'Sec-Fetch-Site': 'same-origin',
            },
            data={
                'lsd': self.temporary_token,
                'variables': json.dumps({
                    'userID': id,
                }),
                'doc_id': '6307072669391286',
            },
        )

        return response.json()

    def get_post(self, id: int) -> dict:
        """
        Get a post.

        Arguments:
            id (int): a post's identifier.
        """
        response = requests.post(
            url=self.THREADS_API_URL,
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-IG-App-ID': '238260118697367',
                'X-FB-LSD': self.temporary_token,
                'Sec-Fetch-Site': 'same-origin',
            },
            data={
                'lsd': self.temporary_token,
                'variables': json.dumps({
                    'postID': id,
                }),
                'doc_id': '5587632691339264',
            },
        )

        return response.json()

    def set_proxy(self, dsn: str):
        """
        Set a proxy.

        Copy-past code from the parent library.

        References:
            - https://github.com/adw0rd/instagrapi/blob/288803bdfbf60432143a474aa90aabdb7ba637e0/instagrapi/__init__.py#L112
        """
        if dsn:
            assert isinstance(
                dsn, str
            ), f'Proxy must been string (URL), but now "{dsn}" ({type(dsn)})'

            self.proxy = dsn

            proxy_href = "{scheme}{href}".format(
                scheme="http://" if not urlparse(self.proxy).scheme else "",
                href=self.proxy,
            )

            self.public.proxies = self.private.proxies = {
                "http": proxy_href,
                "https": proxy_href,
            }

            return True

        self.public.proxies = self.private.proxies = {}
        return False

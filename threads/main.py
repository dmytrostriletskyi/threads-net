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
            'X-FB-LSD': self.temporary_token,
            'X-IG-App-ID': '238260118697367',
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

    def get_user_id(self, username: str):
        """
        Get a user's identifier.

        Arguments:
            username (str): a user's username.
        """
        headers = self.default_headers | {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Referer': f'https://www.threads.net/@{username}',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
        }

        del headers['X-ASBD-ID']
        del headers['X-FB-LSD']
        del headers['X-IG-App-ID']

        response = requests.get(url=f'https://www.threads.net/@{username}')

        user_id_key_position = response.text.find('\"user_id\"')
        user_id = response.text[user_id_key_position + 11:user_id_key_position + 17]

        return user_id

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
                'lsd': self.temporary_token,
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
                'lsd': self.temporary_token,
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
                'lsd': self.temporary_token,
                'variables': json.dumps({
                    'userID': id,
                }),
                'doc_id': '6307072669391286',
            },
        )

        return response.json()

    def get_post_id(self, url_id):
        """
        Get a post' identifier by its URL's identifier.

        For instance, there is the URL — `https://www.threads.net/t/CuXFPIeLLod`.
        The URL's identifier would be `CuXFPIeLLod`.

        Args:
            url_id (str): a post's URL identifier.

        Raises:
            ValueError: If the ost identifier has not been found.
        """
        response = requests.get(f'https://www.threads.net/t/{url_id}/')

        post_id_start_key_position = response.text.find('{"post_id":"') + len('{"post_id":"')
        post_id_end_key_position = response.text.find('"}', post_id_start_key_position)

        if post_id_start_key_position == -1 or post_id_end_key_position == -1:
            raise ValueError(
                'Post identifier has not been found: '
                'please, create an issue — https://github.com/dmytrostriletskyi/threads-net/issues',
            )

        post_id = int(response.text[post_id_start_key_position:post_id_end_key_position])
        return post_id

    def get_post(self, id: int):
        """
        Get a post.

        Arguments:
            id (int): a post's identifier.
        """
        headers = self.default_headers | {
            'X-FB-Friendly-Name': 'BarcelonaPostPageQuery',
        }

        response = requests.post(
            url=self.THREADS_API_URL,
            headers=headers,
            data={
                'lsd': self.temporary_token,
                'variables': json.dumps({
                    'postID': id,
                }),
                'doc_id': '5587632691339264',
            },
        )

        return response.json()

    def get_post_likers(self, id: int):
        """
        Get a post's likers.

        Arguments:
            id (int): a post's identifier.
        """
        response = requests.post(
            url=self.THREADS_API_URL,
            headers=self.default_headers,
            data={
                'lsd': self.temporary_token,
                'variables': json.dumps({
                    'mediaID': id,
                }),
                'doc_id': '9360915773983802',
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

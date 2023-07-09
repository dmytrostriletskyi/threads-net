"""
Threads (threads.net) API wrapper implementation.
"""
import hashlib
import json
import time
import re
from urllib.parse import quote

import requests

from threads.auth import use_instagram_api_token


class Threads:
    """
    Threads (threads.net) API wrapper implementation.

    Each unique API endpoint requires unique document ID which is just a constant predefined by API developers.
    """

    THREADS_API_URL = 'https://www.threads.net/api/graphql'
    INSTAGRAM_API_URL = 'https://i.instagram.com/api/v1'

    def __init__(self, username: str = None, password: str = None):
        """
        Construct the object.
        """
        self.username = username
        self.password = password

        self.android_device_id = self._generate_android_device_id()
        self.timezone_offset = -14400

        self.threads_api_token = self._get_threads_api_token()
        self.instagram_api_token = None

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

    def _generate_android_device_id(self) -> str:
        """
        Generate Android device ID.
        """
        return 'android-%s' % hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]

    def _get_threads_api_token(self):
        """
        Get a token for Threads API.

        It is called `lsd` internally and is required for any request.
        For anonymous users, it is just generated automatically from API's back-end and passed to front-end.
        """
        response = requests.get('https://www.threads.net/@instagram')

        token_key_position = response.text.find('\"token\"')
        token = response.text[token_key_position + 9:token_key_position + 31]

        return token

    def _get_instagram_api_token(self):
        """
        Get a token for Instagram API.
        """
        block_version = '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73'

        parameters_as_string = json.dumps({
            'client_input_params': {
                'password': self.password,
                'contact_point': self.username,
                'device_id': self.android_device_id,
            },
            'server_params': {
                'credential_type': 'password',
                'device_id': self.android_device_id,
            },
        })

        bk_client_context_as_string = json.dumps({
            'bloks_version': block_version,
            'styles_id': 'instagram',
        })

        params = quote(string=parameters_as_string, safe="!~*'()")
        bk_client_context = quote(string=bk_client_context_as_string, safe="!~*'()")

        response = requests.post(
            url=f'{self.INSTAGRAM_API_URL}/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',
            headers={
                'User-Agent': 'Barcelona 289.0.0.77.109 Android',
                'Sec-Fetch-Site': 'same-origin',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            },
            data=f'params={params}&bk_client_context={bk_client_context}&bloks_versioning_id={block_version}'
        )

        bearer_key_position = response.text.find('Bearer IGT:2:')
        response_text = response.text[bearer_key_position:]

        backslash_key_position = response_text.find('\\\\')
        token = response_text[13:backslash_key_position]

        return token

    def get_user_id(self, username: str):
        """
        Get a user's identifier.

        Arguments:
            username (str): a user's username.
        """
        headers = self.default_headers | {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Referer': 'https://www.instagram.com',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
        }

        del headers['X-ASBD-ID']
        del headers['X-FB-LSD']
        del headers['X-IG-App-ID']

        response = requests.get(url=f'https://www.instagram.com/{username}')

        user_id_key_value = re.search('"user_id":"(\d+)",', response.text).group()
        user_id = re.search('\d+', user_id_key_value).group()

        return int(user_id)

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

    @use_instagram_api_token
    def create_thread(self, caption: str, instagram_api_token: str):
        """
        Create a thread.

        Arguments:
            caption (str) a thread's caption.
            instagram_api_token (str): an Instagram API's token.
        """
        current_timestamp = time.time()
        user_id = self.get_user_id(username=self.username)

        parameters_as_string = json.dumps({
            'publish_mode': 'text_post',
            'text_post_app_info': '{"reply_control":0}',
            'timezone_offset': str(self.timezone_offset),
            'source_type': '4',
            'caption': caption,
            '_uid': user_id,
            'device_id': self.android_device_id,
            'upload_id':  int(current_timestamp),
            'device': {
                'manufacturer': 'OnePlus',
                'model': 'ONEPLUS+A3010',
                'android_version': 25,
                'android_release': '7.1.1',
            }
        })

        encoded_parameters = quote(string=parameters_as_string, safe="!~*'()")

        response = requests.post(
            url=f'{self.INSTAGRAM_API_URL}/media/configure_text_only_post/',
            headers={
                'Authorization': f'Bearer IGT:2:{instagram_api_token}',
                'User-Agent': 'Barcelona 289.0.0.77.109 Android',
                'Sec-Fetch-Site': 'same-origin',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            },
            data=f'signed_body=SIGNATURE.{encoded_parameters}'
        )

        return response.json()

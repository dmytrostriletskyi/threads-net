"""
Provide implementation of private Threads API.
"""
import base64
import json
import mimetypes
import random
import time
from http import HTTPStatus as HttpStatus
from urllib.parse import quote
from uuid import uuid4

import requests
from Crypto.Cipher import (
    AES,
    PKCS1_v1_5,
)
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

from threads.apis.abstract import AbstractThreadsApi
from threads.utils import generate_android_device_id


class PrivateThreadsApi(AbstractThreadsApi):
    """
    Private Threads API implementation.
    """

    INSTAGRAM_API_URL = 'https://i.instagram.com/api/v1'

    def __init__(self, username: str = None, password: str = None):
        """
        Construct the object.

        Arguments:
            username (str): a user's Instagram username.
            password (str): a user's Instagram password.
        """
        super().__init__()

        self.username = username
        self.password = password

        self.timezone_offset = -14400
        self.android_device_id = generate_android_device_id()

        if self.username is not None and self.password is not None:
            self.instagram_public_key_id, self.instagram_public_key = self._get_instagram_public_key()
            self.encrypted_password, self.current_timestamp_as_string = self._encrypt_password(password=self.password)
            self.instagram_api_token = self._get_instagram_api_token()

            self.headers = {
                'Authorization': f'Bearer IGT:2:{self.instagram_api_token}',
                'User-Agent': 'Barcelona 289.0.0.77.109 Android',
                'Sec-Fetch-Site': 'same-origin',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            }

            self.user_id = self.get_user_id(username=username)

        self.mimetypes = mimetypes.MimeTypes()

    def get_user_id(self, username: str) -> int:
        """
        Get a user's identifier.

        Arguments:
            username (str): a user's username.

        Returns:
            The user's identifier as an integer.
        """
        response = requests.get(url=f'{self.INSTAGRAM_API_URL}/users/{username}/usernameinfo/', headers=self.headers)

        user_id_as_string = response.json().get('user').get('pk')
        user_id_as_int = int(user_id_as_string)

        return user_id_as_int

    def get_user(self, id: int) -> dict:
        """
        Get a user.

        Arguments:
            id (int): a user's identifier.

        Returns:
            The user as a dict.
        """
        response = requests.get(url=f'{self.INSTAGRAM_API_URL}/users/{id}/info/', headers=self.headers)
        return response.json()

    def search_user(self, query: str) -> dict:
        """
        Search for a user.

        Arguments:
            query (str): a search query.

        Returns:
            The list of found user inside a dict.
        """
        response = requests.get(
            url=f'{self.INSTAGRAM_API_URL}/users/search/?q={query}',
            headers=self.headers,
        )

        return response.json()

    def get_user_followers(self, id: int) -> dict:
        """
        Get a user's followers.

        Arguments:
            id (int): a user's identifier.

        Returns:
            The list of user's followers inside a dict.
        """
        response = requests.get(
            url=f'{self.INSTAGRAM_API_URL}/friendships/{id}/followers/',
            headers=self.headers,
        )

        return response.json()

    def get_user_following(self, id: int) -> dict:
        """
        Get a user's following.

        Arguments:
            id (int): a user's identifier.

        Returns:
            The list of user's following inside a dict.
        """
        response = requests.get(
            url=f'{self.INSTAGRAM_API_URL}/friendships/{id}/following/',
            headers=self.headers,
        )

        return response.json()

    def get_friendship_status(self, id: int) -> dict:
        """
        Get a friendship status with a user.

        Arguments:
            id (int): An identifier of a user to get friendship status with.

        Returns:
            The friendship status as a dict.
        """
        response = requests.get(
            url=f'{self.INSTAGRAM_API_URL}/friendships/show/{id}/',
            headers=self.headers,
        )

        return response.json()

    def follow_user(self, id: int) -> dict:
        """
        Follow a user.

        Arguments:
            id (int): a user's identifier.

        Returns:
            The following information as a dict.
        """
        response = requests.post(
            url=f'{self.INSTAGRAM_API_URL}/friendships/create/{id}/',
            headers=self.headers,
        )

        return response.json()

    def unfollow_user(self, id: int) -> dict:
        """
        Unfollow a user.

        Arguments:
            id (int): a user's identifier.

        Returns:
            The unfollowing information as a dict.
        """
        response = requests.post(
            url=f'{self.INSTAGRAM_API_URL}/friendships/destroy/{id}/',
            headers=self.headers,
        )

        return response.json()

    def get_thread(self, id: int) -> dict:
        """
        Get a thread.

        Arguments:
            id (int): a thread's identifier.

        Returns:
            The thread as a dict.
        """
        response = requests.get(
            url=f'{self.INSTAGRAM_API_URL}/text_feed/{id}/replies',
            headers=self.headers,
        )

        return response.json()

    def get_thread_likers(self, id: int) -> dict:
        """
        Get a thread's likers.

        Arguments:
            id (int): a thread's identifier.

        Returns:
            The list of thread's likers inside a dict.
        """
        response = requests.get(
            url=f'{self.INSTAGRAM_API_URL}/media/{id}_{self.user_id}/likers/',
            headers=self.headers,
        )

        return response.json()

    def create_thread(self, caption: str, url: str = None, image_url: str = None, reply_to: int = None) -> dict:
        """
        Create a thread.

        Arguments:
            caption (str): a thread's caption.
            url (str): a thread's attachment URL.
            image_url (str): an image's HTTP(S) URL or path to a file.
            reply_to (int): an identifier of a thread to reply to.

        Raises:
            ValueError: if provided image URL does not match required format

        Returns:
            The created thread as a dict.
        """
        current_timestamp = time.time()

        parameters_as_string = {
            'text_post_app_info': {
                'reply_control': 0,
            },
            'timezone_offset': str(self.timezone_offset),
            'source_type': '4',
            'caption': caption,
            '_uid': self.user_id,
            'device_id': self.android_device_id,
            'upload_id': int(current_timestamp),
            'device': {
                'manufacturer': 'OnePlus',
                'model': 'ONEPLUS+A3010',
                'android_version': 25,
                'android_release': '7.1.1',
            },
        }

        if reply_to is not None:
            parameters_as_string['text_post_app_info']['reply_id'] = reply_to

        if url is None and image_url is None:
            endpoint = '/media/configure_text_only_post/'
            parameters_as_string['publish_mode'] = 'text_post'

        elif url is not None and image_url is None:
            endpoint = '/media/configure_text_only_post/'
            parameters_as_string['publish_mode'] = 'text_post'
            parameters_as_string['text_post_app_info']['link_attachment_url'] = url

        elif url is None and image_url is not None:
            endpoint = '/media/configure_text_post_app_feed/'
            parameters_as_string['upload_id'] = self._upload_image(url=image_url)
            parameters_as_string['scene_capture_type'] = ''

        else:
            raise ValueError('Provided image URL does not match required format. Please, create GitHub issue')

        encoded_parameters = quote(string=json.dumps(obj=parameters_as_string), safe="!~*'()")

        response = requests.post(
            url=f'{self.INSTAGRAM_API_URL}{endpoint}',
            headers=self.headers,
            data=f'signed_body=SIGNATURE.{encoded_parameters}',
        )

        return response.json()

    def delete_thread(self, id: int) -> dict:
        """
        Delete a thread.

        Arguments:
            id (int): a thread's identifier.

        Returns:
            The deletion information as a dict.
        """
        response = requests.post(
            url=f'{self.INSTAGRAM_API_URL}/media/{id}_{self.user_id}/delete/?media_type=TEXT_POST',
            headers=self.headers,
        )

        return response.json()

    def like_thread(self, id: int) -> dict:
        """
        Like a thread.

        Arguments:
            id (int): a thread's identifier.

        Returns:
            The liking information as a dict.
        """
        response = requests.post(
            url=f'{self.INSTAGRAM_API_URL}/media/{id}_{self.user_id}/like/',
            headers=self.headers,
        )

        return response.json()

    def unlike_thread(self, id: int) -> dict:
        """
        Unlike a thread.

        Arguments:
            id (int): a thread's identifier.

        Returns:
            The unliking information as a dict.
        """
        response = requests.post(
            url=f'{self.INSTAGRAM_API_URL}/media/{id}_{self.user_id}/unlike/',
            headers=self.headers,
        )

        return response.json()

    def repost_thread(self, id: int) -> dict:
        """
        Repost a thread

        Arguments:
            id (int): a thread's identifier.

        Returns:
            The reposting information as a dict.
        """
        response = requests.post(
            url=f'{self.INSTAGRAM_API_URL}/repost/create_repost/',
            headers=self.headers,
            data=f'media_id={id}',
        )

        return response.json()

    def unrepost_thread(self, id: int) -> dict:
        """
        Undo a thread's repost.

        Arguments:
            id (int): a thread's identifier.

        Returns:
            The unreposting information as a dict.
        """
        response = requests.post(
            url=f'{self.INSTAGRAM_API_URL}/repost/delete_text_app_repost/',
            headers=self.headers,
            data=f'original_media_id={id}',
        )

        return response.json()

    def quote_thread(self, id: int, caption: str) -> dict:
        """
        Quote a thread.

        Arguments:
            id (int): a thread's identifier.
            caption (str): a quote's caption.

        Returns:
            The quoting information as a dict.
        """
        current_timestamp = time.time()

        parameters_as_string = {
            'publish_mode': 'text_post',
            'text_post_app_info': {
                'quoted_post_id': id,
                'reply_control': 0,
            },
            'timezone_offset': str(self.timezone_offset),
            'source_type': '4',
            'caption': caption,
            '_uid': self.user_id,
            'device_id': self.android_device_id,
            'upload_id': int(current_timestamp),
            'device': {
                'manufacturer': 'OnePlus',
                'model': 'ONEPLUS+A3010',
                'android_version': 25,
                'android_release': '7.1.1',
            },
        }

        encoded_parameters = quote(string=json.dumps(obj=parameters_as_string), safe="!~*'()")

        response = requests.post(
            url=f'{self.INSTAGRAM_API_URL}/media/configure_text_only_post/',
            headers=self.headers,
            data=f'signed_body=SIGNATURE.{encoded_parameters}',
        )

        return response.json()

    def _get_instagram_public_key(self) -> tuple[int, str]:
        """
        Get Instagram public key.

        Basically, those are used to encrypt a password to never transfer it over the network.

        Returns:
            The public key and its identifier as a tuple of an integer and string.
        """
        parameters_as_string = json.dumps(
            {
                'id': str(uuid4()),
            }
        )

        encoded_parameters = quote(string=parameters_as_string, safe="!~*'()")

        response = requests.post(
            url=f'{self.INSTAGRAM_API_URL}/qe/sync/',
            headers={
                'User-Agent': 'Barcelona 289.0.0.77.109 Android',
                'Sec-Fetch-Site': 'same-origin',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            },
            data=f'params={encoded_parameters}',
        )

        public_key_key_id = response.headers.get('ig-set-password-encryption-key-id')
        public_key = response.headers.get('ig-set-password-encryption-pub-key')

        return int(public_key_key_id), public_key

    def _encrypt_password(self, password) -> tuple[str, str]:
        """
        Encrypt a password.

        At some point, Instagram API changed they way the password is supplied. Basically, you now have two ways:

        Arguments:
            password (str): a Instagram password.

        1) First, you encrypt a secret key (basically, can be random sequence) with Instagram public key (which is
           used specifically for this procedure and retrieved from the API). Second, you encrypt a password with the
           secret key. Then you combine encrypted things and mix with initialization vector, auth tag and other things
           in one Base64 sequence. Third, this sequence is like your password where you prove it by encryptions where
           one of them is based on Instagram public API so your password never transferred publicly over the network.
        2) Just send a password publicly over the network (but requires little changes to the headers:
           password: '#PWD_INSTAGRAM_BROWSER:0:{timestamp_as_string}:plain_password'). Read more about it there:
           `https://stackoverflow.com/a/62524514`.

        Currently, the first way is chosen to align with other libraries approach.

        References:
            - https://github.com/junhoyeo/threads-api/blame/main/threads-api/src/threads-api.ts#L204
            - https://github.com/threadsjs/threads.js/blame/main/src/index.js#L53

        Returns:
            The password sequence and current timestamp as a tuple of strings.
        """
        password_as_bytes = password.encode('utf-8')

        current_timestamp = int(time.time())
        current_timestamp_as_string = str(current_timestamp).encode('utf-8')

        secret_key = get_random_bytes(32)
        initialization_vector = get_random_bytes(12)

        instagram_public_key_as_bytes = base64.b64decode(self.instagram_public_key)
        instagram_public_key = RSA.import_key(extern_key=instagram_public_key_as_bytes)

        cipher = PKCS1_v1_5.new(instagram_public_key)
        encrypted_secret_key = cipher.encrypt(secret_key)

        cipher = AES.new(secret_key, AES.MODE_GCM, nonce=initialization_vector)
        cipher.update(current_timestamp_as_string)
        encrypted_password, auth_tag = cipher.encrypt_and_digest(password_as_bytes)

        key_id_mixed_bytes = int(1).to_bytes(1, 'big') + self.instagram_public_key_id.to_bytes(1, 'big')
        encrypted_rsa_key_mixed_bytes = int(0).to_bytes(1, 'big') + int(1).to_bytes(1, 'big')

        password_as_encryption_sequence = (
            key_id_mixed_bytes
            + initialization_vector
            + encrypted_rsa_key_mixed_bytes
            + encrypted_secret_key
            + auth_tag
            + encrypted_password
        )

        password_as_encryption_sequence_as_base64 = base64.b64encode(
            s=password_as_encryption_sequence,
        ).decode('ascii')

        return password_as_encryption_sequence_as_base64, str(current_timestamp)

    def _get_instagram_api_token(self) -> str:
        """
        Get a token for Instagram API.

        Returns:
            The token for Instagram API as a string.
        """
        block_version = '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73'

        parameters_as_string = json.dumps(
            {
                'client_input_params': {
                    'password': f'#PWD_INSTAGRAM:4:{self.current_timestamp_as_string}:{self.encrypted_password}',
                    'contact_point': self.username,
                    'device_id': self.android_device_id,
                },
                'server_params': {
                    'credential_type': 'password',
                    'device_id': self.android_device_id,
                },
            }
        )

        bk_client_context_as_string = json.dumps(
            {
                'bloks_version': block_version,
                'styles_id': 'instagram',
            }
        )

        params = quote(string=parameters_as_string, safe="!~*'()")
        bk_client_context = quote(string=bk_client_context_as_string, safe="!~*'()")

        response = requests.post(
            url=f'{self.INSTAGRAM_API_URL}/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',
            headers={
                'User-Agent': 'Barcelona 289.0.0.77.109 Android',
                'Sec-Fetch-Site': 'same-origin',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            },
            data=f'params={params}&bk_client_context={bk_client_context}&bloks_versioning_id={block_version}',
        )

        bearer_key_position = response.text.find('Bearer IGT:2:')
        response_text = response.text[bearer_key_position:]

        backslash_key_position = response_text.find('\\\\')
        token = response_text[13:backslash_key_position]

        return token

    def _upload_image(self, url: str) -> int:
        """
        Upload an image.

        Arguments:
            url (str): an image's HTTP(S) URL or path to a file.

        Raises:
            ValueError: if provided image URL neither HTTP(S) URL nor file path.
            ValueError: if provided image could not be uploaded.
            ValueError: if image uploading has been failed.

        References:
            - https://github.com/adw0rd/instagrapi/blob/master/instagrapi/mixins/photo.py#L123
            - https://github.com/adw0rd/instagrapi/blob/master/instagrapi/mixins/photo.py#L99
            - https://github.com/junhoyeo/threads-api/blob/main/threads-api/src/threads-api.ts#L606

        Returns:
            An upload identifier as an integer.
        """
        random_number = random.randint(1000000000, 9999999999)

        upload_id = int(time.time())
        upload_name = f'{upload_id}_0_{random_number}'

        file_data = None
        file_length = None
        mime_type = 'image/jpeg'
        waterfall_id = str(uuid4())

        is_url = url.startswith('http')
        is_file_path = not url.startswith('http')

        if is_file_path:
            with open(url, 'rb') as file:
                file_data = file.read()
                file_length = len(file_data)

            mime_type = self.mimetypes.guess_type(url)[0]

        if is_url:
            response = requests.get(url, stream=True, timeout=2)
            response.raw.decode_content = True

            file_data = response.content
            file_length = len(response.content)

        if not is_file_path and not is_url:
            raise ValueError('Provided image URL neither HTTP(S) URL nor file path. Please, create GitHub issue')

        if file_data is None and file_length is None:
            raise ValueError('Provided image could not be uploaded. Please, create GitHub issue')

        parameters_as_string = {
            'media_type': 1,
            'upload_id': str(upload_id),
            'sticker_burnin_params': json.dumps([]),
            'image_compression': json.dumps(
                {
                    'lib_name': 'moz',
                    'lib_version': '3.1.m',
                    'quality': '80',
                }
            ),
            'xsharing_user_ids': json.dumps([]),
            'retry_context': json.dumps(
                {
                    'num_step_auto_retry': '0',
                    'num_reupload': '0',
                    'num_step_manual_retry': '0',
                }
            ),
            'IG-FB-Xpost-entry-point-v2': 'feed',
        }

        headers = self.headers | {
            'Accept-Encoding': 'gzip',
            'X-Instagram-Rupload-Params': json.dumps(parameters_as_string),
            'X_FB_PHOTO_WATERFALL_ID': waterfall_id,
            'X-Entity-Type': mime_type,
            'Offset': '0',
            'X-Entity-Name': upload_name,
            'X-Entity-Length': str(file_length),
            'Content-Type': 'application/octet-stream',
            'Content-Length': str(file_length),
        }

        response = requests.post(
            url=f'https://www.instagram.com/rupload_igphoto/{upload_name}',
            data=file_data,
            headers=headers,
        )

        if response.status_code != HttpStatus.OK:
            if file_data is None and file_length is None:
                raise ValueError('Image uploading has been failed. Please, create GitHub issue')

        return response.json().get('upload_id')

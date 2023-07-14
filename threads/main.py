"""
Threads (threads.net) API wrapper implementation.
"""
from __future__ import annotations

from typing import (
    Optional,
    Union,
)

from threads.apis import (
    PrivateThreadsApi,
    PublicThreadsApi,
)
from threads.settings import Settings


class Threads:
    """
    Threads (threads.net) API wrapper implementation.
    """

    def __init__(
        self: Threads,
        username: Optional[Union[dict, str]] = None,
        password: Optional[str] = None,
        settings: Optional[Union[dict, str]] = None,
    ) -> None:
        """
        Construct the object.

        Arguments:
            settings: (dict/str): a settings dictionary or a path to a JSON file.
            username (str): a user's Instagram username.
            password (str): a user's Instagram password.
        """
        self.username = username
        self.password = password

        self.settings = Settings(settings=settings)

        self.public_api = PublicThreadsApi()
        self.private_api = PrivateThreadsApi(settings=self.settings, username=username, password=password)

    def download_settings(self: Threads, path: str) -> None:
        """
        Download settings.

        Arguments:
            path (str): a path to a JSON file.
        """
        self.settings.download_settings(
            path=path,
            authentication_token=self.private_api.instagram_api_token,
        )

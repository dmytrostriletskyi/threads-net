"""
Threads (threads.net) API wrapper implementation.
"""
from __future__ import annotations

from typing import Optional

from threads.apis import (
    PrivateThreadsApi,
    PublicThreadsApi,
)


class Threads:
    """
    Threads (threads.net) API wrapper implementation.
    """

    def __init__(
        self: Threads,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ) -> None:
        """
        Construct the object.

        Arguments:
            username (str): a user's Instagram username.
            password (str): a user's Instagram password.
        """
        self.username = username
        self.password = password

        self.public_api = PublicThreadsApi()
        self.private_api = PrivateThreadsApi(username=username, password=password)

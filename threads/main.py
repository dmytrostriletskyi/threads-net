"""
Threads (threads.net) API wrapper implementation.
"""
from threads.apis import (
    PrivateThreadsApi,
    PublicThreadsApi,
)


class Threads:
    """
    Threads (threads.net) API wrapper implementation.
    """

    def __init__(self, username: str = None, password: str = None):
        """
        Construct the object.
        """
        self.username = username
        self.password = password

        self.public_api = PublicThreadsApi()
        self.private_api = PrivateThreadsApi(username=username, password=password)

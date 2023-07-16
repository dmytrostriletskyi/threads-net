"""
Provide example of creating and deleting a thread from private Threads API with using instagrapi authorization.
"""
import os
import json
import logging
from pathlib import Path
from dotenv import load_dotenv

from instagrapi import Client
from instagrapi.exceptions import LoginRequired
from threads import Threads


class INSTAGRAPI_MM:
    # From https://adw0rd.github.io/instagrapi/usage-guide/best-practices.html
    def __init__(self, login, password, proxy=None, filename_session='session_instagram.json'):
        self.__login = login
        self.__password = password
        self.__proxy = proxy
        self.__filename_session = filename_session
        self.__logger = logging.getLogger()

        self.__cl = Client(proxy=self.__proxy)
        self.__auth()

    @property
    def cl(self):
        return self.__cl

    def __auth(self):
        path_session = Path(self.__filename_session)
        session = self.cl.load_settings(path_session) if path_session.is_file() else None

        login_via_session = False
        login_via_pw = False

        if session:
            try:
                self.cl.set_settings(session)
                self.cl.login(self.__login, self.__password)

                # check if session is valid
                try:
                    self.cl.get_timeline_feed()
                except LoginRequired:
                    self.__logger.info("Session is invalid, need to login via username and password")

                    old_session = self.cl.get_settings()

                    # use the same device uuids across logins
                    self.cl.set_settings({})
                    self.cl.set_uuids(old_session["uuids"])

                    self.cl.login(self.__login, self.__password)
                login_via_session = True
            except Exception as e:
                self.__logger.info("Couldn't login user using session information: %s" % e)

        if not login_via_session:
            try:
                self.__logger.info("Attempting to login via username and password. username: %s" % self.__login)
                if self.cl.login(self.__login, self.__password):
                    login_via_pw = True
            except Exception as e:
                self.__logger.info("Couldn't login user using username and password: %s" % e)

        if not login_via_pw and not login_via_session:
            raise Exception("Couldn't login user with either password or session")

        self.cl.dump_settings(path_session)
        return self.cl


if __name__ == '__main__':
    load_dotenv()

    INSTAGRAM_USERNAME = os.environ.get('INSTAGRAM_USERNAME')
    INSTAGRAM_PASSWORD = os.environ.get('INSTAGRAM_PASSWORD')
    PROXY = os.environ.get('PROXY')  # http://username:password@ip:port

    instagram_api = INSTAGRAPI_MM(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, PROXY)

    if PROXY:
        os.environ['https_proxy'] = PROXY  # Set a proxy for the "requests" library

    threads = Threads(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, instagrapi_client=instagram_api.cl)

    created_thread = threads.private_api.create_thread(
        caption='Hello, world!',
    )

    print(json.dumps(created_thread, indent=4))

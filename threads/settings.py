from __future__ import annotations

import json
from typing import (
    Optional,
    Union,
)

from threads.utils import generate_android_device_id


class Settings:

    def __init__(self: Settings, settings: Optional[Union[dict, str]] = None) -> None:
        """
        Construct the object.

        Arguments:
            settings: (dict/str): a settings dictionary or a path to a JSON file.
        """
        self._are_provided = False

        self._authentication_token = None
        self._timezone_offset = -14400
        self._device_id = generate_android_device_id()
        self._device_manufacturer = 'OnePlus'
        self._device_model = 'ONEPLUS+A3010'
        self._device_android_version = 25
        self._device_android_release = '7.1.1'

        if settings is None:
            return

        self._are_provided = True

        if isinstance(settings, str):
            settings_as_file_path = settings

            with open(settings_as_file_path) as json_file:
                settings = json.load(json_file)

        self._authentication_token = settings.get('authentication').get('token')
        self._timezone_offset = settings.get('timezone').get('offset')
        self._device_id = settings.get('device').get('id')
        self._device_manufacturer = settings.get('device').get('manufacturer')
        self._device_model = settings.get('device').get('model')
        self._device_android_version = settings.get('device').get('android_version')
        self._device_android_release = settings.get('device').get('android_release')

    def download_settings(self: Settings, path: str, authentication_token: str) -> None:
        """
        Download settings.

        Arguments:
            path (str): a path to a JSON file.
            authentication_token (str): an authentication token.
        """
        settings = {
            'authentication': {
                'token': authentication_token,
            },
            'timezone': {
                'offset': self.timezone_offset,
            },
            'device': {
                'id': self.device_id,
                'manufacturer': self._device_manufacturer,
                'model': self._device_model,
                'android_version': self._device_android_version,
                'android_release': self._device_android_release,
            },
        }

        with open(path, 'w', encoding='utf-8') as settings_file:
            json.dump(settings, settings_file, ensure_ascii=False, indent=4)

    @property
    def are_provided(self: Settings) -> bool:
        """
        Check if settings were provided.

        Means checking if the class constructor have settings as None (so settings were not provided) or have settings
        as a dictionary or a path to a JSON file.

        It is done such a way because if settings were not provided, other layers such as the private API, should know
        if they need to fetch data on their on (e.g. authentication token) or not. If settings were not provided,
        other layers anyway use the settings with its default data for timezone and device. But they should care
        of things that do not have default data in settings (e.g. authentication token).

        Returns:
            True as a boolean if settings were provided.
            Otherwise, False as a boolean.
        """
        return self._are_provided

    @property
    def authentication_token(self: Settings) -> str:
        """
        Get an authentication token.

        Returns:
            The authentication token as None, if settings are not provided.
            Otherwise, The authentication token as string.
        """
        return self._authentication_token

    @property
    def timezone_offset(self: Settings) -> float:
        """
        Get a timezone offset.

        Returns:
            The timezone offset as a float.
        """
        return self._timezone_offset

    @property
    def device_id(self: Settings) -> str:
        """
        Get a device identifier.

        Returns:
            The device identifier. as a string.
        """
        return self._device_id

    @property
    def device_as_dict(self: Settings) -> dict:
        """
        Get a device information.

        Returns:
            The device information as a dict.
        """
        return {
            'manufacturer': self._device_manufacturer,
            'model': self._device_model,
            'android_version': self._device_android_version,
            'android_release': self._device_android_release,
        }

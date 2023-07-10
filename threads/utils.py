"""
Provide implementation of utils.
"""
import hashlib
import time


def generate_android_device_id() -> str:
    """
    Generate an Android device ID.

    Returns:
        The Android device ID as a string.
    """
    return 'android-%s' % hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]

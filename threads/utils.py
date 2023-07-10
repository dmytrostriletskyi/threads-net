"""
Provide implementation of utils.
"""
import hashlib
import time


def generate_android_device_id() -> str:
    """
    Generate Android device ID.
    """
    return 'android-%s' % hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]

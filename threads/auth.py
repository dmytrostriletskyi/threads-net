"""
Provide implementation of Threads authentication database.
"""
from functools import wraps


def use_instagram_api_token(method):
    """
    Use a token for Instagram API.

    Means that decorator function needs a token for Instagram API, but there is not sense to create tokens for each
    of the decorator functions, so we fetch it one time and then kinda cache in the `instagram_api_token` property.

    Arguments:
        method (function): a method that is wrapped with the decorator.

    Returns:
        A method decorator's wrapper as `method_`.
    """
    @wraps(method)
    def method_(*args, **kwargs):
        """
        Add a token for Instagram API to method arguments (last named argument).

        Arguments:
            *args (tuple): method's positional arguments.
            **kwargs (dict) method's named arguments.

        Returns:
            A result of the function call.
        """
        threads_class_object_ = args[0]

        if not threads_class_object_.instagram_api_token:
            threads_class_object_.instagram_api_token = threads_class_object_._get_instagram_api_token()

        kwargs['instagram_api_token'] = threads_class_object_.instagram_api_token
        return method(*args, **kwargs)

    return method_

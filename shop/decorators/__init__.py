from django.shortcuts import redirect
from functools import wraps


def only_authenticated(method):
    """ Decorator for class methods. Redirect to home if user is not authenticated"""

    @wraps(method)
    def wrapper(*args, **kwargs):
        request = kwargs.get('request') if 'request' in kwargs else args[1]

        if not request.user.is_authenticated:
            return redirect('app_main:login')

        return method(*args, **kwargs)
    return wrapper


def only_superuser(method):
    """ Decorator for class methods. Redirect to home if user is not superuser"""

    @wraps(method)
    def wrapper(*args, **kwargs):
        request = kwargs.get('request') if 'request' in kwargs else args[1]

        if not request.user.is_superuser:
            return redirect('app_main:index_view')

        return method(*args, **kwargs)

    return wrapper


def only_not_authenticated(method):
    """ Decorator for class methods. Redirect to profile if user is authenticated"""

    @wraps(method)
    def wrapper(*args, **kwargs):
        request = kwargs.get('request') if 'request' in kwargs else args[1]

        if request.user.is_authenticated:
            return redirect('app_profile:profile')

        return method(*args, **kwargs)
    return wrapper




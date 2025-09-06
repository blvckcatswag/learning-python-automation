from functools import wraps

def log_call(logger=print):

    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger(f"[call] {func.__name__} args={args} kwargs={kwargs}")
            result = func(*args, **kwargs)
            logger(f"[ret ] {func.__name__} -> {result}")
            return result
        return wrapper
    return deco





def catch_and_handle(handler=None, default=None, exc_types=(Exception,)):

    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exc_types as e:
                if handler is not None:
                    return handler(e)
                return default
        return wrapper
    return deco



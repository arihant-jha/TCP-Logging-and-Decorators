from functools import wraps

def log_args(function):
    @wraps(function)
    def wrapped_function(*args, **kwargs):
        print(f"Calling {function.__name__}(*{args}, **{kwargs})")
        result = function(*args, **kwargs)
        return result
    return wrapped_function

@log_args
def test1(a, b, c):
    return (a + b) / c

# Usage
test1(1, 9, 2)

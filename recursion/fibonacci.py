def memoize(func):
    cache = {}
    history = []

    def wrapper(*args):
        arg = args[0]
        if arg not in cache:
            cache[arg] = func(arg)
        history.append(arg)
        return cache[arg]

    return wrapper


@memoize
def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

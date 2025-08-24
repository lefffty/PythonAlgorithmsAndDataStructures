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
def factorial(num):
    if num <= 1:
        return num
    return num * factorial(num - 1)


fact = factorial
fact(10)
fact(5)
print(fact.__closure__[0].cell_contents)
print(fact.__closure__[2].cell_contents)

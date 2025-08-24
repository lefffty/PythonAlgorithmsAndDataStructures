from math import sqrt, floor


def get_prime_number():
    for number in range(7, 10**7):
        factors = []
        LOWER_BOUND = 2
        UPPER_BOUND = floor(sqrt(number)) + 1
        for factor in range(LOWER_BOUND, UPPER_BOUND):
            if number % factor == 0:
                factors.append(factor)
        if not factors:
            yield number

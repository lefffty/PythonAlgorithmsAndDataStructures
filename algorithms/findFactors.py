# from dataStructures.list import List
from math import sqrt


def findFactors(number: int) -> frozenset:
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number //= 2
    factor = 3
    maxFactor = sqrt(number)
    while (factor <= maxFactor):
        while number % factor == 0:
            factors.append(factor)
            number //= factor
            maxFactor = sqrt(number)
        factor += 2
    return frozenset(factors)


print(findFactors(126))
print(findFactors(64))
print(findFactors(1054))

def gcd(dividend: int, divisor: int):
    while divisor:
        r = dividend % divisor
        dividend = divisor
        divisor = r
    return dividend


print(gcd(4851, 3003))

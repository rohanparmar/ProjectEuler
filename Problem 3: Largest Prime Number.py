def isFactor(n, m):
    return n % m == 0


def isPrime(n):
    max_poss_fact = n // 2
    for i in range(2, max_poss_fact + 1):
        if (isFactor(n, i)):
            return False
    return True


def get_largest_prime_factors(n):
    factors = []
    max_poss_fact = n ** (0.5)

    for i in range(2, int(max_poss_fact) + 1):
        if isFactor(n, i) and isPrime(i):
            factors += i
    return factors[-1]


num = get_largest_prime_factors(13195)

print(num)
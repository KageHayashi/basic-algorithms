import math

### Returns a list of numbers that contains the 
### prime factors of a given number
def primeFactors(n):
    prime_factors = []

    # divide all the 2's out first
    while n % 2 == 0:
        prime_factors.append(2)
        n = n / 2

    # now n should be an odd number so we iterate at 2
    # and find all the numbers less than sqrt(n)
    # that can be evenly divide n
    for i in range(3, int(math.sqrt(n)), 2):
        while n % i == 0:
            prime_factors.append(int(i))
            n = n / i

    # at the end, if n is a prime and greater than 2
    # add n into the list
    if n > 2:
        prime_factors.append(int(n))

    return prime_factors

n = int(input())
print(primeFactors(n))
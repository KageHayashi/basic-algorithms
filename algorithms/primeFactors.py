import math

### Returns a list of numbers that contains the 
### prime factors of a given number
def primeFactors(n):
    prime_factors = []

    while n % 2 == 0:
        prime_factors.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)), 2):
        while n % i == 0:
            prime_factors.append(int(i))
            n = n / i

    if n > 2:
        prime_factors.append(int(n))

    return prime_factors

n = int(input())
print(primeFactors(n))
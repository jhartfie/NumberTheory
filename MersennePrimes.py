# A Mersenne prime is a prime number that is one less than a power of two, i.e., a prime number of the form 2^p - 1 where p is also a prime number.
# Mersenne primes are closely related to perfect numbers, as every even perfect number is derived from a Mersenne prime.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_mersenne_primes(limit):
    mersenne_primes = []
    p = 2
    while True:
        mersenne_number = 2**p - 1
        if mersenne_number > limit:
            break
        if is_prime(mersenne_number):
            mersenne_primes.append(mersenne_number)
        p += 1
    return mersenne_primes

# Example usage
limit = 10000
mersenne_primes = find_mersenne_primes(limit)
print("Mersenne primes up to", limit, "are:", mersenne_primes)

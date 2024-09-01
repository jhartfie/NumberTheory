# A prime number p is called a Sophie Germain prime if 2p + 1 is also prime. For example, 11 is a Sophie Germain prime because 2 × 11 + 1 = 23, which is also prime. These primes are named after the French mathematician Sophie Germain and are related to safe primes, which are of the form 2p + 1.

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n%2==0 or n<2:
        return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False
    return True

def is_sophie_germain_prime(p):
    return is_prime(p) and is_prime(2 * p + 1)

def find_sophie_germain_primes(limit):
    return [p for p in range(2, limit + 1) if is_sophie_germain_prime(p)]

# Example usage
limit = 1000
sophie_germain_primes = find_sophie_germain_primes(limit)
print("Sophie Germain primes up to", limit, "are:", sophie_germain_primes)

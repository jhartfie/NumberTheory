# Twin primes are pairs of primes that differ by two, like (3, 5) and (11, 13). The Twin Prime Conjecture posits that there are infinitely many twin primes, but this remains unproven.
# This concept is closely related to the distribution of primes and has implications for the structure of the prime number sequence.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(limit):
    twin_primes = []
    for p in range(2, limit - 1):
        if is_prime(p) and is_prime(p + 2):
            twin_primes.append((p, p + 2))
    return twin_primes

# Example usage
limit = 1000
twin_primes = find_twin_primes(limit)
print("Twin primes up to", limit, "are:", twin_primes)

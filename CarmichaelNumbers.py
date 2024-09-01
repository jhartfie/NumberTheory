# Carmichael numbers are composite numbers that satisfy Fermat's little theorem for all integer bases that are coprime to the number. These numbers are sometimes called "pseudoprimes" because they pass Fermat's primality test despite being composite.
# Carmichael numbers are important in cryptography and primality testing.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_carmichael_number(n):
    if is_prime(n) or n < 3:
        return False
    for b in range(2, n):
        if gcd(b, n) == 1:  # Check if b is coprime with n
            if pow(b, n-1, n) != 1:
                return False
    return True

def find_carmichael_numbers(limit):
    return [n for n in range(2, limit + 1) if is_carmichael_number(n)]

# Example usage
limit = 10000
carmichael_numbers = find_carmichael_numbers(limit)
print("Carmichael numbers up to", limit, "are:", carmichael_numbers)

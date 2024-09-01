def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_totient(n):
    count = sum(1 for k in range(1, n + 1) if gcd(n, k) == 1)
    return count

def find_totients(limit):
    return [(n, euler_totient(n)) for n in range(1, limit + 1)]

# Example usage
limit = 50
totients = find_totients(limit)
print("Euler's Totient function values up to", limit, "are:", totients)

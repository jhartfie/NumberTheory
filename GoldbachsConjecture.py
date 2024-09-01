# This famous unsolved problem in number theory states that every even integer greater than 2 can be expressed as the sum of two prime numbers. Despite being tested up to 4*10^18, it remains unproven.
# The conjecture has inspired a great deal of research in additive number theory.


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def goldbach_conjecture(limit):
    for n in range(4, limit + 1, 2):
        found = False
        for p in range(2, n):
            if is_prime(p) and is_prime(n - p):
                print(f"{n} = {p} + {n - p}")
                found = True
                break
        if not found: # haha this will never happen unless n > 4*10^18 miniminally
            print(f"Goldbach's conjecture fails at {n}")

# Example usage
limit = 100
goldbach_conjecture(limit)

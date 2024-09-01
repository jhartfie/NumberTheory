# This theorem states that every natural number can be represented as the sum of four integer squares. For example, 7 can be written as 7 = 4 + 1 + 1 + 1
# The theorem is an example of a broader class of problems in number theory related to expressing numbers as sums of powers.

import itertools

def lagrange_four_squares(n):
    for a in range(int(n**0.5) + 1):
        for b in range(int((n - a**2)**0.5) + 1):
            for c in range(int((n - a**2 - b**2)**0.5) + 1):
                d = int((n - a**2 - b**2 - c**2)**0.5)
                if a**2 + b**2 + c**2 + d**2 == n:
                    return (a, b, c, d)
    return None

def find_lagrange_solutions(limit):
    return {n: lagrange_four_squares(n) for n in range(1, limit + 1)}

# Example usage
limit = 50
lagrange_solutions = find_lagrange_solutions(limit)
for n, squares in lagrange_solutions.items():
    print(f"{n} can be expressed as the sum of squares: {squares}")

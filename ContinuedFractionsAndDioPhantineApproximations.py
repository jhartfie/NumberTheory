# Continued fractions provide a way to approximate irrational numbers and are closely related to the best rational approximations of those numbers. This ties into Diophantine approximations, which study how well numbers can be approximated by rational numbers.
# These topics are fundamental in understanding irrationality and transcendence.

from fractions import Fraction

def continued_fraction_approximation(x, n_terms):
    approx = Fraction(int(x))
    x -= int(x)
    for _ in range(n_terms):
        if x == 0:
            break
        x = 1 / x
        approx += int(x)
        x -= int(x)
    return approx

def diophantine_approximation(x, n_terms):
    return continued_fraction_approximation(x, n_terms)

# Example usage
x = 3.245
n_terms = 5
approx = diophantine_approximation(x, n_terms)
print(f"Diophantine approximation of {x} with {n_terms} terms is: {approx}")

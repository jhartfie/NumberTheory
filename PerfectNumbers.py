# A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself. For example, 6 is a perfect number because its divisors (excluding 6 itself) are 1, 2, and 3, and 1 + 2 + 3 = 6

def is_perfect_number(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def find_perfect_numbers(limit):
    return [i for i in range(1, limit + 1) if is_perfect_number(i)]

# Example usage
limit = 10000
perfect_numbers = find_perfect_numbers(limit)
print("Perfect numbers up to", limit, "are:", perfect_numbers)

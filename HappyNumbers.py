# A happy number is defined as a number which eventually reaches 1 when replaced by the sum of the square of each digit. If this process results in an endless cycle of numbers that does not include 1, the number is unhappy (or sad).

def is_happy_number(n):
    seen_numbers = set()
    
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    
    return n == 1

def find_happy_numbers(range_start, range_end):
    happy_numbers = []
    
    for i in range(range_start, range_end + 1):
        if is_happy_number(i):
            happy_numbers.append(i)
    
    return happy_numbers

# Example usage
range_start = 1
range_end = 100  # Adjust the range as needed
happy_numbers = find_happy_numbers(range_start, range_end)
print("Happy numbers in the range", range_start, "to", range_end, "are:")
print(happy_numbers)

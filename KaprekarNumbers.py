# A Kaprekar number is a non-negative integer n such that if you square it, and then split the square into two parts, the sum of those parts equals the original number n

def is_kaprekar_number(n):
    if n == 0:
        return True
    
    square = n * n
    square_str = str(square)
    len_n = len(str(n))
    
    # Splitting the square into two parts
    right_part = int(square_str[-len_n:]) if square_str[-len_n:] else 0
    left_part = int(square_str[:-len_n]) if square_str[:-len_n] else 0
    
    # Checking if the sum of the parts equals the original number
    return (left_part + right_part) == n

def find_kaprekar_numbers(range_start, range_end):
    kaprekar_numbers = []
    for i in range(range_start, range_end + 1):
        if is_kaprekar_number(i):
            kaprekar_numbers.append(i)
    return kaprekar_numbers

# Example usage
range_start = 1
range_end = 990000  # You can adjust this range as needed
kaprekar_numbers = find_kaprekar_numbers(range_start, range_end)
print("Kaprekar numbers in the range", range_start, "to", range_end, "are:")
print(kaprekar_numbers)


# def is_kaprekar_number(n):
#     if n == 0 or n == 1:
#         return True
    
#     square = n * n
#     digits = len(str(n))
    
#     # Calculate right and left parts without converting to strings
#     right_part = square % (10 ** digits)
#     left_part = square // (10 ** digits)
    
#     return (left_part + right_part) == n

# def find_kaprekar_numbers_optimized(range_start, range_end):
#     kaprekar_numbers = []
    
#     # Start from 1 if range_start is 0 to avoid unnecessary checks
#     range_start = max(range_start, 1)
    
#     # Iterate through odd numbers only
#     for i in range(range_start | 1, range_end + 1, 2):
#         if is_kaprekar_number(i):
#             kaprekar_numbers.append(i)
    
#     return kaprekar_numbers

# # Example usage
# range_start = 997097201428275
# range_end = 997097201428276  # Adjust to include larger ranges
# kaprekar_numbers = find_kaprekar_numbers_optimized(range_start, range_end)
# print("Kaprekar numbers in the range", range_start, "to", range_end, "are:")
# print(kaprekar_numbers)

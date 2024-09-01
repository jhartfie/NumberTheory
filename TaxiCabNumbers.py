# A Taxicab number (also known as a Hardy-Ramanujan number) is a number that can be expressed as the sum of two cubes in multiple distinct ways. The first Taxicab number is 1729.

def find_taxicab_numbers(limit):
    taxicab_numbers = {}
    
    # Iterate over possible pairs of integers (a, b)
    for a in range(1, int(limit**(1/3)) + 1):
        for b in range(a, int(limit**(1/3)) + 1):
            sum_of_cubes = a**3 + b**3
            
            if sum_of_cubes > limit:
                break
            
            # If this sum_of_cubes has already been found, it's a potential Taxicab number
            if sum_of_cubes in taxicab_numbers:
                taxicab_numbers[sum_of_cubes].append((a, b))
            else:
                taxicab_numbers[sum_of_cubes] = [(a, b)]
    
    # Filter out numbers that can be expressed as the sum of cubes in more than one way
    result = {num: pairs for num, pairs in taxicab_numbers.items() if len(pairs) > 1}
    
    return result

# Example usage
limit = 100000  # Adjust the limit to search for larger Taxicab numbers
taxicab_numbers = find_taxicab_numbers(limit)

for num, pairs in taxicab_numbers.items():
    print(f"{num} can be expressed as:")
    for pair in pairs:
        print(f"{pair[0]}^3 + {pair[1]}^3")


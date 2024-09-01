# Fermat numbers are of the form 𝐹 𝑛 = 2 2 𝑛 + 1 F n ​ =2 2 n +1. 
# These numbers are named after Pierre de Fermat, who conjectured that all such numbers are prime. However, it was later found that this conjecture is false; for example, 𝐹 5 F 5 ​ is not prime. 
# The study of Fermat numbers is interesting because of their properties and their connections to constructible polygons.
 
def fermat_number(n):
    return 2**(2**n) + 1

def find_fermat_numbers(limit):
    fermat_numbers = []
    n = 0
    while True:
        f_n = fermat_number(n)
        if f_n > limit:
            break
        fermat_numbers.append(f_n)
        n += 1
    return fermat_numbers

# Example usage
limit = 100000
fermat_numbers = find_fermat_numbers(limit)
print("Fermat numbers up to", limit, "are:", fermat_numbers)

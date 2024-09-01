# The partition function, denoted as p(n) is a function in number theory that gives the number of distinct ways of representing n as a sum of positive integers, without considering the order of the summands. For example, p(4)=5 because 4 can be written as: 4, 3+1, 2+2, 2+1+1, 1+1+1+1

def partition(n, max_value=None):
    if n == 0:
        return [[]]
    if max_value is None:
        max_value = n

    result = []
    for i in range(min(n, max_value), 0, -1):
        for p in partition(n - i, i):
            result.append([i] + p)
    return result

def print_partitions(partitions):
    for idx, p in enumerate(partitions, 1):
        print(f"{idx}.) " + " + ".join(map(str, p)))

# Example usage
n = 10
partitions = partition(n)
print(f"Number of partitions for {n}: {len(partitions)}")
print("Partitions are:")
print_partitions(partitions)

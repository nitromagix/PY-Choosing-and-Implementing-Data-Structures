import numpy as np
a = np.array([1, 2, 3, 4])

print(a)

def print_one_per_line(arr):
    for item in arr:
        print(item)

print_one_per_line(a)


def sum_of_array(arr):
    sum = 0
    for item in arr:
        sum += item
    return sum

print(sum_of_array(a))

def mulitply_by_three(arr):
    return np.array(list(map(lambda x: x * x, arr)))

m = mulitply_by_three(a)
print(m)

print_one_per_line(m)
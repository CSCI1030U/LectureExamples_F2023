# 09a - Algorithms

# Coding Exercise 09a.1

'''
INSERT-SORT(A)
1  for j = 2 to length[A] do
2     key = A[j]
3     i = j-1
4     while i > 0 and A[i] > key do
5        A[i+1] = A[i]
6        i = i-1
7     A[i+1] = key
'''
def reverse_insertion_sort(a):
    for j in range(len(a) - 2, -1, -1):
        key = a[j]
        i = j + 1
        while i < len(a) and a[i] < key:
            a[i - 1] = a[i]
            i += 1
        a[i - 1] = key
    return a

print(f'{reverse_insertion_sort([3,5,2,4,1]) = }')
print(f'{reverse_insertion_sort([5,-3,2,-1,-4]) = }')
print(f'{reverse_insertion_sort([5,-3,2,-1,100000]) = }')
print(f'{reverse_insertion_sort([5,-2]) = }')
print(f'{reverse_insertion_sort([-2]) = }')
print(f'{reverse_insertion_sort([]) = }')

# Coding Exercise 09a.2

# linear (n - O(n))
def sequential_search(values, to_find):
    op_count = 0

    # op_count += 1
    # if len(values) == 0:
    #     return False, op_count

    for i in range(len(values)):
        op_count += 1
        if values[i] == to_find:
            return True, op_count
    return False, op_count

print(f'{sequential_search([5,2,4,1,3], -1)}')

import random 

for size in [10000, 20000, 30000, 40000, 50000]:
    values = list(range(size))
    random.shuffle(values)
    was_found, compare_count = sequential_search(values, -1)
    # print(f'{size} {compare_count}')
    print(f'{size:06d}' + '*' * (compare_count//1000))


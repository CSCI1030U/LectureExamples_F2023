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
'''
[1 2 5 | 3 4]
     ^     ^
     j     i
'''
def mirror_insertion_sort(a):
    for j in range(len(a) - 2, -1, -1):
        key = a[j]
        i = j + 1
        while i < len(a) and a[i] < key:
            a[i - 1] = a[i]
            i += 1
        a[i - 1] = key 
    return a

print(f'{mirror_insertion_sort([5,2,4,1,3]) = }')
print(f'{mirror_insertion_sort([1,2,3,4,5]) = }')
print(f'{mirror_insertion_sort([5,4,3,2,1]) = }')
print(f'{mirror_insertion_sort([]) = }')
print(f'{mirror_insertion_sort([-1]) = }')

# Coding Exercise 09a.2

def sequential_search(values, to_find):
    comparison_count = 0
    for i in range(len(values)):
        comparison_count += 1
        if values[i] == to_find:
            return True, comparison_count
    return False, comparison_count

# print(f'{sequential_search([5,2,4,1,3], -1) = }')

for size in [10,100,1000,10000]:
    values = list(range(size))
    result, comp_count = sequential_search(values, -1) 
    print(f'{size:06d}:', '*' * (comp_count//100))

# 09b Algorithm Strategies

# Coding Exercise 09b.1

def d_and_c_search(values, to_find):
    # base cases
    if len(values) == 0:
        return False

    if len(values) == 1:
        return to_find == values[0]

    # divide the problem into two
    first_half = values[0:len(values)//2]
    second_half = values[len(values)//2:]

    # solve each of the smaller problems (recursively)
    first_half_result = d_and_c_search(first_half, to_find)
    second_half_result = d_and_c_search(second_half, to_find)

    # combine the two solutions
    return first_half_result or second_half_result

print(f'{d_and_c_search([4,1,5,2,3], -1) = }')
print(f'{d_and_c_search([4,1,5,2,3], 3) = }')

# Coding Exercise 09b.2


def reverse_insertion_sort_tuple_by_fourth(a):
    '''
    Sorts a list of tuples using the 4th element 
    in that tuple as the key.  The list of sorted
    in reverse order.
    '''
    for j in range(len(a) - 2, -1, -1):
        key = a[j]
        i = j + 1
        while i < len(a) and a[i][3] > key[3]:
            a[i - 1] = a[i]
            i += 1
        a[i - 1] = key

def knapsack_greedy(items_available, max_weight):
    # calculate the value/weight ratio of all items 
    value_to_weight = []
    for item in items_available:
        value_to_weight.append((item[0], item[1], item[2], item[2]/item[1]))

    # sort the items by their ratio (descending)
    reverse_insertion_sort_tuple_by_fourth(value_to_weight)

    # one at a time, choose items in ratio order
    available_weight = max_weight
    selected_items = []
    for item in value_to_weight:
        if item[1] < available_weight:
            # take the entire item 
            selected_items.append(item)
            available_weight -= item[1]
        else:
            desired_weight = available_weight
            fractional_value = item[3] * desired_weight
            selected_items.append((item[0], desired_weight, fractional_value, item[3]))
            available_weight = 0
            break 
    return selected_items

items = [
    # name, weight, value
    ('Wooden Sculpture', 2.0, 3.5),
    ('Silver Earrings', 1.0, 150.0),
    ('Diamond Necklace', 1.0, 750.0),
    ('Stone Statue', 45.0, 8.5),
    ('Gold Bracelet', 5.0, 275.0)
]
print(f'{knapsack_greedy(items, 8.5) = }')


# Coding Exercise 09b.3

'''
FIBONACCI-DP(n)
1. solns = [0, 1]
2. if n < 2 then
3.    return solns[n]
4. for i = 2 to n do
5.    append (solns[i-1] + solns[i-2]) to solns
6. return solns[n]
'''
def fib_dp(n):
    solutions = [0, 1]
    # base case
    if n < 2:
        return solutions[n]
    
    for i in range(2, n + 1):
        solutions.append(solutions[i - 1] + solutions[i - 2])
    
    return solutions[n]

print(f'{fib_dp(80) = }')
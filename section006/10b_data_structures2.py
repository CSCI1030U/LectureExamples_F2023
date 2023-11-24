# 10b - Advanced Data Structures

# Coding Exercise 10b.1
class Binary_Search_Tree:
    def __init__(self, values):
        self._values = values[:]

    def parent_index(self, index):
        return (index - 1) // 2

    def left_child_index(self, index):
        return (index * 2) + 1
    
    def right_child_index(self, index):
        return (index * 2) + 2
    
    def _is_valid_index(self, index):
        return index >= 0 and index < len(self._values)

    def search(self, to_find, index_to_search = 0):
        if not self._is_valid_index(index_to_search):
            return False 
        
        if to_find == self._values[index_to_search]:
            return True
        elif to_find < self._values[index_to_search]:
            return self.search(to_find, self.left_child_index(index_to_search))
        else:
            return self.search(to_find, self.right_child_index(index_to_search))

    # this version prints the tree on its side (don't strain your neck)
    def print(self, depth=0, index=0):
        if not self._is_valid_index(index):
            return
        
        # right subtree
        self.print(depth + 1, self.right_child_index(index))

        # node value
        print('\t' * depth + str(self._values[index]))

        # left subtree
        self.print(depth + 1, self.left_child_index(index))


'''
            4
    1               8
-2      3       6       8
'''
vals = [4,1,8,-2,3,6,8]
bst = Binary_Search_Tree(vals)
# print(f'The parent of {vals[3]} is at {vals[bst.parent_index(3)]}')

values = [7, 3, 12, 1, 5, 9, 14]
bst = Binary_Search_Tree(values=values)
index = 1
pindex = bst.parent_index(index)
lindex = bst.left_child_index(index)
rindex = bst.right_child_index(index)
print(f'parent is at index {pindex}, value: {values[pindex]}')
print(f'left child is at index {lindex}, value: {values[lindex]}')
print(f'right child is at index {rindex}, value: {values[rindex]}')
print(f'{bst.search(14) = }')
print(f'{bst.search(7) = }')
print(f'{bst.search(-2) = }')
bst.print()
# 10b - Advanced Data Structures

# Coding Exercise 10b.1 and 10b.2

class Binary_Search_Tree:
    def __init__(self, values):
        self._values = values 
    
    def left_child_index(self, parent_index):
        return (2 * parent_index) + 1
    
    def right_child_index(self, parent_index):
        return (2 * parent_index) + 2
    
    def parent_index(self, child_index):
        return (child_index - 1) // 2
    
    def _is_valid_index(self, index):
        return index >= 0 and index < len(self._values)

    def search(self, to_find, starting_index = 0):
        if not self._is_valid_index(starting_index):
            return False 
        
        if to_find == self._values[starting_index]:
            return True 
        elif to_find < self._values[starting_index]:
            left_index = self.left_child_index(starting_index)
            return self.search(to_find, left_index)
        else:
            right_index = self.right_child_index(starting_index)
            return self.search(to_find, right_index)

'''
            11
    4               21
-2      8       19      94
'''
init_values = [11, 4, 21, -2, 8, 19, 94]
bst = Binary_Search_Tree(values = init_values)
print(f'{bst.parent_index(2) = }')
print(f'{bst.right_child_index(2) = }')
print(f'{bst.left_child_index(2) = }')
print(f'{bst.search(94) = }')
print(f'{bst.search(-2) = }')
print(f'{bst.search(11) = }')
print(f'{bst.search(-7) = }')
print(f'{bst.search(388) = }')

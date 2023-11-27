# 10b - Advanced Data Structures

# Coding Exercise 10b.1
class Binary_Search_Tree:
    def __init__(self, values = []):
        self._values = values 
    
    def left_child_index(self, parent_index):
        return (2 * parent_index) + 1
    
    def right_child_index(self, parent_index):
        return (2 * parent_index) + 2
    
    def parent_index(self, child_index):
        return (child_index - 1) // 2

    def _is_index_valid(self, index):
        return index >= 0 and index < len(self._values)

    def search(self, to_find, index = 0):
        if not self._is_index_valid(index):
            return False
        
        if to_find == self._values[index]:
            return True 
        elif to_find < self._values[index]:
            left_index = self.left_child_index(index)
            return self.search(to_find, left_index)
        else:
            right_index = self.right_child_index(index)
            return self.search(to_find, right_index)
    
    def print(self, index = 0, depth = 0):
        if not self._is_index_valid(index):
            return 
        
        self.print(self.right_child_index(index), depth + 1)
        print('\t' * depth, self._values[index])
        self.print(self.left_child_index(index), depth + 1)


'''
            12
    8               16
-2      9       13      16    
'''
bst = Binary_Search_Tree(values = [12,8,16,-2,9,13,16])
print(f'{bst.left_child_index(1) = }')
print(f'{bst.right_child_index(1) = }')
print(f'{bst.parent_index(1) = }')
print(f'{bst.search(-2) = }')
print(f'{bst.search(20) = }')
bst.print()

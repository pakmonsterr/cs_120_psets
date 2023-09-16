#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    if v.left != None:
        calculate_sizes(v.left)

    if v.right != None:
        calculate_sizes(v.right)
    
    v.size = (v.left.size if v.left != None else 0) + (v.right.size if v.right != None else 0) + 1
    
    pass

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r): 

    arr = [r]

    v_find(r, r.size, arr)

    return arr[0];
    
def v_find(v, n, array):
    r_size = v.right.size if v.right else 0
    l_size = v.left.size if v.left else 0

    if (r_size <= (n / 2)) and (l_size <= (n / 2)):
        array[0] = v
    else:
        if (v.right != None):
            v_find(v.right, n, array)
        elif (v.left != None):
            v_find(v.left, n, array)



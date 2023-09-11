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

    r_size = r.right.size if r.right else 0
    l_size = r.left.size if r.left else 0

    if (r_size <= (r.size / 2)) and (l_size <= (r.size / 2)):
        print("reached end with: ", r.size, ", ", r_size, ", ", l_size)
        return r
    else:
        if (r.right != None):
            find_vertex(r.right)
        if (r.left != None):
            find_vertex(r.left)
    
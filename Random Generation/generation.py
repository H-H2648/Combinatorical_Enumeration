import random
from scipy.special import comb
#Tree is of the form [0, Tree1, Tree2]
#where 0 represents a node, tree1, tree2 is the root node of the node 0


#TO DO LIST: DRAW THE TREE
def genEpsilon(n):
    if n > 1:
        return None
    if n == 0:
        return ()
def genTree(n):
    def num_tree(k):
        return comb(2*k, k, exact=True)//(k+1)
    x = random.random()
    if n == 0:
        epsilon = 1
    else:
        epsilon = 0
    
    num_tree_n = num_tree(n)
    if x <= epsilon/num_tree_n:
        return genEpsilon(n)
    kk = 0
    range_so_far = (num_tree(kk)*num_tree(n - kk - 1))/(num_tree_n)
    while x > range_so_far:
        kk +=1
        range_so_far += (num_tree(kk)*num_tree(n - kk - 1))/(num_tree_n)
    return ("Node", genTree(kk), genTree(n - kk - 1))

tree = genTree(100)
print(tree)
print(tree[0])
print(tree[1])
print(tree[2])


    

    
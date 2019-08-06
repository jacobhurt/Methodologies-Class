"""
 * LinkedTree.java
 *
 * COMSC-132
 *
 * Adopted from David G. Sullivan, Ph.D.
 *
 * Modifications and additions by:
 *     name:
 *     username:
"""
 
"""
* A class for the nodes in the tree
"""

from SortHelper import *
import math

class LinkedTreeNode():

    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        #additions for bbst
        self.parent = None
        self.height = 0

    def is_leaf(self):
        return (self.height == 0)

    """
    finds max height of all children of a node
    """
    def max_children_height(self):
        if self.left and self.right: # node has both children
            return max(self.left.height, self.right.height)
        elif self.left and not self.right: # only left child
            return self.left.height
        elif not self.left and  self.right: #only right child
            return self.right.height
        else:
            return -1               #no children
    """
    finds out difference in heights of  left and right subtrees
    """
    def balance (self):
        return (self.left.height if self.left else -1) - (self.right.height if self.right else -1)


"""
 * LinkedTree - a class that represents a binary tree containing data
 * items with integer keys.  If the nodes are inserted using the
 * insert method, the result will be a binary search tree.
"""
class LinkedTree():
     
    """
    * The root of the tree as a whole
    """
    def __init__(self):
        self.root = None
        self.elements_count = 0    #for testing of implementation of bbst
        self.rebalance_count = 0    # for bbst 
        self.maxheight = 0 #for testing bbst implementation
    """
     * Prints the keys of the tree in the order given by a preorder traversal.
     * Invokes the recursive preorderPrintTree method to do the work.
    """
    def preorderPrint(self):
        if self.root != None:
            LinkedTree.preorderPrintTree(self.root)      
    
    """
     * Recursively performs a preorder traversal of the tree/subtree
     * whose root is specified, printing the keys of the visited nodes.
     * Note that the parameter is *not* necessarily the root of the 
     * entire tree. 
    """
    def preorderPrintTree(root):
        print(str(root.key) + " ", end="")
        if root.left != None:
            LinkedTree.preorderPrintTree(root.left)
        if root.right != None:
            LinkedTree.preorderPrintTree(root.right)

    """
     * Prints the keys of the tree in the order given by a inorder traversal.
     * Invokes the recursive inorderPrintTree method to do the work.
    """
    def inorderPrint(self):
        if self.root != None:
            LinkedTree.inorderPrintTree(self.root)      

    """
     * Recursively performs a inorder traversal of the tree/subtree
     * whose root is specified, printing the keys of the visited nodes.
     * Note that the parameter is *not* necessarily the root of the 
     * entire tree. 
    """
    def inorderPrintTree(root):
        if root.left != None:
            LinkedTree.inorderPrintTree(root.left)
        print(str(root.key) + " ", end="")
        if root.right != None:
            LinkedTree.inorderPrintTree(root.right)
    """
     * Prints the keys of the tree in the order given by a postorder traversal.
     * Invokes the recursive postorderPrintTree method to do the work.
    """
    def postorderPrint(self):
        if self.root != None:
            LinkedTree.postorderPrintTree(self.root)      
    
    """
     * Recursively performs a postorder traversal of the tree/subtree
     * whose root is specified, printing the keys of the visited nodes.
     * Note that the parameter is *not* necessarily the root of the 
     * entire tree. 
    """
    def postorderPrintTree(root):
        if root.left != None:
            LinkedTree.postorderPrintTree(root.left)
        if root.right != None:
            LinkedTree.postorderPrintTree(root.right)
        print(str(root.key) + " ", end="")
    


    """ return height of the root node for checking valid bbst"""
    def findMaxHeight(self):
        if self.root != None:
            return LinkedTree.maxHeightAVL(self.root)

    def maxHeightAVL(root):
        return (root.height)

    """
     * Searches for the specified key in the tree.
     * Invokes the recursive searchTree method to perform the actual search.
    """
    def search(self, key):
        n = LinkedTree.searchTree(self.root, key)
        if n == None:
            return None
        else:
            return n.data
    
    """
     * Recursively searches for the specified key in the tree/subtree
     * whose root is specified. Note that the parameter is *not*
     * necessarily the root of the entire tree.
    """
    def searchTree(root, key):
        if root == None:
            return None
        elif key == root.key:
            return root
        elif key < root.key:
            return LinkedTree.searchTree(root.left, key)
        else:
            return LinkedTree.searchTree(root.right, key)
    
    """
     * Inserts the specified (key, data) pair in the tree so that the
     * tree remains a binary search tree.
    """
    def insert(self, key, data):
        # Find the parent of the new node.
        parent = None
        trav = self.root
        while trav != None:
            parent = trav
            if key < trav.key:
                trav = trav.left
            else:
                trav = trav.right
        
        # Insert the new node.
        newNode = LinkedTreeNode(key, data)
        if parent == None:          # The tree was empty, the new node is the root
            self.root = newNode
        elif key < parent.key:
            parent.left = newNode
        else:
            parent.right = newNode
    
    """
     Deletes the node containing the (key, data) pair with the
     specified key from the tree and return the associated data item.
    """
    def delete(self, key):
        # Find the node to be deleted and its parent.
        parent = None
        trav = self.root
        while trav != None and trav.key != key:
            parent = trav
            if key < trav.key:
                trav = trav.left
            else:
                trav = trav.right
        
        # Delete the node (if any) and return the removed data item.
        if trav == None:   # no such key    
            return None
        else:
            removedData = trav.data
            LinkedTree.deleteNode(trav, parent)
            return removedData

    
    def deleteNode(toDelete, parent):
        # extra credit for PS 4
        pass 

    def depth(self, key):
        trav = self.root
        if key == trav.key:
            return 0
        depth = 0
        while key != trav.key:
            if trav.right == None:
                return -1
            trav = trav.right
            depth += 1
        return depth 
               
        
    
    """
     * Determines if this tree is isomorphic to the other tree,
     * returning true if they are isomorphic and false if they are not.
     * Calls the private helper method isomorphic() to do the work.
     * 
     * You should ***NOT*** change this method. Instead, you should
     * implement the private helper method found below.
    """
    def isomorphicTo(self, other):
        if other.root == None:
           print("parameter must be non-None")
           return False
        else:
            return LinkedTree.isomorphic(self.root, other.root)
    
    """
     * Determines if the trees with the specified root nodes are
     * isomorphic, returning true if they are and false if they are not.
    """
    def isomorphic(tree1, tree2):
        if tree1 == None and tree2 == None:
            return True
        if tree1 != None and tree2 != None:
            return (LinkedTree.isomorphic(tree1.left, tree2.left) and LinkedTree.isomorphic(tree1.right, tree2.right))
        return False 
    
    """
     * Determines if the trees with the specified root nodes are
     * isomorphic, returning true if they are and false if they are not.
    """


    """ finds height of the root to test correctness of avl tree  """
    """def height(self):
        print ("aa")
        if self.root:
            return self.root.height
        else:
            return 0
    """

    """ 
        AVL tree implemented, this function checks for the 4  cases that arise 
        (when tree is unbalanced) and uses different types of rotation to balance the tree
        https://en.wikipedia.org/wiki/AVL_tree#Insertion
    """ 

    def rebalance (self, node_to_rebalance):
        self.rebalance_count += 1
        A = node_to_rebalance 
        F = A.parent #allowed to be NULL
        if node_to_rebalance.balance() == -2:
            if node_to_rebalance.right.balance() <= 0:
                #Rebalance, case RRC only right rotate
                B = A.right
                C = B.right
                assert (not A is None and not B is None and not C is None)
                A.right = B.left
                if A.right:
                    A.right.parent = A
                B.left = A
                A.parent = B                                                               
                if F is None:                                                              
                   self.root = B 
                   self.root.parent = None                                                   
                else:                                                                        
                   if F.right == A:                                                          
                       F.right = B                                                                  
                   else:                                                                      
                       F.left = B                                                                   
                   B.parent = F 
                self.recompute_heights (A) 
                self.recompute_heights (B.parent)                                                                                         
            else:
                #Rebalance, case RLC first leftrotate then right rotate
                B = A.right
                C = B.left
                assert (not A is None and not B is None and not C is None)
                B.left = C.right
                if B.left:
                    B.left.parent = B
                A.right = C.left
                if A.right:
                    A.right.parent = A
                C.right = B
                B.parent = C                                                               
                C.left = A
                A.parent = C                                                             
                if F is None:                                                             
                    self.root = C
                    self.root.parent = None                                                    
                else:                                                                        
                    if F.right == A:                                                         
                        F.right = C                                                                                     
                    else:                                                                      
                        F.left = C
                    C.parent = F
                self.recompute_heights (A)
                self.recompute_heights (B)
        else:
            assert(node_to_rebalance.balance() == +2)
            if node_to_rebalance.left.balance() >= 0:
                B = A.left
                C = B.left
                #Rebalance, case LLC only leftrotate
                assert (not A is None and not B is None and not C is None)
                A.left = B.right
                if (A.left): 
                    A.left.parent = A
                B.right = A
                A.parent = B
                if F is None:
                    self.root = B
                    self.root.parent = None                    
                else:
                    if F.right == A:
                        F.right = B
                    else:
                        F.left = B
                    B.parent = F
                self.recompute_heights (A)
                self.recompute_heights (B.parent) 
            else:
                B = A.left
                C = B.right 
                #Rebalance, case LRC first right rotate then leftrotate
                assert (not A is None and not B is None and not C is None)
                A.left = C.right
                if A.left:
                    A.left.parent = A
                B.right = C.left
                if B.right:
                    B.right.parent = B
                C.left = B
                B.parent = C
                C.right = A
                A.parent = C
                if F is None:
                   self.root = C
                   self.root.parent = None
                else:
                   if (F.right == A):
                       F.right = C
                   else:
                       F.left = C
                   C.parent = F
                self.recompute_heights (A)
                self.recompute_heights (B)
                
    """ recomputes the heights of all the child nodes of a particular node """
    def recompute_heights (self, start_from_node):
        changed = True
        node = start_from_node
        while node and changed:
            old_height = node.height
            node.height = (node.max_children_height() + 1 if (node.right or node.left) else 0)
            changed = node.height != old_height
            node = node.parent
    
    """
    similar to insert function in regular BST decides where to add node 
    and also checks imbalances 
    """  
    def add_node_to_avl (self, parent_node, child_node):
        node_to_rebalance = None
        if child_node.key < parent_node.key:
            if not parent_node.left:
                parent_node.left = child_node
                child_node.parent = parent_node
                if parent_node.height == 0:
                    node = parent_node
                    while node:
                        node.height = node.max_children_height() + 1
                        if not node.balance () in [-1, 0, 1]:
                            node_to_rebalance = node
                            break #we need the one that is furthest from the root
                        node = node.parent     
            else:
                self.add_node_to_avl(parent_node.left, child_node)
        else:
            if not parent_node.right:
                parent_node.right = child_node
                child_node.parent = parent_node
                if parent_node.height == 0:
                    node = parent_node
                    while node:
                        node.height = node.max_children_height() + 1
                        if not node.balance () in [-1, 0, 1]:
                            node_to_rebalance = node
                            break #we need the one that is furthest from the root
                        node = node.parent       
            else:
                self.add_node_to_avl(parent_node.right, child_node)
        
        if node_to_rebalance:
            self.rebalance (node_to_rebalance)
    
    def insertAVL (self, key, data):
        new_node = LinkedTreeNode (key,data)
        if not self.root:
            self.root = new_node
        else:
            self.elements_count += 1
            self.add_node_to_avl (self.root, new_node)



    def listToBBST(self, keys, data):
        
        SortHelper.quickSort(keys,data) # sort data
    #    for i in range(len(keys)):
    #       print (keys[i],data[i])

        avl = LinkedTree()
        for i in range(len(keys)):    
            self.insertAVL(keys[i],data[i])  #insert into tree
        
    
    
        
        
def main():
    
    tree = LinkedTree()
    tree.insert(7, "root node")
    tree.insert(9, "7's right child")
    tree.insert(5, "7's left child")
    tree.insert(2, "5's left child")
    tree.insert(8, "9's left child")
    tree.insert(6, "5's right child")
    tree.insert(4, "2's right child")



    
    print("\n preorder: ", end="")
    tree.preorderPrint()
    print()
        
    print("postorder: ", end="")
    tree.postorderPrint()
    print()
        
    print("inorder:   ", end="")
    tree.inorderPrint()
    print()

    key = int(input("\nkey to search for: "))
    data = tree.search(key)
    if data != None:
        print(str(key) + " = " + str(data))
    else:
        print("no such key in tree")

    print("\n Tree 1")
    print("\n preorder: ", end="")
    tree.preorderPrint();
    print();
        
    print("postorder: ", end="")
    tree.postorderPrint()
    print()

    print("inorder: ", end="")
    tree.inorderPrint()
    print()

    print("\n Tree 2")
    print("\n preorder: ", end="")
    tree.preorderPrint();
    print();
        
    print("postorder: ", end="")
    tree.postorderPrint()
    print()

    print("inorder: ", end="")
    tree.inorderPrint()
    print()

    
    key = int(input("\nkey to delete: "))
    data = tree.delete(key)
    if data != None:
        print("removed " + str(data))
    else:
        print("no such key in tree")

    print("\n")

    keys = [7,9,5,2,8,6,4]
    data = ["root node","7's right child","7's left child","5's left child","9's left child","5's right child","2's right child"]
    tree1 = LinkedTree()
    tree1.listToBBST(keys,data)

    print("\n AVLpreorder: ", end="")
    tree1.preorderPrint();
    print();
        
    print("AVLpostorder: ", end="")
    tree1.postorderPrint()
    print()

    print("  AVLinorder: ", end="")
    tree1.inorderPrint()
    print()


    """ for checking correctness of tree """
    #height of the tree
    height=tree1.findMaxHeight()
    # this is the max height possible for a tree with certain no of elements
    max_height=1.44*math.log(int(tree1.elements_count+2),2) - 1 
    
    assert(max_height >= height) 
   # print tree1.height()
    
main()
 

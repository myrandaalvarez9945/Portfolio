# I want to be able to understand this code and see if I can remake it another time

# I know that we are making a node, that way
# it would be easier to go through each child branch 
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Inorder traversal - visited a specific order: Left, root, and then right
def inorder(root):
    if root is not None:
        # Goes Left
        inorder(root.left)

        # Goes To The Root
        print(str(root.key) + "->", end=' ')

        # Goes Right
        inorder(root.right)


# We are adding a node
def insert(node, key):

    # Return a new node if the tree is empty
    if node is None:
        return Node(key)

    # Traverse - refers to the process of moving through the nodes
    # of a binary search tree to find the correct location.
    # So if the node is less than the root than it goes to the left,
    # if it is greater than it will go to the right.
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


# Here we are getting the minimum value of the node
def minValueNode(node):
    current = node

    # Find the leftmost leaf
    while(current.left is not None):
        current = current.left

    return current


# Deleting a node
def deleteNode(root, key):

    # Return if the tree is empty
    if root is None:
        return root

    # Find the node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        # If the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # If the node has two children,
        # place the mininmum value in position of the node to be deleted
        temp = minValueNode(root.right)

        root.key = temp.key

        # Delete the minimum value of the inorder traversal
        root.right = deleteNode(root.right, temp.key)

    return root

# Here, they are just adding numbers to create the tree
root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

# Now we will see the difference of the inorder traversal - first,
# it will have all the roots
# Then, with a deleted node.
print("Inorder traversal: ", end=' ')
inorder(root)

print("\nDelete 10")
root = deleteNode(root, 10)

print("Inorder traversal: ", end=' ')
inorder(root)
"""
Creating Binary Search Tree using Linked List
"""


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeVal):
    if rootNode.data is None:
        rootNode.data = nodeVal
    elif nodeVal <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BinarySearchTree(nodeVal)
        else:
            insertNode(rootNode.leftChild, nodeVal)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BinarySearchTree(nodeVal)
        else:
            insertNode(rootNode.rightChild, nodeVal)
    return 'Successfully inserted'


newBst = BinarySearchTree(None)
print(insertNode(newBst, 70))
print(insertNode(newBst, 60))

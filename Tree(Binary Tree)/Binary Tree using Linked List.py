import Queue as Q


class TreeNode:
    def __init__(self, value: str = None):
        self.data = value
        self.leftChild = None
        self.rightChild = None


newBt = TreeNode("Drinks")
leftChild = TreeNode('Hot')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode('Cold')
newBt.leftChild = leftChild
newBt.rightChild = rightChild


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Q.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.data.data)
            if root.data.leftChild is not None:
                customQueue.enqueue(root.data.leftChild)
            if root.data.rightChild is not None:
                customQueue.enqueue(root.data.rightChild)


def searchBT(rootNode, nodeValue):
    if not rootNode:
        return 'Binary Tree does not exist'
    else:
        customQueue = Q.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.data.data == nodeValue:
                return 'Success'
            if root.data.leftChild is not None:
                customQueue.enqueue(root.data.leftChild)
            if root.data.rightChild is not None:
                customQueue.enqueue(root.data.rightChild)
        return 'Not Found'


def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = Q.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.data.leftChild is None:
                root.data.leftChild = newNode
                return "inserted Successfully"
            else:
                customQueue.enqueue(root.data.leftChild)
            if root.data.rightChild is None:
                root.data.rightChild = newNode
                return "inserted Successfully"
            else:
                customQueue.enqueue(root.data.rightChild)


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Q.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.data.leftChild is not None:
                customQueue.enqueue(root.data.leftChild)
            if root.data.rightChild is not None:
                customQueue.enqueue(root.data.rightChild)
        deepestNode = root.data
        return deepestNode


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = Q.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.data is dNode:
                root.data = None
                return
            if root.data.rightChild:
                if root.data.rightChild is dNode:
                    root.data.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.data.rightChild)
            if root.data.leftChild:
                if root.data.leftChild is dNode:
                    root.data.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.data.leftChild)


def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "BT does not exist"
    else:
        customQueue = Q.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.data.data == node:
                dNode = getDeepestNode(rootNode)
                root.data.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"
            if root.data.leftChild is not None:
                customQueue.enqueue(root.data.leftChild)
            if root.data.rightChild is not None:
                customQueue.enqueue(root.data.rightChild)
        return "Failed to delete"


def deleteEntireBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "deleted successfully"


print(deleteEntireBT(newBt))
levelOrderTraversal(newBt)

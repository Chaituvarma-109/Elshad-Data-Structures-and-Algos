from typing import Union


class TreeNode:
    def __init__(self, data: Union[str, int], children: list[Union[str, int]] = None):
        if children is None:
            children = []
        self.data = data
        self.children = children

    def __str__(self, level: int = 0) -> str:
        ret = ' '*level + str(self.data) + '\n'
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, TreeNode) -> None:
        self.children.append(TreeNode)


tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
tree.addChild(cold)
tree.addChild(hot)

tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
hot.addChild(tea)
hot.addChild(coffee)

print(tree)

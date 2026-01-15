# 请你给出二叉树的层次建树代码
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_level_order(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    index = 1

    while index < len(values):
        current = queue.pop(0)

        # 添加左孩子
        if values[index] is not None:
            current.left = TreeNode(values[index])
            queue.append(current.left)
        index += 1

        # 添加右孩子
        if index < len(values) and values[index] is not None:
            current.right = TreeNode(values[index])
            queue.append(current.right)
        index += 1

    return root
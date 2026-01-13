class Node(object):
    """节点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        # elem 是节点存储的数据，默认值为 -1
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""

    def __init__(self):
        # 初始化时创建一个空的根节点
        self.root = Node()
        # myQueue 队列用于存放还没长满子节点的父节点
        self.myQueue = []

    def add(self, elem):
        """按层序为树添加节点"""
        node = Node(elem)

        # 情况1：如果是空树，先给根节点赋值
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)

        # 情况2：树不为空，寻找最左侧的空位插入
        else:
            # 取出当前队列最前面的节点（即当前层最左边没满的父节点）
            treeNode = self.myQueue[0]

            # 优先填充左孩子
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            # 左边满了，填充右孩子
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                # 一旦右孩子也填满了，这个父节点就“任务圆满”，弹出队列
                self.myQueue.pop(0)

    # 给出前序遍历代码
def preOrder(node):
    if node == None:
         return
    print(node.elem, end=" ")
    preOrder(node.lchild)
    preOrder(node.rchild)


def midOrder(node):
    if node == None:
         return
    midOrder(node.lchild)
    print(node.elem, end=" ")
    midOrder(node.rchild)


def postOrder(node):
    if node == None:
         return
    postOrder(node.lchild)
    postOrder(node.rchild)
    print(node.elem, end=" ")


def levelOrder(node):
    """层序遍历"""
    if node == None:
        return
    myQueue = []
    myQueue.append(node)
    while myQueue:
        # 取出队列的第一个节点
        treeNode = myQueue.pop(0)
        print(treeNode.elem, end=" ")
        # 如果左孩子不为空，加入队列
        if treeNode.lchild != None:
            myQueue.append(treeNode.lchild)
        # 如果右孩子不为空，加入队列
        if treeNode.rchild != None:
            myQueue.append(treeNode.rchild)


if __name__ == "__main__":

    tree = Tree()
    for i in range(10):
        tree.add(i)

    # 测试前序遍历
    print("前序遍历结果如下：")
    preOrder(tree.root)
    print()


    print("中序遍历结果如下：")
    midOrder(tree.root)
    print()

    print("后序遍历结果如下：")
    postOrder(tree.root)
    print()


    print("层序遍历结果如下：")
    levelOrder(tree.root)
    print()

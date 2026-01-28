# 二叉树的层次建树


class Node(object):
    #节点类

    def __init__(self, elem = -1, lchild = None, rchild = None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    # 树类

    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        # 为树添加节点

        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)

        else:
            treeNode = self.myQueue[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)

    def front_digui(self, node):
        # 前序递归遍历

        if node == None:
            return
        print(node.elem, end = " ")
        self.front_digui(node.lchild)
        self.front_digui(node.rchild)

    def mid_digui(self, node):
        # 中序递归遍历

        if node == None:
            return
        self.mid_digui(node.lchild)
        print(node.elem, end = " ")
        self.mid_digui(node.rchild)

    def back_digui(self, node):
        # 后序递归遍历

        if node == None:
            return
        self.back_digui(node.lchild)
        self.back_digui(node.rchild)
        print(node.elem, end = " ")

    def level_queue(self, root):
        if root == None:
            return

        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem, end=" ")
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)


if __name__ == "__main__":
    tree = Tree()
    for i in range(10):
        tree.add(i)
    print("前序递归遍历：", end = " ")
    tree.front_digui(tree.root)
    print("\n中序递归遍历：", end = " ")
    tree.mid_digui(tree.root)
    print("\n后序递归遍历：", end = " ")
    tree.back_digui(tree.root)
    print("\n层次遍历：", end = " ")
    tree.level_queue(tree.root)



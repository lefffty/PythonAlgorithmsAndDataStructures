Int = int
Float = float
Bool = bool


class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_terminal(self) -> Bool:
        return not (self.left_child and self.right_child)

    def __repr__(self):
        return f'Value: {self.value}'


class BinarySearchTree:
    def __init__(self):
        """
        Конструктор класса
        """
        self.root = None

    def insert(self, value):
        """
        Добавление вершины
        """
        node = BinarySearchTreeNode(value)
        if not self.root:
            self.root = node
        else:
            temp = self.root
            while True:
                if value > temp.value:
                    if temp.right_child is None:
                        temp.right_child = node
                        break
                    else:
                        temp = temp.right_child
                else:
                    if temp.left_child is None:
                        temp.left_child = node
                        break
                    else:
                        temp = temp.left_child

    def find(self, target):
        """
        Поиск значения в дерева
        """
        temp = self.root
        while temp:
            if temp.value == target:
                return temp
            elif temp.value > target:
                temp = temp.left_child
            else:
                temp = temp.right_child
        return None

    def delete(self, target):
        """
        Удаление узла из дерева
        """
        node = self.find(target)
        # если удаляемый узел - терминальный, то просто удаляем узел
        if node.is_terminal():
            del node
        # если есть только левый потомок
        elif node.left_child and not node.right_child:
            node = node.left_child
        # если есть только правый потомок
        elif node.right_child and not node.left_child:
            node = node.right_child
        # если есть оба потомка
        else:
            # если у левого потомка нет правого потомка,
            # то на место удаляемого узла ставим левого потомка
            if not node.left_child.right_child:
                node = node.left_child
            # если у левого потомка есть правый потомок, то
            # на место удаляемого узла ставим самого правого потомка
            else:
                temp = node.left_child.right_child
                while temp.right_child:
                    temp = temp.right_child
                node = temp

    def breadthSearch(self):
        """
        Поиск в ширину
        """
        queue = []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print(node.value)
            if node.left_child:
                queue.append(node.left_child)
            if node.right_child:
                queue.append(node.right_child)

    def findMax(self):
        """
        Поиск максимального элемента
        """
        if not self.root:
            return None
        temp = self.root
        while temp.right_child:
            temp = temp.right_child
        return temp.value

    def findMin(self):
        """
        Поиск минимального элемента
        """
        if not self.root:
            return None
        temp = self.root
        while temp.left_child:
            temp = temp.left_child
        return temp.value

    def depthSearch(self):
        """
        Поиск в глубину
        """
        queue = []
        queue.insert(0, self.root)
        while (queue):
            node = queue.pop(0)
            print(node.value)
            if node.left_child:
                queue.insert(0, node.left_child)
            if node.right_child:
                queue.insert(0, node.right_child)

    # лево - центр - право
    def inOrderTraversal(self):
        ans = []
        stack = []
        current = self.root
        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left_child
            current = stack.pop()
            ans.append(current.value)
            current = current.right_child
        return ans

    # центр - лево - право
    def preOrderTraversal(self):
        if not self.root:
            return []
        ans = []
        stack = [self.root]
        while stack:
            current = stack.pop()
            ans.append(current.value)
            if current.right_child:
                stack.append(current.right_child)
            if current.left_child:
                stack.append(current.left_child)
        return ans

    # лево - право - центр
    def postOrderTraversal(self):
        pass


tree = BinarySearchTree()
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(3)
tree.insert(3.5)
print(tree.inOrderTraversal())
print(tree.preOrderTraversal())

from __future__ import annotations
from dataclasses import dataclass
from collections import deque
from random import randint


@dataclass
class AVLTreeNode:
    value: int
    right: AVLTreeNode = None
    left: AVLTreeNode = None
    height: int = 1

    def __repr__(self):
        return f'AVLTreeNode({self.value})'


def height(node: AVLTreeNode) -> int:
    """
    Height for current node
    """
    return node.height if node else 0


def fix_height(node: AVLTreeNode) -> None:
    """
    Correcting height for current node
    """
    left_height = height(node.left)
    right_height = height(node.right)
    node.height = max(left_height, right_height) + 1


def balance_factor(node: AVLTreeNode) -> int:
    """
    Balance factor for current node
    """
    return height(node.right) - height(node.left)


def left_rotation(old_root: AVLTreeNode):
    """
    Left rotation around current node
    """
    new_root = old_root.right
    old_root_right = new_root.left
    new_root.left = old_root
    old_root.right = old_root_right
    fix_height(old_root)
    fix_height(new_root)
    return new_root


def right_rotation(old_root: AVLTreeNode):
    """
    Right rotation around current node
    """
    new_root = old_root.left
    old_root_left = new_root.right
    new_root.right = old_root
    old_root.left = old_root_left
    fix_height(old_root)
    fix_height(new_root)
    return new_root


def balance(root: AVLTreeNode):
    """
    Balancing AVLTree
    """
    fix_height(root)

    b_factor = balance_factor(root)

    if b_factor == 2:
        if balance_factor(root.right) < 0:
            # Left-Right insertion (Right-Left rotation)
            root.right = right_rotation(root.right)
        # Right-Right insertion (Left rotation)
        return left_rotation(root)
    if b_factor == -2:
        if balance_factor(root.left) > 0:
            # Right-Left insertion (Left-Right rotation)
            root.left = left_rotation(root.left)
        # Left-Left insertion (Right rotation)
        return right_rotation(root)
    return root


def insert(root: AVLTreeNode, value):
    """
    Insert node into tree
    """
    if not root:
        return AVLTreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return balance(root)


def find_min(root: AVLTreeNode) -> AVLTreeNode:
    """
    Find minimal element of AVL-Tree with root as root element
    """
    return find_min(root.left) if root.left else root


def find_max(root: AVLTreeNode) -> AVLTreeNode:
    """
    Find maximum element of AVL-Tree with root as root element
    """
    return find_max(root.right) if root.right else root


def remove_min(node: AVLTreeNode) -> AVLTreeNode:
    """
    Remove minimal element of AVL-Tree
    """
    if not node.left:
        return node.right
    node.left = remove_min(node.left)
    return balance(node)


def remove(root: AVLTreeNode, value):
    """
    Remove node with value=value
    """
    if not root:
        return None
    if value < root.value:
        root.left = remove(root.left, value)
    elif value > root.value:
        root.right = remove(root.right, value)
    else:
        left = root.left
        right = root.right
        del root
        if not right:
            return left
        min_node: AVLTreeNode = find_min(right)
        min_node.right = remove_min(right)
        min_node.left = left
        return balance(min_node)


def breadth_first_search(root: AVLTreeNode):
    """
    BreadthFirstSearch traversal in AVL-Tree

    Example:
            6
           / \
          3   8
         / \
        1   4
    >>> depth_first_search(root)
    Output:
        AVLTreeNode(6)
        AVLTreeNode(3)
        AVLTreeNode(1)
        AVLTreeNode(4)
        AVLTreeNode(8)
    """
    if not root:
        return
    queue = deque([root])
    reprs = []
    while queue:
        node: AVLTreeNode = queue.popleft()
        reprs.append(repr(node))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return '\n'.join(reprs)


def depth_first_search(root: AVLTreeNode):
    """
    DepthFirstSearch traversal in AVL-Tree

    Example:
            6
           / \
          3   8
         / \
        1   4
    >>> depth_first_search(root)
    Output:
        AVLTreeNode(6)
        AVLTreeNode(3)
        AVLTreeNode(8)
        AVLTreeNode(1)
        AVLTreeNode(4)
    """
    if not root:
        return
    queue = deque([root])
    reprs = []
    while queue:
        node: AVLTreeNode = queue.popleft()
        reprs.append(repr(node))
        if node.right:
            queue.appendleft(node.right)
        if node.left:
            queue.appendleft(node.left)
    return '\n'.join(reprs)


def in_order_traversal(root: AVLTreeNode):
    """
    Left - Center - right traversal

    Example:
            6
           / \
          3   8
         / \
        1   4
    >>> in_order_traversal(root)
    Output:
        AVLTreeNode(1)
        AVLTreeNode(3)
        AVLTreeNode(4)
        AVLTreeNode(6)
        AVLTreeNode(8)
    """
    if not root:
        return
    in_order_traversal(root.left)
    print(root)
    in_order_traversal(root.right)


def pre_order_traversal(root: AVLTreeNode):
    """
    Center - Left - Right traversal
            6
           / \
          3   8
         / \
        1   4
    >>> pre_order_traversal(root)
    Output:
        AVLTreeNode(6)
        AVLTreeNode(3)
        AVLTreeNode(1)
        AVLTreeNode(4)
        AVLTreeNode(8)
    """
    if not root:
        return
    print(root)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)


def post_order_traversal(root: AVLTreeNode):
    """
    Left - Right - Center traversal
            6
           / \
          3   8
         / \
        1   4
    >>> post_order_traversal(root)
    Output:
        AVLTreeNode(1)
        AVLTreeNode(4)
        AVLTreeNode(3)
        AVLTreeNode(8)
        AVLTreeNode(6)
    """
    if not root:
        return
    post_order_traversal(root.left)
    post_order_traversal(root.right)
    print(root)


    
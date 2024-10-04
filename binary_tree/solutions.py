from typing import Optional, List


# Пример построения дерева по уровням и обход его в глубину
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(8)
# root.left.right.left = TreeNode(6)
# root.left.right.right = TreeNode(7)
# root.right.right = TreeNode(8)
# root.right.right.left = TreeNode(9)
#
# # обход в глубину
# dfs_result = []
# def dfs(node: TreeNode):
#     if node is None:
#         return
#
#     dfs(node.left)
#     dfs_result.append(node.val)
#     dfs(node.right)
#
#
# dfs(root)
# print(dfs_result)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
#
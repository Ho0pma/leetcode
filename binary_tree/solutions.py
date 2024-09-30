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
# 94. Binary Tree Inorder Traversal / EASY

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class TreeByLevel:
#     def build_tree_by_levels(self, lst):
#         if not lst:
#             return None
#
#         root = TreeNode(lst[0])
#         queue = [root]
#         i = 1
#
#         while i < len(lst):
#             current = queue.pop(0)
#
#             if i < len(lst) and lst[i] is not None:
#                 current.left = TreeNode(lst[i])
#                 queue.append(current.left)
#             i += 1
#
#             if i < len(lst) and lst[i] is not None:
#                 current.right = TreeNode(lst[i])
#                 queue.append(current.right)
#             i += 1
#
#         return root
#
#
# lst = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
# tree_builder = TreeByLevel()
# root = tree_builder.build_tree_by_levels(lst) #

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._postorder_helper(root, result)
        return result

    def _postorder_helper(self, node: Optional[TreeNode], result: List[int]) -> None:
        if node:
            self._postorder_helper(node.left, result)
            result.append(node.val)
            self._postorder_helper(node.right, result)

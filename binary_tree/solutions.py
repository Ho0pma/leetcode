from collections import deque
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
# 94. Binary Tree Inorder Traversal

# задача: задача вывести дерево путем in-order traversal (обход в глубину)
# 1) O(n)
# с использование рекурсии
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result_lst = [] # очищаем список перед каждым вызовом
#
#         def inorder(node):
#             if node is None:
#                 return
#
#             inorder(node.left)
#             result_lst.append(node.val)
#             inorder(node.right)
#
#         inorder(root)
#
#         return result_lst
#
#
# root1 = TreeNode(
#     val=1,
#     right=TreeNode(
#         val=2,
#         left=TreeNode(3)
#     )
# )
#
# root2 = TreeNode(
#     val=1,
#     left=TreeNode(
#         val=2,
#         left=TreeNode(val=4),
#         right=TreeNode(
#             val=5,
#             left=TreeNode(6),
#             right=TreeNode(7),
#         )
#
#     ),
#     right=TreeNode(
#         val=3,
#         right=TreeNode(
#             val=8,
#             left=TreeNode(9)
#         )
#     )
# )
#
# s = Solution()
# print(s.inorderTraversal(root1)) # Output: [1, 3, 2]
# print(s.inorderTraversal(root2))  # Output: [4, 2, 6, 5, 7, 1, 3, 9, 8]

# 2) с использованием стека
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result_lst = []
#         stack = []
#
#         while root or stack:
#             # сначала идем максимально вглубь влево, добавляя значения в стек
#             while root:
#                 stack.append(root)
#                 root = root.left
#
#             # как только дошли до конца - высвобождаем значения и переходим
#             # к правому поддереву
#             root = stack.pop()
#             result_lst.append(root.val)
#
#             # благодаря этой строчке (если уперлись в самое левую ноду) и дальше None
#             # не будет заходить во внутренний цикл и будет дальше искать правые поддеревья
#             root = root.right
#
#         return result_lst
#
#
#
# root1 = TreeNode(
#     val=1,
#     right=TreeNode(
#         val=2,
#         left=TreeNode(3)
#     )
# )
#
# root2 = TreeNode(
#     val=1,
#     left=TreeNode(
#         val=2,
#         left=TreeNode(val=4),
#         right=TreeNode(
#             val=5,
#             left=TreeNode(6),
#             right=TreeNode(7),
#         )
#
#     ),
#     right=TreeNode(
#         val=3,
#         right=TreeNode(
#             val=8,
#             left=TreeNode(9)
#         )
#     )
# )
#
# s = Solution()
# print(s.inorderTraversal(root1)) # Output: [1, 3, 2]
# print(s.inorderTraversal(root2))  # Output: [4, 2, 6, 5, 7, 1, 3, 9, 8]

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 100. Same Tree

# задача: задача проверить одинаковые ли деревья

# 1) через цикл и стек
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#         stack = []
#
#         while root1 or root2 or stack:
#             if root1 and root2:
#                 if root1.val != root2.val:
#                     return False
#
#                 stack.append((root1, root2))
#                 root1 = root1.left
#                 root2 = root2.left
#
#             # заходит сюда, если не выполняется условие выше
#             elif root1 or root2:
#                 return False
#
#             else:
#                 root1, root2 = stack.pop()
#                 root1 = root1.right
#                 root2 = root2.right
#
#         return True

# # первый кейс:
# root1 = TreeNode(
#     val=1,
#     left=TreeNode(2),
#     right=TreeNode(3),
# )
# root2 = TreeNode(
#     val=1,
#     left=TreeNode(2),
#     right=TreeNode(3),
# )

# # второй кейс:
# root1 = TreeNode(
#     val=1,
#     left=TreeNode(2),
# )
# root2 = TreeNode(
#     val=1,
#     right=TreeNode(2),
# )

# третий кейс:
# root1 = TreeNode(
#     val=1,
#     left=TreeNode(2),
#     right=TreeNode(1),
# )
# root2 = TreeNode(
#     val=1,
#     left=TreeNode(1),
#     right=TreeNode(2),
# )

# 4 кейс:
# root1 = TreeNode(
#     val=0
# )
# root2 = TreeNode()
#
# s = Solution()
# print(s.isSameTree(root1, root2))

# 2) через рекурсию
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#         if not root1 and not root2:
#             return True
#         if not root1 or not root2:
#             return False
#
#         if root1.val == root2.val:
#             return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
#
#         return False
#
# первый кейс:
# root1 = TreeNode(
#     val=1,
#     left=TreeNode(2),
#     right=TreeNode(3),
# )
# root2 = TreeNode(
#     val=1,
#     left=TreeNode(2),
#     right=TreeNode(3),
# )

# третий кейс:
# root1 = TreeNode(
#     val=1,
#     left=TreeNode(2),
#     right=TreeNode(1),
# )
# root2 = TreeNode(
#     val=1,
#     left=TreeNode(1),
#     right=TreeNode(2),
# )
#
# s = Solution()
# print(s.isSameTree(root1, root2))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 101. Symmetric Tree

# задача: проверить симметрично ли дерево

# 1)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
#
#         def isMirror(t1, t2):
#             # базовые проверки существуют ли узлы
#             if not t1 and not t2:
#                 return True
#             if not t1 or not t2:
#                 return False
#
#             # от корня идем в разные направления и проверяем их между собой. Лучше нарисовать, сразу понятно
#             return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
#
#         return isMirror(root.left, root.right)
#
# первый кейс
# root = TreeNode(
#     val=1,
#     left=TreeNode(
#         val=2,
#         left=TreeNode(3),
#         right=TreeNode(4),
#     ),
#     right=TreeNode(
#         val=2,
#         left=TreeNode(4),
#         right=TreeNode(3),
#     )
# )

# второй кейс
# root = TreeNode(
#     val=1,
#     left=TreeNode(
#         val=2,
#         right=TreeNode(3)
#     ),
#     right=TreeNode(
#         val=2,
#         right=TreeNode(3)
#     )
# )
#
# третий кейс
# root = TreeNode(
#     val=1,
#     left=TreeNode(
#         val=2,
#         left=TreeNode(2)
#     ),
#     right=TreeNode(
#         val=2,
#         left=TreeNode(2)
#     )
# )
# s = Solution()
# print(s.isSymmetric(root))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 104. Maximum Depth of Binary Tree

# задача: нужно посчитать максимальную глубину дерева

# 1)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#
#         left_depth = self.maxDepth(root.left)
#         right_depth = self.maxDepth(root.right)
#
#         return 1 + max(left_depth, right_depth)
#
#
# root = TreeNode(
#     val=3,
#     left=TreeNode(9),
#     right=TreeNode(
#         val=20,
#         left=TreeNode(15),
#         right=TreeNode(7),
#     )
# )
#
# s = Solution()
# print(s.maxDepth(root))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 108. Convert Sorted Array to Binary Search Tree

# задача: нужно создать BST по поступаемому отсортированному массиву

# 1)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         if not nums:
#             return None
#
#         mid = len(nums) // 2
#         root = TreeNode(nums[mid])
#
#         # нашли центр массива, сохраняем его как ноду
#         # от ноды разбиваем массив на две части
#         # так делаем до тех пор, пока есть nums
#         root.left = self.sortedArrayToBST(nums[:mid])
#         root.right = self.sortedArrayToBST(nums[mid + 1:])
#
#         return root
#
#
# s = Solution()
# root = s.sortedArrayToBST(nums=[-10, -3, 0, 5, 9])  # Output: [0,-3,9,-10,null,5] or [0,-10,5,null,-3,null,9]
#
# # для проверки
# def bfs(root):
#     if not root:
#         return
#
#     bfs(root.left)
#     print(root.val, end=' ')
#     bfs(root.right)
#
#
# bfs(root)  # output: [-10, -3, 0, 5, 9] те равно тому что задали

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 110. Balanced Binary Tree

# url: https://leetcode.com/problems/balanced-binary-tree/description/

# задача:

# 1)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]):
#         pass
#
#
# root = TreeNode(
#     val=3,
#     left=TreeNode(9),
#     right=TreeNode(
#         val=20,
#         left=TreeNode(15),
#         right=TreeNode(7)
#     )
# )
#
# s = Solution()
# print(s.isBalanced(root))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# Алгоритм обхода дерева в ширину (BFS: Breadth-First Search)

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# root = TreeNode(
#     val=1,
#     left=TreeNode(
#         val=2,
#         left=TreeNode(4),
#         right=TreeNode(5)
#     ),
#     right=TreeNode(3)
# )
#
# def bfs(root):
#     if root is None:
#         return
#
#     # добавляем корень в очередь
#     queue = deque([root])
#
#     while queue:
#         # текущий узел берем из попа
#         node = queue.popleft()
#         print(node.val, end=' ')
#
#         # если у удаленного из очереди элемента есть дети - добавляем их в очередь
#         # тем самым пополняем ее до тех пор, пока не дойдем до None
#         if node.left:
#             queue.append(node.left)
#
#         if node.right:
#             queue.append(node.right)
#
# bfs(root)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
#
#####################################################################################################
import pytest


# 🌶️ 20. Valid Parentheses
#
# Задача: подается строка состоящая из разных скобок, к примеру: ({[][][]})
# нужно проверить является ли она валидной
#
# 1) Time O(n)  Space O(n)
# class Solution:
#     def isValid(self, s: str) -> bool:
#         if s[0] in '})]':
#             return False
#
#         stack = []
#         hash_map = {
#             '}': '{',
#             ')': '(',
#             ']': '[',
#         }
#
#         for i in s:
#             if i not in '})]':
#                 stack.append(i)
#             else:
#                 if stack:
#                     p = stack.pop()
#                     if hash_map[i] != p:
#                         return False
#                 else:
#                     return False
#
#         return False if stack else True
#
# 2) лучше код + как мин нет проверки < if i not in '})]' >
# class Solution:
#     def isValid(self, s: str) -> bool:
#         if s[0] in '})]':
#             return False
#
#         stack = []
#         hash_map = {
#             '}': '{',
#             ')': '(',
#             ']': '[',
#         }
#
#         for i in s:
#             if i in hash_map:
#                 if stack and stack[-1] == hash_map[i]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(i)
#
#         return True if not stack else False
#
# s = Solution()
# print(s.isValid(s="()"))  # True
# print(s.isValid(s="()[]{}"))  # True
# print(s.isValid(s="(]"))  # False
# print(s.isValid(s="([])"))  # True
# print(s.isValid(s="([)]"))  # False
# print(s.isValid(s="[])"))  # False
#
# @pytest.mark.parametrize(
#     's, expected',
#     [
#         ('()', True),
#         ('()[]{}', True),
#         ('(]', False),
#         ('([])', True),
#         ('([)]', False),
#         ('[])', False),
#     ]
# )
# def test_isValid(s, expected):
#     sol = Solution()
#     assert sol.isValid(s) == expected

# 🌶️ 155. Min Stack

#
# Задача: реализовать методы за O(1)
#
# 1) Time O(1)  Space O(n)
# class MinStack:
#     def __init__(self):
#         # В стеке храним пары: (значение, минимум на момент вставки)
#         self.stack = []
#
#     def push(self, val: int) -> None:
#         if not self.stack:
#             current_min = val
#         else:
#             current_min = min(val, self.stack[-1][1])
#         self.stack.append((val, current_min))
#
#     def pop(self) -> None:
#         if self.stack:
#             self.stack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1][0]
#
#     def getMin(self) -> int:
#         return self.stack[-1][1]
#
#
# min_stack = MinStack()
# min_stack.pop()
# min_stack.push(3)
# print(min_stack.stack)
# min_stack.pop()
# print(min_stack.stack)
# min_stack.push(4)
# print(min_stack.top())
# print(min_stack.getMin())


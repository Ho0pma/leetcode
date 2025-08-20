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


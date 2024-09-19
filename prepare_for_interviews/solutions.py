# 13. Roman to Integer

# задача: перевести число из римских в обычные.
# 1)
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         d1 = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000,
#         }
#         d2 = {
#             'IV': 4,
#             'IX': 9,
#             'XL': 40,
#             'XC': 90,
#             'CD': 400,
#             'CM': 900,
#         }
#
#         num = 0
#         for i in d2:
#             if i in s:
#                 num += d2[i]
#                 s = s.replace(i, '') # важно присваивать s (тк строка неизменяемый тип)
#
#         for i in s:
#             if i in d1:
#                 num += d1[i]
#
#         return num
#
# s = Solution()
# print(s.romanToInt(s="MCMXCIV"))
#
# 2)
# чуть быстрее
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         d1 = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000,
#         }
#         s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
#         s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
#         s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')
#
#         counter = 0
#         for i in s:
#             counter += d1[i]
#
#         return counter
#
#
# s = Solution()
# print(s.romanToInt(s="MCMXCIV"))
# print(s.romanToInt(s="LVIII"))
# print(s.romanToInt(s="III"))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 20. Valid Parentheses

# задача: проверить корректность написания скобок в строке

# 1)
# просто по фану написал, тут проверят корректность скобок одного типа - ")" и "("
# from collections import deque
#
# class Solution:
#     def isValid(self, s: str) -> bool:
#         dq = deque()
#         for i in s:
#             if i in '(':
#                 dq.append(i)
#             elif dq and i in ')':
#                 dq.pop()
#             else:
#                 return False
#
#         if dq:
#             return False
#         else:
#             return True
#
# s = Solution()
# print(s.isValid('((()))))'))

# 2)
# идея правильная, но слишком похоже на портянку
#
# from collections import deque
#
# class Solution:
#     def isValid(self, s: str) -> bool:
#         if s[0] in ')}]':
#             return False
#
#         brackets_dict = {
#             '(': ')',
#             '[': ']',
#             '{': '}',
#         }
#
#         dq = deque()
#         for i in s:
#             if i in '({[':
#                 dq.append(i)
#             elif dq:
#                 dropped_elem = dq.pop()
#                 if brackets_dict[dropped_elem] != i:
#                     return False
#             else:
#                 return False
#         if dq:
#             return False
#         else:
#             return True
#
# s = Solution()
# print(s.isValid('{[{()}]'))

# 3)
# чуть по другому, более компактно и тп, идея та же. По скорости и памяти одинаково с прошлым
# from collections import deque
#
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = deque()
#         brackets_dict = {
#             ')': '(',
#             '}': '{',
#             ']': '[',
#         }
#         for i in s:
#             if i in brackets_dict:
#                 if not stack or brackets_dict[i] != stack.pop():
#                     return False
#             else:
#                 stack.append(i)
#
#         if stack:
#             return False
#         else:
#             return True
#
#
# s = Solution()
# print(s.isValid('([()]'))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
#


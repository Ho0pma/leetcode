from typing import Optional


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
# 21. Merge Two Sorted Lists

# задача: подается на вход два объекта класса связного списка. Задача объединить эти два списка и отсортировать.
# конечный список должен быть тоже типа LinkedList
# На литкоде чуть по другому просят, тут реализовал самостоятельно класс LinkedList

# 1)
# class Node:
#     def __init__(self, value=None, next_node=None):
#         self.value = value
#         self.next_node = next_node
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def append(self, element):
#         new_node = Node(element)
#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next_node = new_node
#             self.tail = new_node
#
#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node
#             node = node.next_node
#
#
# lst1 = LinkedList()
# lst1.append(1)
# lst1.append(2)
# lst1.append(4)
# print([i.value for i in lst1])  # Вывод: [1, 2, 4]
#
# lst2 = LinkedList()
# lst2.append(1)
# lst2.append(3)
# lst2.append(4)
# print([i.value for i in lst2])  # Вывод: [1, 3, 4]
#
#
# class Solution:
#     def mergeTwoLists(self, list1: LinkedList, list2: LinkedList) -> LinkedList:
#         merged_lst = LinkedList()
#         node1 = list1.head
#         node2 = list2.head
#
#         while node1 and node2:
#             if node1.value < node2.value:
#                 merged_lst.append(node1.value)
#                 node1 = node1.next_node
#             else:
#                 merged_lst.append(node2.value)
#                 node2 = node2.next_node
#
#         while node1:
#             merged_lst.append(node1.value)
#             node1 = node1.next_node
#
#         while node2:
#             merged_lst.append(node2.value)
#             node2 = node2.next_node
#
#         return merged_lst
#
#
# solution = Solution()
# merged_list = solution.mergeTwoLists(lst1, lst2)
# print([i.value for i in merged_list])

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 
# # 13. Roman to Integer
# # Перевод римских чисел в арабские.
# этот вар хороший по памяти, но плохой по скорости
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         result = 0
#         prev_value = 0
#
#         d = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
#
#         for i in s:
#             value = d[i]
#
#             if value > prev_value:
#                 result += value - 2 * prev_value
#                 prev_value = value
#             else:
#                 result += d[i]
#                 prev_value = value
#
#         return result
#
# s = Solution()
# # print(s.romanToInt('III'))
# print(s.romanToInt('LVIII'))
# print(s.romanToInt('MCMXCIV'))


# ВТОРОЙ ВАРИК
# хуже по памяти, но лучше по скорости
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         translations = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         number = 0
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#         for char in s:
#             number += translations[char]
#         return number

# -------------------------------------------------------------------------------------------------------------------- #
# 20. Valid Parentheses

# задача проверить расположены ли скобки правильно

# медленно
# from collections import deque
#
# class Solution:
#     def isValid(self, s: str) -> bool:
#         markers = {'(': ')', '{': '}', '[': ']'}
#
#         dq = deque()
#
#         for i in s:
#             if i in '([{':
#                 dq.append(i)
#             else:
#                 try:
#                     drop = dq.pop()
#                 except IndexError as e:
#                     return False
#                 if i != markers[drop]:
#                     return False
#
#         return False if dq else True
#
#
# s = Solution()
# print(s.isValid('(()'))
# print(s.isValid('()'))
# print(s.isValid('[]{}()'))
# print(s.isValid('())'))

# 2: быстро тк нет блока try/except и в целом мень проверок
# class Solution:
#     def isValid(self, s: str) -> bool:
#
#         # граничная проверка, добавляет скорости
#         if s[0] in (')', '}', ']'):
#             return False
#
#         markers = {')': '(', '}': '{', ']': '['}
#         stack = []
#
#         for i in s:
#             if i in '([{':
#                 stack.append(i)
#             elif stack and markers[i] == stack[-1]:
#                 stack.pop()
#             else:
#                 return False
#
#         return len(stack) == 0
#
#
# s = Solution()
# print(s.isValid('(()'))
# print(s.isValid('()'))
# print(s.isValid('[]{}()'))
# print(s.isValid('())'))

# -------------------------------------------------------------------------------------------------------------------- #
# 21. Merge Two Sorted Lists

# runtime: beats 45% / memory: beats 95%
# задача объединить отсортированные списки
# from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         # создаем фейковую голову, которую не выведем в результате
#         head = ListNode(0)
#         current = head
#
#         while list1 and list2:
#             if list1.val < list2.val:
#                 current.next = list1
#                 list1 = list1.next
#
#             else:
#                 current.next = list2
#                 list2 = list2.next
#
#             current = current.next
#
#         current.next = list1 if list1 else list2
#
#         return head.next
#
#
# # Создание связанных списков list1 и list2
# list1 = ListNode(1)
# list1.next = ListNode(2)
# list1.next.next = ListNode(4)
#
# list2 = ListNode(1)
# list2.next = ListNode(3)
# list2.next.next = ListNode(4)
#
# s = Solution()
# merged_list = s.mergeTwoLists(list1, list2)
#
# while merged_list:
#     print(merged_list.val, end=' ')
#     merged_list = merged_list.next

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ВТОРОЙ ВАРИК
# runtime: beats 85% / memory: beats 95% лучше

# просто лучше реализация
# from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         # создаем фейковую голову, которую не выведем в результате
#         head = current = ListNode()
#
#         while list1 and list2:
#             if list1.val < list2.val:
#                 current.next = list1
#                 list1, current = list1.next, list1
#
#             else:
#                 current.next = list2
#                 list2, current = list2.next, list2
#
#         if list1 or list2:
#             current.next = list1 if list1 else list2
#
#         return head.next
#
#
# # Создание связанных списков list1 и list2
# list1 = ListNode(1)
# list1.next = ListNode(2)
# list1.next.next = ListNode(4)
#
# list2 = ListNode(1)
# list2.next = ListNode(3)
# list2.next.next = ListNode(4)
#
# s = Solution()
# merged_list = s.mergeTwoLists(list1, list2)
#
# while merged_list:
#     print(merged_list.val, end=' ')
#     merged_list = merged_list.next

# -------------------------------------------------------------------------------------------------------------------- #
# 141. Linked List Cycle

# задача определить если в списке цикл

# алгоритм зайца и черепахи. Два указателя (быстрый и медленный) идут от старта с разными шагами. Если происходит момент,
# что указатели оказываются одной позиции - у списка есть цикл. Если быстрый указатель утыкается на None - цикла нет.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# #
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         if not head:
#             return False
#
#         slow = fast = head
#
#         while True:
#             slow = slow.next
#             fast = fast.next
#
#             if not fast:
#                 return False
#
#             fast = fast.next
#
#             if not fast:
#                 return False
#
#             if fast == slow:
#                 return True

# -------------------------------------------------------------------------------------------------------------------- #
# 155. Min Stack

# задача реализовать класс, в котором будет стек с набором функций.
# runtime: beats 5% / memory: beats 93% лучше
# from collections import deque
# class MinStack:
#     def __init__(self):
#         self.dq = deque()
#     def push(self, val: int) -> None:
#         self.dq.append(val)
#     def pop(self) -> None:
#         self.dq.pop()
#     def top(self) -> int:
#         return self.dq[-1]
#     def getMin(self) -> int:
#         return min(self.dq)
#
# m = MinStack()
# m.push(1)
# m.push(2)
# m.push(3)
# print(m.dq)
# m.pop()
# print(m.dq)
# print(m.top())
# print(m.getMin())

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ВТОРОЙ ВАРИК
# runtime: beats 85% / memory: beats 95%
# лучше тем, что мы создали еще один список, в котором будем хранить минимальные значения и не нужно его будет искать

from collections import deque
from typing import List


# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.min_stack = []
#
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if not self.min_stack or val <= self.min_stack[-1]:
#             self.min_stack.append(val)
#
#     def pop(self) -> None:
#         if self.stack.pop() == self.min_stack[-1]:
#             self.min_stack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1]
#     def getMin(self) -> int:
#         return self.min_stack[-1]
#
# m = MinStack()
# m.push(1)
# m.push(2)
# m.push(3)
# print(m.stack)
# m.pop()
# print(m.stack)
# print(m.top())
# print(m.getMin())

# -------------------------------------------------------------------------------------------------------------------- #
# # 169. Majority Element
#
# # задача найти наиболее часто встречаемый элемент в списке
#
# from typing import List
# from collections import Counter
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         return Counter(nums).most_common()[0][0]
#
#
# s = Solution()
# print(s.majorityElement([5, 4, 3, 2, 3, 2, 3, 4]))

# -------------------------------------------------------------------------------------------------------------------- #
# 202. Happy Number

# Return true if n is a happy number, and false if not.

# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1 --> если 1 - тру

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         s = set()
#
#         while True:
#             subtotal = 0
#             for i in str(n):
#                 subtotal += int(i)**2
#
#             if subtotal == 1:
#                 return True
#
#             n = subtotal
#
#             if subtotal in s:
#                 return False
#             else:
#                 s.add(subtotal)

# s = Solution()
# print(s.isHappy(2))

# ВТОРОЙ ВАРИК

# идея такая же, реализация лучше

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         happy_set = set()
#
#         while n != 1 and n not in happy_set:
#             happy_set.add(n)
#             n = sum(int(i)**2 for i in str(n))
#
#         return n == 1
#
# s = Solution()
# print(s.isHappy(19))

# -------------------------------------------------------------------------------------------------------------------- #
# 204. Count Primes

# задача посчитать кол-во простых чисел в заданном диапазоне

# Алгоритм решето-эратосфена
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n <= 1:
#             return 0
#
#         # Создаем список всех чисел от 2 до n
#         primes = [True for _ in range(n + 1)]
#         primes[0] = primes[1] = False
#
#         p = 2
#         while p * p <= n:
#             # Если число p простое, помечаем все его кратные как составные числа
#             if primes[p]:
#                 for i in range(p * p, n + 1, p):
#                     primes[i] = False
#             p += 1
#
#         # Возвращаем список простых чисел
#         return len([i for i in range(2, n) if primes[i] is True])
#
#
# s = Solution()
# print(s.countPrimes(2))

# # ВТОРОЙ ВАРИК (хуже, если мал. диапазон)
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         primes_lst = [i for i in range(2, n) if all(i % j != 0 for j in range(2, i))]
#         return len(primes_lst)
#
# s = Solution()
# print(s.countPrimes(2))

# -------------------------------------------------------------------------------------------------------------------- #
# 242. Valid Anagram

# проверить является ли слово анаграммой
# Пример: cat = tac / anac = cana и тп

# from collections import Counter
#
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#
#         return Counter(s) == Counter(t)

# -------------------------------------------------------------------------------------------------------------------- #
# 371. Sum of Two Integers

# сложить два числа не используя + или -
# Нужно решать как-то через bin
# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         return eval('a + b')
#
# s = Solution()
# print(s.getSum(1, 2))

# -------------------------------------------------------------------------------------------------------------------- #
# 88. Merge Sorted Array

# задача объединить отсортированные массивы. Нужно менять первый список. Не пересоздавать его
# сложное решение
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         a, b, write_index = m - 1, n - 1, m + n - 1
#
#         while b >= 0:
#             if a >= 0 and nums1[a] > nums2[b]:
#                 nums1[write_index] = nums1[a]
#                 a -= 1
#             else:
#                 nums1[write_index] = nums2[b]
#                 b -= 1
#
#             write_index -= 1
#
#         return nums1
#
# s = Solution()
# print(s.merge([1, 2, 3, 0, 0, 0], 3, [1, 2, 3], 3))


# ВТОРОЙ ВАРИК ПРОЩЕ

# проще тем, что просто перенесли второй массив в первый вместо нулей и использовали sort
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         for i in range(n):
#             nums1[m + i] = nums2[i]
#         nums1.sort()
#
#         return nums1
#
# s = Solution()
# print(s.merge([1, 2, 3, 0, 0, 0], 3, [1, 2, 3], 3))

# -------------------------------------------------------------------------------------------------------------------- #
# 1. Two Sum

# задача найти в списке числа которые в сумме будут равны target

# медленное решение:
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i == j:
#                     continue
#
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#
# s = Solution()
# print(s.twoSum([3, 3], 6))

# ВТОРОЙ ВАРИК
# лучше тем, что нет continue, но все равно медленный
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#
# s = Solution()
# print(s.twoSum([3, 3], 6))

# ТРЕТИЙ ВАРИК
# используется хеш-таблица. Вычитаем из target по очереди значения из nums. Если результат есть в таблице - совпало
# если нет - заносим значение с индексом в таблицу.
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numMap = {}
#         n = len(nums)
#
#         for i in range(n):
#             complement = target - nums[i]
#             if complement in numMap:
#                 return [numMap[complement], i]
#             numMap[nums[i]] = i
#
#         return []  # No solution found
#
#
# s = Solution()
# s.twoSum([2, 8, 11, 7], 9)

# -------------------------------------------------------------------------------------------------------------------- #


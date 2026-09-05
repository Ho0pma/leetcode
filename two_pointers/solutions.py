from typing import List, Optional
from collections import Counter

from distlib.version import get_scheme


# 1. ☠️ 26. Remove Duplicates from Sorted Array

# task: remove duplicates from a sorted list. The list must remain the same, i.e. do it in-place.
#       the remaining elements can be ignored, or mark them with "_" as in the example
# example:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]

# example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

# 1) 🌶️ Complexity: Time: O(n), Memory O(1)
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         # discard the edge case
#         if len(nums) == 1:
#             return 1
#
#         # register two pointers (reader - i, writer - slow)
#         # go through the array
#         # if i == i - 1 --> skip
#         # if i != i - 1 --> write the value at index i to pointer slow
#         # this way we get in-place, the first elements are unique
#         # time complexity will = one pass through the array, i.e. O(n)
#         # memory = the introduced variables, i.e. i and slow, i.e. O(1)
#         slow = 1
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 continue
#             else:
#                 nums[slow] = nums[i]
#                 slow += 1
#
#         # second pass through the array for pretty output, can also not do it per the problem
#         for j in range(slow, len(nums)):
#             nums[j] = "_"
#
#         return slow, nums
#
#
# s = Solution()
# print(s.removeDuplicates([0, 1]))  # (2, [0, 1])
# print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # (5, [0, 1, 2, 3, 4, '_', '_', '_', '_', '_'])

# 2) 🫑 using python features
# Complexity: Time: O(n), Memory O(n) (because of creating a new set or dict)
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         unique = list(dict.fromkeys(nums)) # preserve order
#         unique = list(set(nums))           # doesn't preserve order
#         k = len(unique)
#         nums[:k] = unique
#         return k
#
# s = Solution()
# print(s.removeDuplicates([0, 1]))  # (2, [0, 1])
# print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # (5, [0, 1, 2, 3, 4, '_', '_', '_', '_', '_'])
#
# ----------------------------------------------------------------------------------------------------------------------#

# 2. ☠️ 27. Remove Element

# task: an array of unsorted elements (nums) and a number (val) are given
#       need to return the count of elements not equal to val
#       do it in-place

# example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

# example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]

# 1) 🌶️ Complexity: Time: O(n), Memory O(1)
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         # set two pointers: i (moving), slow (writing)
#         # if i matches val - write the value from i at slow
#         slow = 0
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 continue
#             else:
#                 nums[slow] = nums[i]
#                 slow += 1
#
#         # second pass through the array for the pretty output
#         for i in range(slow, len(nums)):
#             nums[i] = '_'
#
#         return slow, nums
#
# 2) same complexity, but reads a bit cleaner
# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         counter = 0
#         for i in nums:
#             if i != val:
#                 nums[counter] = i
#                 counter += 1
#
#         return counter
#
#
# s = Solution()
# print(s.removeElement(nums=[3, 2, 2, 3], val=3))  # (2, [2, 2, '_', '_'])
# print(s.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))  # (5, [0, 1, 3, 0, 4, '_', '_', '_'])

# 3) 🫑 using python features
# Complexity: Time: O(n), Memory O(n) (because of creating a new set or dict)
# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         kept = [i for i in nums if i != val]
#         k = len(kept)
#         nums[:k] = kept # in-place
#         return k
#
#
# s = Solution()
# print(s.removeElement(nums=[3, 2, 2, 3], val=3))  # (2, [2, 2, '_', '_'])
# print(s.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))  # (5, [0, 1, 3, 0, 4, '_', '_', '_'])

# ----------------------------------------------------------------------------------------------------------------------#

# 3) ☠️ 28. Find the Index of the First Occurrence in a String

# task: подается строка1 (haystack) и строка2 (needle).
#       нужно вернуть индекс первого сопоставления needle в haystack

# example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0

# example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1

# 1) 🌶️ Complexity: Time: O(n), Memory O(1)
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         h, n  = len(haystack), len(needle)
#
#         if n == 0:
#             return 0
#         if n > h:
#             return -1
#
#         for i in range(h - n + 1):
#             for j in range(n):
#                 if haystack[i + j] != needle[j]:
#                     break
#             else:
#                 return i # inner loop finished without break → full match
#
#         return -1
#
#
# s = Solution()
# print(s.strStr(haystack="leetcode", needle="leeto")) # -1
# print(s.strStr(haystack="2112", needle="11")) # 1
# #                        012345678910
# print(s.strStr(haystack="mississippi", needle="issipi")) # -1
# print(s.strStr(haystack="a", needle="a")) # 0

# 2) 🫑 using python features
#  Complexity: Time: O(n), Memory O(1)
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.find(needle)
#
#
# s = Solution()
# print(s.strStr(haystack="leetcode", needle="leeto"))
# print(s.strStr(haystack="2112", needle="11"))
# #                        012345678910
# print(s.strStr(haystack="mississippi", needle="issipi"))
# print(s.strStr(haystack="a", needle="a"))

# ----------------------------------------------------------------------------------------------------------------------#

# 4. ☠️ 88. Merge Sorted Array

# task: You are given two integer arrays nums1 and nums2, sorted in non-decreasing order
#       and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#       Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#       The final sorted array should not be returned by the function,
#       but instead be stored inside the array nums1.
#       To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that
#       should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]

# example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]

# 1) 🌶️ Complexity: Time: O(m + n), Memory O(1)
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         i = m - 1
#         j = n - 1
#         # set three pointers: i - last OCCUPIED element in nums1, j - last OCCUPIED element in nums2
#         #                       w - last element in nums1 (writer)
#         # go through the array, check i and j, whichever is greater - put into nums1, decrement the index
#         # when array j is finished - stop
#         for w in range(n + m - 1, -1, -1):
#             if j < 0:
#                 break  # if nums2 is over
#             if i >= 0 and nums1[i] > nums2[j]:
#                 nums1[w] = nums1[i]
#                 i -= 1
#             else:
#                 nums1[w] = nums2[j]
#                 j -= 1
#         # on task no need to return, but i need this for check output
#         return nums1
#
#
# s = Solution()
# print(s.merge(nums1=[1, 2, 0], m=2, nums2=[2, 5, 6, 7], n=3)) # [1, 2, 2, 3, 5, 6]
# print(s.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)) # [1, 2, 2, 3, 5, 6]
# print(s.merge(nums1=[1], m=1, nums2=[], n=0)) # [1]
# print(s.merge(nums1=[0], m=0, nums2=[1], n=1)) # [1]

# 2) 🫑 using python features
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         # 1) Complexity: Time: O(m + n), Memory O(1)
#         from heapq import merge
#         nums1[:] = merge(nums1[:m], nums2[:n])
#         return nums1
#
#         # 2) Complexity: Time: O((m + n) log(m + n)) из-за сортировки лог, Memory O(1)
#         nums1[:] = nums1[:m] + nums2[:n]
#         nums1.sort()
#         return nums1
#
#         # 3) Complexity: Time: O((m + n) log(m + n)), Memory O(1)
#         nums1[m:] = nums2[:n]
#         nums1.sort()
#         return nums1
#
# s = Solution()
# print(s.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)) # [1, 2, 2, 3, 5, 6]

# ----------------------------------------------------------------------------------------------------------------------#

# 5. ☠️ 125. Valid Palindrome

# task: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
#       and removing all non-alphanumeric characters, it reads the same forward and backward.
#       Alphanumeric characters include letters and numbers.
#       Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: s = "race a car"
# Output: false

# Example 3:
# Input: s = " "
# Output: true

# 1) 🌶️ Complexity: Time: O(n), Memory O(1) because in-place
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # two pointers here as well
#         # to do in-place, while loops are necessary
#         # "while you encounter an invalid character" - increment the pointer
#         # compare the start and end of the string via two pointers (left, right)
#         # when left becomes equal to or greater than right - exit
#
#         left, right = 0, len(s) - 1
#         for _ in range(len(s)):
#             while left < right and not s[left].isalnum():
#                 left += 1
#             while left < right and not s[right].isalnum():
#                 right -= 1
#             if left >= right:
#                 break
#             if s[left].lower() != s[right].lower():
#                 return False
#             left += 1
#             right -= 1
#         return True
#
#
# s = Solution()
# print(s.isPalindrome(s="A man, a plan, a canal: Panama"))  # true 'amanaplanacanalpanama'

# 2) 🫑 using python features
# Complexity: Time: O(n), Memory O(n) because an extra string is created
# class Solution:
#     # 1) with logic
#     def isPalindrome(self, s: str) -> bool:
#         # create a new string with only valid characters
#         # go up to the center of the array
#         # the 2nd pointer can also be done like this:
#         # j = l - 1
#         # and decrement it each time, or as in the example l - 1 - i
#
#         new_s = ''.join(ch.lower() for ch in s if ch.isalnum())
#         l = len(new_s)
#         for i in range(l // 2):
#             if new_s[i] != new_s[l - 1 - i]:
#                 return False
#         return True
#
#     # 2) can also be shorter without logic
#     def isPalindrome(self, s: str) -> bool:
#         new_s = ''.join(ch.lower() for ch in s if ch.isalnum())
#         return new_s == new_s[::-1]
#
#     # 3) another way to create the string:
#     def isPalindrome(self, s: str) -> bool:
#         cleaned = ''.join(filter(str.isalnum, s)).lower()  # complains because a string method is passed
#         cleaned = ''.join(
#             filter(lambda ch: ch.isalnum(), s)).lower()  # so the IDE doesn't complain (we pass the element)
#         return cleaned == cleaned[::-1]
#
#
# s = Solution()
# print(s.isPalindrome(s="A man, a plan, a canal: Panama"))  # true 'amanaplanacanalpanama'

# ----------------------------------------------------------------------------------------------------------------------#

# 6. ☠️ 141. Linked List Cycle

# task: подается односвязный список, есть указатели next и val
#       pos в примере показывается только в качестве примера
#       нужно узнать циклический это список или нет
#       решается через идею алгоритма "заяц-черепаха"

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true

# Example 3:
# Input: head = [1], pos = -1
# Output: false

# 1) 🌶️ Complexity: Time: O(n), Memory O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         # идея алгоритма: заяц-черепаха
#         # один идет медленно (slow) - на одно деление вперед
#         # другой быстро (fast) - на два деления вперед
#         # если есть цикл - они гарантировано встречаются если шаг отличается на 1
#         # тк при выходе обоих указателей на "цикл" - скорость их встречи равно 2 - 1
#         # те расстояние между ними всегда сокращается на 1 шаг
#         # те не возможности перепрыгнуть
#         # если поставить разницу больше одного - возможен "перепрыг" f через s
#
#         slow = head
#         fast = head
#
#         while fast and fast.next:
#             slow = slow.next      # +1
#             fast = fast.next.next # +2
#
#             if slow  == fast:
#                 return True
#
#         return False
#
# # 1) пример с циклом
# n1 = ListNode(3)
# n2 = ListNode(2)
# n3 = ListNode(0)
# n4 = ListNode(-4)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n2   # хвост указывает на n2 → цикл
# head = n1
#
# # разбор
# # 1 шаг: s и f оба на head те на 3
# # 2 шаг: s = 2, f = 0
# # 3 шаг: s = 0, f = 2
# # 4 шаг: s = 4, f = 4  - те они только вот тут встретятся
#
# s = Solution()
# print(s.hasCycle(head))

# ----------------------------------------------------------------------------------------------------------------------#

# 7. ☠️ 160. Intersection of Two Linked Lists

# task: Given the heads of two singly linked-lists headA and headB
#       return the node at which the two lists intersect.
#       If the two linked lists have no intersection at all, return null.
#       skipA - кол-во нод до пересечения у А c B
#       skipB - кол-во нод до пересечения у B c A

# example1:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'

# example2:
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Intersected at '2'

# 1) 🌶️ Complexity: Time: O(n + m), Memory O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         # идея в том, чтобы сначала понять длину списка
#         # после этого мы вычисляем разницу (diff)
#         # и двигаем у большего списка diff нод
#         # когда это произойдет - получатся два одинаковых по длине списка, которые пересекаются в какой-то точке
#         # останется только двигать и искать совпадающую ноду
#         # если такой не найдется просто вернуть None
#
#
#         a = headA
#         b = headB
#
#         a_len = 0
#         b_len = 0
#         while a.next:
#             a_len += 1
#             a = a.next
#
#         while b.next:
#             b_len += 1
#             b = b.next
#
#         a = headA
#         b = headB
#
#         if a_len > b_len:
#             for _ in range(a_len - b_len):
#                 a = a.next
#         if b_len > a_len:
#             for _ in range(b_len - a_len):
#                 b = b.next
#
#         while a and b:
#             if a == b:
#                 return a # or b
#             a = a.next
#             b = b.next
#
#         return None

# 2) лучше (тк меньше итераций и кода меньше), сложность та же
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         a, b = headA, headB
#
#         while a != b:
#             a = a.next if a else headB
#             b = b.next if b else headA
#
#         return a

# разбор:
# пример
# A:              8 → 4 → 5 → null
# B: 5 → 6 → 1 →  8 → 4 → 5 → null
#                 ↑ пересечение (один и тот же узел 8)

# шаг	 a	 b	 что случилось
#  1     8   5     разные
#  2     4   6
#  3     5   1
#  4     5   8     a кончился → и переключился на headB
#  5     6   4     a уже по B, b ещё по B
#  6     1   5
#  7     8   8     b кончился → и переключился на headA → встретились

# ----------------------------------------------------------------------------------------------------------------------#

# 8. ☠️ 202. Happy Number

# task: Write an algorithm to determine if a number n is happy.
#       A happy number is a number defined by the following process:
#       Starting with any positive integer, replace the number by the sum of the squares of its digits.
#       Repeat the process until the number equals 1 (where it will stay),
#       or it loops endlessly in a cycle which does not include 1.
#       Those numbers for which this process ends in 1 are happy.
#       Return true if n is a happy number, and false if not.

# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# Example 2:
# Input: n = 2
# Output: false # 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 → ...

# 1) 🌶️ Complexity: Time: O(k · log n) k - чисел в цепочке, Memory O(1)
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         # алгоритм флойда
#         # устанавливаем два указателя: slow и fast
#         # для slow вычисляем следующие число
#         # для fast проводим вычисление два раза
#         # если fast станет = 1 - цикла нет, дойдет первым
#         # если цикл есть - оба в какой-то момент зайдут в цикл и встретятся те станут равны - выводим false
#
#         def next_num(x: int) -> int:
#             total = 0
#             # хитрый способ: сначала вычисляем остаток - заносим в тотал
#             # после делим исходное число, получая целое
#             # таким образом число постепенно уменьшается и придет к нулю
#             while x:
#                 total += (x % 10) ** 2
#                 x //= 10
#             return total
#         slow = n
#         fast = next_num(n)
#         while fast != 1 and slow != fast:
#             slow = next_num(slow)
#             fast = next_num(next_num(fast))
#         return fast == 1
#
#
# s = Solution()
# print(s.isHappy(n=19)) # true
# print(s.isHappy(n=4)) # false

# 2) 🫑 using python features
# Complexity: Time: O(k · log n), Memory O(k)
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         # вариант без двух указателей, а через хранение пройденных значений в сете
#
#         s = set()
#
#         while n != 1:
#             if n in s:
#                 return False
#             s.add(n)
#
#             total = 0
#             while n:
#                 total += (n % 10) ** 2
#                 n = n // 10
#             n = total
#
#         return n == 1
#
#
# s = Solution()
# print(s.isHappy(n=19)) # true
# print(s.isHappy(n=4)) # false

# ----------------------------------------------------------------------------------------------------------------------#

# 9. ☠️ 234. Palindrome Linked List

# task: Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1) in-place
# 🌶️ Complexity: Time: O(n), Memory O(1)
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         if not head or not head.next:
#             return True
#         # 1) найти середину
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         # 2) развернуть вторую половину
#         prev = None
#         while slow:
#             nxt = slow.next
#             slow.next = prev
#             prev = slow
#             slow = nxt
#         # prev — голова развернутой второй половины
#         # 3) сравнить две половины
#         left = head
#         right = prev
#         while right:
#             if left.val != right.val:
#                 return False
#             left = left.next
#             right = right.next
#         return True

# 2) 🫑 using python features
# Complexity: Time: O(n), Memory O(n)
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         # если на память пофиг
#         lst = []
#         while head:
#             lst.append(head.val)
#             head = head.next
#         return lst == lst[::-1]


# 3) если бы можно было поменять структуру по заданию
# class DoublyListNode:
#     def __init__(self, val=0, prev=None, next=None):
#         self.val = val
#         self.prev = prev  # добавил обратный указатель
#         self.next = next
#
# class Solution:
#     def isPalindrome(self, head: DoublyListNode) -> bool:
#         if not head:
#             return True
#
#         # найти tail
#         tail = head
#         while tail.next:
#             tail = tail.next
#
#         # два указателя
#         left = head
#         right = tail
#         while left != right and left.prev != right:
#             # можно еще добавить указатели проверки в while: left and right and..
#             # это на случай если связный список битый
#             if left.val != right.val:
#                 return False
#             left = left.next
#             right = right.prev
#         return True

# ----------------------------------------------------------------------------------------------------------------------#

# 10. ☠️ 283. Move Zeroes

# task: Given an integer array nums, move all 0's to the end of it
#       while maintaining the relative order of the non-zero elements.
#       Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# 1) 🌶️ in-place
# Complexity: Time: O(n), Memory O(1)
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         # идем по списку
#         # если встречаем i != 0 - свапаем с j
#         j = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[j], nums[i] = nums[i], nums[j]
#                 j += 1
#
#         return nums
#
#     def moveZeroes(self, nums: List[int]) -> None:
#         # без свапа
#         j = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[j] = nums[i]
#                 j += 1
#         for i in range(j, len(nums)):
#             nums[i] = 0
#
#         return nums

# 2) 🫑 using python features
# Complexity: Time: O(n), Memory O(n)
#     def moveZeroes(self, nums: List[int]) -> None:
#         nums.sort(key=lambda x: x == 0)
#         return nums
#
# s = Solution()
# print(s.moveZeroes(nums=[0, 1, 0, 3, 12]))
# print(s.moveZeroes(nums=[0]))
# print(s.moveZeroes(nums=[0, 0, 1]))

# ----------------------------------------------------------------------------------------------------------------------#

# 11. ☠️ 344. Reverse String

# task: Write a function that reverses a string. The input string is given as an array of characters s.
#       You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1
# Input: s = ["h", "e", "l", "l", "o"]
# Output: ["o", "l", "l", "e", "h"]

# Example 2
# Input: s = ["H", "a", "n", "n", "a", "h"]
# Output: ["h", "a", "n", "n", "a", "H"]

# 1) 🌶️ in-place
# Complexity: Time: O(n), Memory O(1)
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         # два указателя с разных концов
#         # 1)
#         right = len(s) - 1
#         for left in range(len(s)):
#             if left >= right:
#                 break
#             else:
#                 s[left], s[right] = s[right], s[left]
#                 right -= 1
#
#         # 2) более каноничный вариант
#         left, right = 0, len(s) - 1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1
#
#         return s
#
#
# s = Solution()
# print(s.reverseString(s=["h", "e", "l", "l", "o"])) # ["o", "l", "l", "e", "h"]
# print(s.reverseString(s=["H", "a", "n", "n", "a", "h"])) # ["h", "a", "n", "n", "a", "H"]

# 2) 🫑 using python features
# Complexity: Time: O(n), Memory O(n)
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         # s.reverse()   O(1) — меняет тот же список
#         # s[::-1]       O(n) — новый список
#         # reversed(s)   итератор, O(1), но нужно куда - то записать
#
#         # in-pace:
#         s = ["h", "e", "l", "l", "o"]
#         old_id = id(s)
#         s[:] = reversed(s)
#         print(s)  # ['o', 'l', 'l', 'e', 'h']
#         print(id(s) == old_id)  # True
#
#         # non in-pace:
#         s = reversed(s)  # s — уже другой объект (итератор)
#         s = s[::-1]  # новый список
#
#
# s = Solution()
# print(s.reverseString(s=["h", "e", "l", "l", "o"])) # ["o", "l", "l", "e", "h"]
# print(s.reverseString(s=["H", "a", "n", "n", "a", "h"])) # ["h", "a", "n", "n", "a", "H"]

# ----------------------------------------------------------------------------------------------------------------------#

# 12. ☠️ 345. Reverse Vowels of a String

# task: Given a string s, reverse only all the vowels in the string and return it.
#       The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases,
#       more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
#
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# 1) 🌶️ best approach
# Complexity: Time: O(n), Memory O(n)
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         l = list(s)
#         vowels = set('aeiou') # быстрее in
#         left = 0
#         right = len(s) - 1
#
#         while left < right:
#             while left < right and l[left].lower() not in vowels:
#                 left += 1
#             while left < right and l[right].lower() not in vowels:
#                 right -= 1
#
#             l[left], l[right] = l[right], l[left]
#             left += 1
#             right -= 1
#
#         return ''.join(l)
#
#
# s = Solution()
# print(s.reverseVowels(s="IceCreAm"))  # "AceCreIm"
# print(s.reverseVowels(s="leetcode"))  # "leotcede"

# ----------------------------------------------------------------------------------------------------------------------#

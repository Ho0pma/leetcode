from typing import List
from collections import Counter


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

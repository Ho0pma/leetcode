# 1. Two Sum / Easy
from re import search
# задача: задается список и target. Нужно найти пары чисел, которые в сумме = target и вывести их индексы.
# 1) O(n^2)
# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for index_1, value_1 in enumerate(nums):
#             for index_2, value_2 in enumerate(nums):
#                 if value_1 + value_2 == target and index_1 != index_2:
#                     return [index_1, index_2]
#
#
# s = Solution()
# print(s.twoSum([2, 7, 11, 15], 9))
# print(s.twoSum([3, 2, 4], 6))
# print(s.twoSum([3, 3], 6))

# 2) Two-pass Hash Table
# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d = {}
#         n = len(nums)
#
#         for i in range(n):
#             d[nums[i]] = i
#
#         for i in range(n):
#             diff = target - nums[i]
#             if diff in d and d[diff] != i:
#                 return [i, d[diff]]
#
#         return []
#
#
# s = Solution()
# print(s.twoSum([2, 7, 11, 15], 9))
# print(s.twoSum([3, 2, 4], 6))
# print(s.twoSum([3, 3], 6))

# 3) One-pass Hash Table
# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d = {}
#         n = len(nums)
#
#         for i in range(n):
#             diff = target - nums[i]
#             if diff in d:
#                 return [d[diff], i]
#
#             d[nums[i]] = i
#
#
# s = Solution()
# print(s.twoSum([2, 7, 11, 15], 9))
# print(s.twoSum([3, 2, 4], 6))
# print(s.twoSum([3, 4, 3], 6))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# 26. Remove Duplicates from Sorted Array / EASY

# задача: на вход поступает массив, в нем числа, сортированные по возрастанию, повторяются. Нужно сделать так, чтобы
# в том же массиве остались только уникальные числа и размер массива остался изначальным (дубликаты поменять на любой
# символ) Те из [1, 1, 2] --> [1, 2, _]. На выходе вывести кол-во уникальных элементов.

# 1)
# from typing import List
#
#
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         unique_nums = sorted(set(nums))
#         nums_len = len(nums)
#         unique_nums_len = len(unique_nums)
#         counter = nums_len - unique_nums_len
#         nums[:] = unique_nums + ['_'] * counter
#         print(nums)
#         return unique_nums_len
#
#
# s = Solution()
# print(s.removeDuplicates([-1, 0, 0, 0, 0, 3, 3]))
# print(s.removeDuplicates([1, 1, 2, 3]))
# print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

# 2) ???
# from typing import List
#
#
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         j = 1
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 nums[j] = nums[i]
#             j += 1
#         print(nums)
#         return j
#
#
# s = Solution()
# print(s.removeDuplicates([-1, 0, 0, 0, 0, 3, 3]))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 27. Remove Element / EASY

# задача: подается nums и val. Нужно не создавая новый массив убрать из него val и вернуть кол-во уникальных элементов.

# 1)
# from typing import List
#
#
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         nums_without_val = [i for i in nums if i != val]
#         nums_without_val_len = len(nums_without_val)
#         nums[:] = nums_without_val + ['_'] * nums_without_val_len
#         print(nums)
#         return nums_without_val_len
#
#
# s = Solution()
# print(s.removeElement([3, 2, 2, 3], 3))

# 2) мне не очень нравится, но работает
# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         c = 0
#         for i in nums:
#             if i != val:
#                 nums[c] = i
#                 c += 1
#         print(nums)
#         return c
#
#
# s = Solution()
# print(s.removeElement([3, 2, 2, 3], 3))
# print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# 35. Search Insert Position / EASY

# задача: подается упорядоченный массив и target. Если в массиве есть target - вывести его индекс. Если нет - найти
# место где нужно вставить число в порядке возрастания

# 1)
# from typing import List
#
#
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#         else:
#             for i in nums:
#                 if target < i:
#                     return nums.index(i)
#
#             return len(nums) # если target больше всех в lst
#
#
# s = Solution()
# print(s.searchInsert([1, 3, 5, 6], 5))
# print(s.searchInsert([1, 3, 5, 6], 2))
# print(s.searchInsert([1, 3, 5, 6], 7))

# 2)
# такой же вар как и выше, только лучше структура, хотя есть блок try, что хуже
# from typing import List
#
#
# class Solution:
#     def searchInsert(self, nums: list[int], target: int) -> int:
#
#         if target not in nums:
#             for i in range(len(nums)):
#                 if target < nums[i]:
#                     return i
#
#         try:
#             return nums.index(target)
#         except:
#             return len(nums)
#
# s = Solution()
# print(s.searchInsert([1, 3, 5, 6], 5))
# print(s.searchInsert([1, 3, 5, 6], 2))
# print(s.searchInsert([1, 3, 5, 6], 7))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 66. Plus One / EASY

# задача:

# 1) подается массив из чисел: [1, 2, 3] = 123. Нужно вернуть массив [1, 2, 4] = 124 те + 1
# from typing import List
#
#
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         next_digit = int(''.join(str(i) for i in digits)) + 1
#         return [int(i) for i in str(next_digit)]
#
#
# s = Solution()
# print(s.plusOne([1, 2, 3]))
# print(s.plusOne([4, 3, 2, 1]))
# print(s.plusOne([9]))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 88. Merge Sorted Array / Easy

# задача: подается два массива и два числа. К примеру: [1, 2, 3, 0, 0] и к нему число m=3
# это означает, что в массиве 3 числа, оставшиеся нули - пустое место.
# Нужно склеить эти два массива в один в порядке возрастания и сделать это все в nums1 (те не создавать новый)

# 1)
# from typing import List
#
#
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         nums1_plus_nums2 = sorted(nums1[:m] + nums2[:n])
#         nums1[:] = nums1_plus_nums2
#         print(nums1)
#
#
# s = Solution()
# s.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
# s.merge(nums1=[1], m=1, nums2=[], n=0)
# s.merge(nums1=[0], m=0, nums2=[1], n=1)
# s.merge(nums1=[-1, 0, 0, 3, 3, 3, 0, 0, 0], m=6, nums2=[1, 2, 2], n=3)

# 2)
# решение сильно лучше, чем выше

# from typing import List
#
#
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         # указатели, чтобы достучаться до последних элементов в списках
#         pointer1 = m - 1
#         pointer2 = n - 1
#
#         # благодаря этому указателю идем с конца списка и перезаписываем элементы по очереди
#         overwrite_pointer = m + n - 1
#
#         while pointer2 >= 0:
#             if pointer1 < 0 or nums2[pointer2] > nums1[pointer1]:
#                 nums1[overwrite_pointer] = nums2[pointer2]
#                 pointer2 -= 1
#             else:
#                 nums1[overwrite_pointer] = nums1[pointer1]
#                 pointer1 -= 1
#
#             overwrite_pointer -= 1
#
#         print(nums1)
#
#
# s = Solution()
# s.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
# s.merge(nums1=[1], m=1, nums2=[], n=0)
# s.merge(nums1=[0], m=0, nums2=[1], n=1)
# s.merge(nums1=[-1, 0, 0, 3, 3, 3, 0, 0, 0], m=6, nums2=[1, 2, 2], n=3)

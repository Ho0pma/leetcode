# 1. Two Sum / Easy

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
# 
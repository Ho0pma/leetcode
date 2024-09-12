# 1. Two Sum / Easy
from itertools import count
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


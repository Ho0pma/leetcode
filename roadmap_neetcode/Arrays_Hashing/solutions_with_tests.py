import collections
from typing import List
from collections import Counter, defaultdict

import pytest

# 🌶️ 242. Valid Anagram
#
# Задача: подается две строки s и t. Нужно определить являются ли они анаграммой (когда из букв
# одного слова можно составить другие, длина должна совпадать)
#
# 1) Time O(n) Space O(1)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         print()
#         s_dict = defaultdict(int)
#         for i in s:
#             s_dict[i] = s_dict[i] + 1
#         print(s_dict)
#
#         t_dict = defaultdict(int)
#         for i in t:
#             t_dict[i] = t_dict[i] + 1
#         print(t_dict)
#
#         return s_dict == t_dict
#
#
# @pytest.mark.parametrize(
#     "word1, word2, expected",
#     [
#         ("anagram", "nagaram", True),
#         ("rat", "car", False),
#     ]
# )
# def test_is_anagram(word1, word2, expected):
#     s = Solution()
#     assert s.isAnagram(word1, word2) == expected

########################################################################################################################

# 🌶️ 1. Two Sum
#
# Задача: подается список интов (nums) и target. Нужно найти такие два инта, которые в сумме дают
# target. Вернуть индексы этих чисел
#
# 1) Time O(n) Space O(n)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         print()
#         nums_set = {}
#         for i in range(len(nums)):
#             diff = target - nums[i]
#             if diff in nums_set:
#                 return [i, nums_set[diff]]
#             nums_set[nums[i]] = i
#
#         return []
#
# @pytest.mark.parametrize(
#     "nums, target, expected",
#     [
#         ([3, 2, 4], 6, {(2, 1), (1, 2)}),
#         ([3, 3], 6, {(0, 1), (1, 0)}),
#         ([2, 7, 11, 15], 9, {(0, 1), (1, 0)}),
#     ]
# )
# def test_two_sum(nums, target, expected):
#     s = Solution()
#     assert tuple(s.twoSum(nums, target)) in expected

########################################################################################################################


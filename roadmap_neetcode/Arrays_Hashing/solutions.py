from typing import List
from collections import Counter

# 217. Contains Duplicate

# Задача: есть список nums. Если в нем есть дубликаты - вернуть True, если нет - False

# 1) Time O(n) Space O(n)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hash_table = set()
#
#         for i in nums:
#             if i not in hash_table:
#                 hash_table.add(i)
#             else:
#                 return True
#
#         return False
#
#
# s = Solution()
# print(s.containsDuplicate(nums=[1, 2, 3, 1])) # true
# print(s.containsDuplicate(nums=[1, 2, 3, 4])) # false
# print(s.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2])) # true

# 2) Time O(n) Space O(n)
# -- То же самое, только чуть лучше написано
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hash_table = set()
#
#         for i in nums:
#             if i in hash_table:
#                 return True
#             hash_table.add(i)
#
#         return False
#
#
# s = Solution()
# print(s.containsDuplicate(nums=[1, 2, 3, 1])) # true
# print(s.containsDuplicate(nums=[1, 2, 3, 4])) # false
# print(s.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2])) # true

#####################################################################################################

# 242. Valid Anagram

# Задача: подается две строки s и t. Нужно определить являются ли они анаграммой (когда из букв
# одного слова можно составить другие, длина должна совпадать)

# 1) Time O(n) Space O(1)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(t) != len(s):
#             return False
#
#         return Counter(s) == Counter(t)
#
#
# s = Solution()
# print(s.isAnagram(s="anagram", t="nagaram"))  # true
# print(s.isAnagram(s="rat", t="car"))  # false

# 2) Time O(n) Space O( 1)
# -- не используя Counter
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(t) != len(s):
#             return False
#
#         hash_map_s, hash_map_t = {}, {}
#
#         for i in s:
#             if i in hash_map_s:
#                 hash_map_s[i] = hash_map_s[i] + 1
#             else:
#                 hash_map_s[i] = 1
#
#         for i in t:
#             if i in hash_map_t:
#                 hash_map_t[i] = hash_map_t[i] + 1
#             else:
#                 hash_map_t[i] = 1
#
#         return hash_map_s == hash_map_t
#
# s = Solution()
# print(s.isAnagram(s="anagram", t="nagaram"))  # true
# print(s.isAnagram(s="rat", t="car"))  # false

#####################################################################################################

#

# Задача:

# 1) Time O(n) Space O(1)

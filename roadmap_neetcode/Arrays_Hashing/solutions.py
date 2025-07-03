from typing import List
from collections import Counter, defaultdict


# 217. Contains Duplicate

# Задача: есть список nums. Если в нем есть дубликаты - вернуть True, если нет - False
#
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
#
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
#
# Задача: подается две строки s и t. Нужно определить являются ли они анаграммой (когда из букв
# одного слова можно составить другие, длина должна совпадать)
#
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
#
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

# 1. Two Sum
#
# Задача: подается список интов (nums) и target. Нужно найти такие два инта, которые в сумме дают
# target. Вернуть индексы этих чисел
#
# 1) Time O(n) Space O(n)
# -- two pass hash table
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_map = {}
#
#         for i in range(len(nums)):
#             hash_map[nums[i]] = i
#
#         for i in range(len(nums)):
#             diff = target - nums[i]
#             if diff in hash_map and i != hash_map[diff]:
#                 return [i, hash_map[diff]]
#
#         return []
#
#
# s = Solution()
# print(s.twoSum(nums=[2, 7, 11, 15], target=9))  # [0,1]
# print(s.twoSum(nums=[3, 2, 4], target=6))  # [1,2]
# print(s.twoSum(nums=[3, 3], target=6))  # [0,1]
#
# 2) Time O(n) Space O(n)
# -- one pass hash table
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_map = {}
#
#         for i in range(len(nums)):
#             diff = target - nums[i]
#
#             if diff in hash_map:
#                 return [i, hash_map[diff]]
#             hash_map[nums[i]] = i
#
#         return []
#
#
# s = Solution()
# print(s.twoSum(nums=[2, 7, 11, 15], target=9))  # [0,1]
# print(s.twoSum(nums=[3, 2, 4], target=6))  # [1,2]
# print(s.twoSum(nums=[3, 3], target=6))  # [0,1]

#####################################################################################################

# 49. Group Anagrams

# Задача:

# PRAC:
# 1)
# d = {}
# d['a'].append(1) # error тк нет а: []
# print(d)
# 2)
# d = {'a': []}
# d['a'].append(1) # {'a': [1]} --> добавит тк уже был ключ  'a'
# print(d)
# 3)
# d = defaultdict(list) # если ключа еще не было в дикте - автоматически создаст для него значение list
# d['a'].append(1) # defaultdict(<class 'list'>, {'a': [1]})
# print(d)
# d['b'] = 1 # не будет создавать значение типа list, просто создаст 'b': 1
# print(d) # defaultdict(<class 'list'>, {'a': [1], 'b': 1})


# 1) Time O(n) Space O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:






s = Solution()
print(s.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])) # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]



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

# 🌶️ 49. Group Anagrams

# Задача: подается список (strs), состоящий из слов. Нужно составить новый список, комбинирующий анаграммы
# вместе, см пример в конце, сразу понятно.

# 1) Time O(n * k) Space O(n * 26)
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         print()
#         res = defaultdict(list)
#         for word in strs:
#             char_counter_list = [0] * 26
#             for i in word:
#                 char_counter_list[(ord(i) - ord('a'))] += 1
#
#             res[tuple(char_counter_list)].append(word)
#
#         return list(res.values())

# 2) плохой вар из-за сортировки
# TIME: O(N * K log K)
# N — количество слов
# K — средняя длина слова
# Counter — O(K)
# sorted(items()) — O(K log K)
# SPACE: O(N * K)
# K - кол-во созданных тюплов
# N - кол-во слов
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         print()
#         res = defaultdict(list)
#         for word in strs:
#             char_counter_list = sorted(Counter(word).items())
#             print(char_counter_list)
#
#             res[tuple(char_counter_list)].append(word)
#         print(res)
#
#         return list(res.values())
#
# def sort_output(anagram_list):
#     for i in anagram_list:
#         i.sort()
#     anagram_list.sort()
#
#     return anagram_list
#
# @pytest.mark.parametrize(
#     "strs, expected",
#     [
#         (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
#         ([""], [[""]]),
#         (["a"], [["a"]]),
#     ]
# )
# def test_groupAnagrams(strs, expected):
#     s = Solution()
#     assert sort_output(s.groupAnagrams(strs)) == sort_output(expected)

#####################################################################################################

# 🌶️ 347. Top K Frequent Elements

# Задача: подается список интов (nums) и таргет (k). Нужно найти k максимальных вхождений в массив
# и вывести эти числа
# те если nums=[4, 1, -1, 2, -1, 2, 3] и k=2
# Counter({-1: 2, 2: 2, 4: 1, 1: 1, 3: 1}) -- топ два вхождения имеют -1 и 2

# Time O(n log n)  Space O(n) (за хранение counter)
class Solution:
    # 1) sorting + Counter
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     # print()
    #     # print(Counter(nums))
    #     # counter_nums = sorted(Counter(nums).items(), key=lambda x: x[1])
    #     # print(counter_nums)
    #     # print([i for i, j in counter_nums][-k:])
    #     # return [i for i, j in counter_nums][-k:]
    #
    #     # можно наоборот, сортировать в другую сторону, срез обычный (а не с конца)
    #     print()
    #     print(Counter(nums))
    #     counter_nums = sorted(Counter(nums).items(), key=lambda x: -x[1])
    #     print(counter_nums)
    #     print([i for i, j in counter_nums][:k])
    #     return [i for i, j in counter_nums][:k]

    # 2) bucket sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        print()
        bucket = [[] for _ in range(len(nums) + 1)]  # +1, т.к. частота может быть == len(nums)
        print(bucket) # [[], [], [], [], [], [], [], []]

        nums_counter = {}
        for i in nums:
            nums_counter[i] = nums_counter.get(i, 0) + 1
        print(nums_counter) # {4: 1, 1: 1, -1: 2, 2: 2, 3: 1}

        for i, j in nums_counter.items():
            bucket[j].append(i)
        print(bucket) # [[], [4, 1, 3], [-1, 2], [], [], [], []]

        res = []
        # для кейса когда {1: 3, 2: 2, 3: 1} и t=2 (находятся в разных корзинах)
        # Если bucket = [[], [1], [2], [3]], то:
        # range(len(bucket) - 1, 0, -1)
        # -> range(3, 0, -1)
        # -> 3, 2, 1
        for freq in range(len(bucket) - 1, 0, -1):  # от самых больших частот к меньшим
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    print("final result:", res)
                    return res

        print("final result (after loop):", res)
        return res

@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 1, -1, 2, -1, 2, 3], 2, ([-1, 2], [2, -1])),
        ([1, 1, 1, 2, 2, 3], 2, ([1, 2], [2, 1])),
        ([1], 1, ([1],)),
        ([], 1, ([],)),
    ]
)
def test_topKFrequent(nums, target, expected):
    s = Solution()
    assert s.topKFrequent(nums, target) in expected

















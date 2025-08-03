import collections
from typing import List
from collections import Counter, defaultdict


# 🌶️ 217. Contains Duplicate

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

# 🌶️ 242. Valid Anagram
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

# 🌶️ 1. Two Sum
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

# 🌶️ 49. Group Anagrams

# Задача: подается список (strs), состоящий из слов. Нужно составить новый список, комбинирующий анаграммы
# вместе, см пример в конце, сразу понятно.

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


# 1) Time O(n * k) Space O(n * k)
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # создаем дикт, который для новых элементов создает по умолчанию пустой список
#         result_dict = defaultdict(list)
#
#         for word in strs:
#             # список для хранения кол-ва символов в слове
#             char_counter_lst = [0] * 26
#             for i in word:
#                 char_counter_lst[ord(i) - ord('a')] += 1
#
#             # сохраняем полученный список в качестве ключа, на месте значения - слово, что "просчитывали по буквам"
#             # tuple тк на месте ключа может изменяемого типа данных
#             result_dict[tuple(char_counter_lst)].append(word)
#
#         return list(result_dict.values())
#
#
# s = Solution()
# print(s.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])) # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

#####################################################################################################

# 🌶️ 347. Top K Frequent Elements

# Задача: подается список интов (nums) и таргет (k). Нужно найти k максимальных вхождений в массив
# и вывести эти числа
# те если nums=[4, 1, -1, 2, -1, 2, 3] и k=2
# Counter({-1: 2, 2: 2, 4: 1, 1: 1, 3: 1}) -- топ два вхождения имеют -1 и 2

# Time O(n log n)  Space O(n) (за хранение counter)
# 1) sorting + Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         nums_counter = Counter(nums)
#         print(nums_counter)
#         sorted_nums = sorted(nums_counter.items(), key=lambda x: x[1])
#         return [i for i, j in sorted_nums][-k:]
#
#
# s = Solution()
# print(s.topKFrequent(nums=[4, 1, -1, 2, -1, 2, 3], k=2))  # [-1, 2]
# print(s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))  # [1,2]
# print(s.topKFrequent(nums=[1], k=1))  # [1]
# print(s.topKFrequent(nums=[], k=1))  # []

# 2) Time O(n)  Space O(n)
# bucket sorting
# Идея bucket sort:
# мы заранее знаем диапазон возможных значений ключа, и для каждого значения создаём своё «ведро» (bucket), куда складываем элементы.
# в конце проходим все ведра по порядку и извлекаем элементы.
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#
#         # тут будут храниться значения
#         freq = [[] for i in range(len(nums) + 1)]
#         print(freq)
#
#         # работает как Counter, только не сортирует по ключам
#         # # count[num] = сколько раз встретился num
#         for num in nums:
#             count[num] = 1 + count.get(num, 0)
#         print(count)
#
#         # freq[cnt] = список чисел, у которых частота cnt
#         for num, cnt in count.items():
#             freq[cnt].append(num)
#         print(freq)
#
#         res = []
#         # проходим по ведрам с максимальной частотой к минимальной
#         for i in range(len(nums), 0, -1):
#             for j in freq[i]:
#                 res.append(j)
#                 if len(res) == k:
#                     return res
#
#
# s = Solution()
# print(s.topKFrequent(nums=[4, 1, -1, 2, -1, 2, 3], k=2))  # [-1, 2]
# print(s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))  # [1,2]
# print(s.topKFrequent(nums=[1], k=1))  # [1]
# print(s.topKFrequent(nums=[], k=1))  # []
# print(s.topKFrequent(nums=[1, 2, 3, 1, 3, 4, 4, 4], k=3))  # [test]

#####################################################################################################

# 🌶️ 238. Product of Array Except Self

# Задача: подается список интов (nums), нужно вернуть список состоящий из перемноженных интов (из nums)
# кроме текущего элемента
#
# tip:
# Для каждого элемента посчитай что-то относительно всех остальных элементов
# (сумму, произведение, максимум, количество...)
# — это прям сигнал, что нужно использовать префиксы и суффиксы
#
# pref[i] = произведение всего ЛЕВЕЕ позиции i (не включая i).
# suff[i] = произведение всего ПРАВЕЕ позиции i.

# 1) Time O(n)  Space O(n)
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#
#         prefix = [1] * n
#         for i in range(1, n):
#             print(i)
#             prefix[i] = prefix[i - 1] * nums[i - 1]
#         print(prefix)
#
#         suffix = [1] * n
#         for i in range(n - 2, -1, -1):
#             print(i)
#             suffix[i] = suffix[i + 1] * nums[i + 1]
#         print(suffix)
#
#         res = []
#         for i in range(n):
#             res.append(prefix[i] * suffix[i])
#
#         return res
#
#
# s = Solution()
# print(s.productExceptSelf(nums=[1, 2, 3, 4])) # [24,12,8,6]
# print(s.productExceptSelf(nums=[-1, 1, 0, -3, 3])) # [0,0,9,0,0]

#####################################################################################################

# 🌶️ 36. Valid Sudoku

# Задача: задача определить валидное ли судоку по правилам
# 1) Each row must contain the digits 1-9 without repetition.
# 2) Each column must contain the digits 1-9 without repetition.
# 3) Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
# squares - это определение квадратов 3х3
#      0           1         2
#  0  box(0,0)  box(1,0)  box(2,0)
#  1  box(0,1)  box(1,1)  box(2,1)
#  2  box(0,2)  box(1,2)  box(2,2)

# если поделить индекс, скажем row на общее кол-во боксов,
# то получим индекс бокса по row
# то же самое можно сделать и с column
# к примеру имеем индексы row = 5 и col = 2
# --> (5 // 3, 2 // 3) --> box(1, 0)

# PRAC
# r = {0: {'5', '3'}}
# print('5' in r[0])

# 1) Time O(9^2)  Space O(9^2)
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows = collections.defaultdict(set)
#         cols = collections.defaultdict(set)
#         squares = collections.defaultdict(set) # key = (r // 3, c // 3)
#
#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == '.':
#                     continue
#                 if (board[r][c] in rows[r] or
#                     board[r][c] in cols[c] or
#                     board[r][c] in squares[(r // 3, c // 3)]
#                 ):
#                     return False
#                 rows[r].add(board[r][c])
#                 cols[c].add(board[r][c])
#                 squares[(r // 3, c // 3)].add(board[r][c])
#
#         return True
#
#
# s = Solution()
# print(s.isValidSudoku(board=[
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
# ]))  # True
#
# print(s.isValidSudoku(board=
#                       [     ["8", "3", ".", ".", "7", ".", ".", ".", "."]
#                           , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
#                           , [".", "9", "8", ".", ".", ".", ".", "6", "."]
#                           , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
#                           , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
#                           , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
#                           , [".", "6", ".", ".", ".", ".", "2", "8", "."]
#                           , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
#                           , [".", ".", ".", ".", "8", ".", ".", "7", "9"]])) # False

#####################################################################################################

# 🌶️ 36. 128. Longest Consecutive Sequence

# Задача: подается not-sorted массив интов (nums). Нужно найти максимальную последовательность в этом массиве
# Решить за O(n)

# 1) Time O(n)  Space O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        max_counter = 0

        for i in nums_set:
            if i - 1 not in nums_set:
                x = i
                counter = 1
                while x + 1 in nums_set:
                    counter += 1
                    x += 1
                max_counter = max(counter, max_counter)

        return max_counter


s = Solution()
print(s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))  # 4
print(s.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
print(s.longestConsecutive(nums=[1, 0, 1, 2]))  # 3


















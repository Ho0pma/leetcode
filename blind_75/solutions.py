from typing import List


# # 1. 128. Longest Consecutive Sequence
# 1) Time: O(n log n) | Space: O(n)
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#
#         sorted_nums = sorted(set(nums))
#
#         current = 1
#         longest = 1
#
#         for i in range(1, len(sorted_nums)):
#             if sorted_nums[i] == sorted_nums[i - 1] + 1:
#                 current += 1
#                 longest = max(longest, current)
#             else:
#                 current = 1
#
#         return longest
#
#
# s = Solution()
# print(s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
# print(s.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
# print(s.longestConsecutive(nums=[1, 0, 1, 2]))

# 2) Time: O(n) | Space: O(n) - best
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:  # отбойник на пустой массив
#             return 0
#
#         num_set = set(nums)     # создаем хэш таблицу из поступаемого массива
#         longest_seq_counter = 1
#
#         # Идем по сету (сложность O(n)). Ифом проверяем является ли текущий элемент стартом какой-то последовательности
#         # Далее делаем копию элемента (x) и создаем счетчик текущей последовательности.
#         # В цикле while работаем в другую сторону - проверяем есть ли побольше элемент (x + 1). Если есть - начинаем
#         # считать размер последовательности (current_seq_counter). Если нет - сравниваем longest_seq_counter и current
#         for element in num_set:
#             if element - 1 not in num_set:  # начало последовательности
#                 x = element
#                 current_seq_counter = 1
#                 while x + 1 in num_set: # считаем кол-во элементов в текущей последовательности
#                     x += 1
#                     current_seq_counter += 1
#                 longest_seq_counter = max(current_seq_counter, longest_seq_counter)
#
#             return longest_seq_counter
#
#
# s = Solution()
# print(s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
# print(s.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
# print(s.longestConsecutive(nums=[1, 0, 1, 2]))

########################################################################################################################

# # 2. 1. Two Sum
# 1) Brute force  Time: O(n^2) | Space: O(1)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # в первом цикле идет по всем элементам nums (от 0, до конца)
#         # во втором цикле идет по элементам nums, но уже с i + 1 до конца. Чтобы избежать повторных проверок и не
#         # попадались одинаковые элементы i и j.
#         # к примеру:
#         # i = 0 -> элемент = 2 -> пары: [2 и 7, 2 и 11, 2 и 15]
#         # i = 1 -> элемент = 7 -> пары: [7 и 11, 7 и 15, и могла быть 7 и 2, что уже была выше, если рассматривать все]
#         # далее просто ищем верное равенство 2 (i) = 9 (target) - 7 (j) и выводим
#         # если не нашло - вывод пустого списка
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]
#         return []
#
#
# s = Solution()
# print(s.twoSum(nums=[2, 7, 11, 15], target=9)) # [0, 1]
# print(s.twoSum(nums=[3, 2, 4], target=6)) # [1, 2]
# print(s.twoSum(nums=[3, 3], target=6)) # [0, 1]

# 2) Two-pass Hash Table Time: O(n) | Space: O(n)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # создается хэш таблица - дикт, в который через цикл заносятся значения и индексы из поступающего массива
#         # пример: hashmap = {2: 0, 7: 1, 11: 2, 15: 3} те значение из nums (ключ): индекс из nums (значение)
#         # далее, во втором цикле на каждом шаге мы вычисляем complement и проверяем есть ли такой ключ в хэш таблице.
#         # если есть и значение этого ключа (индекс из nums) != текущему индексу в цикле (чтобы не брались одинаковые
#         # индексы) - выводим полученные индексы
#         hashmap = {}
#
#         for i in range(len(nums)):
#             hashmap[nums[i]] = i
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap and hashmap[complement] != i:
#                 return [i, hashmap[complement]]
#
#         return []
#
#
# s = Solution()
# print(s.twoSum(nums=[2, 7, 11, 15], target=9)) # [0, 1]
# print(s.twoSum(nums=[3, 2, 4], target=6)) # [1, 2]
# print(s.twoSum(nums=[3, 3], target=6)) # [0, 1]

# 3) One-pass Hash Table Time: O(n) | Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # тут идея в том, что мы делаем проверку что и в предыдущем варе только сразу
        # на моменте создания хэш таблицы.
        # пример: nums [2, 7, 11, 15]
        # при первом проходе: i=0, complement = 7, такого нет в хэш таблице, значит
        # заносится {2(значение): 0(индекс)}.
        # второй: i=1, complement = 2 - в хэш таблице есть - выводим
        # И главное еще тут не нужна проверка на одинаковость индексов. Они точно не могут
        # быть равны тк i постоянно растет и в кэш таблицу заносятся всегда разные i.
        hashtable = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashtable:
                return [i, hashtable[complement]]
            hashtable[nums[i]] = i
        return []


s = Solution()
print(s.twoSum(nums=[2, 7, 11, 15], target=9)) # [0, 1]
print(s.twoSum(nums=[3, 2, 4], target=6)) # [1, 2]
print(s.twoSum(nums=[3, 3], target=6)) # [0, 1]
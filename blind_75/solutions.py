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

# # 2.
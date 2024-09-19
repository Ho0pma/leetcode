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
#
# 3)
# такой же как второй варик, только через цикл for. С while лучше тк меньше итераций

# from typing import List
#
#
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         pointer1 = m - 1
#         pointer2 = n - 1
#
#         overwrite_pointer = m + n - 1
#
#         for _ in range(n + m):
#             if pointer2 < 0:
#                 break
#
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

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 118. Pascal's Triangle / EASY

# задача: построить треугольник Паскаля.
# проще всего посмотреть гифку:
# https://leetcode.com/problems/pascals-triangle/description/?envType=problem-list-v2&envId=array
# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]] при n=5. Слева, справа всегда 1. То что между ними суммируется


# 1)
# from typing import List
#
#
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         if numRows == 0:
#             return []
#         if numRows == 1:
#             return [[1]]
#
#         prev_rows = self.generate(numRows - 1)
#         prev_row = prev_rows[-1]
#         current_row = [1]
#
#         for i in range(1, numRows - 1):
#             current_row.append(prev_row[i - 1] + prev_row[i])
#
#         current_row.append(1)
#         prev_rows.append(current_row)
#
#         return prev_rows
#
#
# s = Solution()
# print(s.generate(5))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 119. Pascal's Triangle II / EASY

# задача: идея такая же, что и выше. Только теперь чуть по другому начинается
# Example 2:
#
# Input: rowIndex = 0
# Output: [1]
# Example 3:
#
# Input: rowIndex = 1
# Output: [1,1]

# 1)
# from typing import List
#
#
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         if rowIndex == 0:
#             return [1]
#         if rowIndex == 1:
#             return [1, 1]
#
#         row = self.getRow(rowIndex - 1)
#         prev_row = row
#         new_row = [1]
#
#         for i in range(1, rowIndex):
#             new_row.append(prev_row[i - 1] + prev_row[i])
#
#         new_row.append(1)
#         row = new_row
#
#         return row
#
#
# s = Solution()
# print(s.getRow(2))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 121. Best Time to Buy and Sell Stock / EASY

# задача: состоит в том, чтобы найти максимальную прибыль, которую можно получить, покупая и продавая акции.
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# 1)
# говно подход, работает, но если засунуть 1лям значений - умэр
# from typing import List
#
#
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         for i in range(len(prices)):
#             for j in range(i + 1, len(prices)):
#                 print(prices[i], prices[j])
#                 if prices[j] > prices[i]:
#                     current_profit = abs(prices[i] - prices[j])
#                     if current_profit > profit:
#                         profit = current_profit
#
#         return profit
#
#
# s = Solution()
# print(s.maxProfit([7, 1, 5, 3, 6, 4]))
# print(s.maxProfit([7, 6, 4, 3, 1]))


# 2)
# Алгоритм Кадане для решения этой задачи (есть в гугл доке)
# class Solution:
#     def maxProfit(self, prices):
#         buy = prices[0]
#         profit = 0
#         for i in range(1, len(prices)):
#             if prices[i] < buy:
#                 buy = prices[i]
#             elif prices[i] - buy > profit:
#                 profit = prices[i] - buy
#         return profit
#
#
# s = Solution()
# print(s.maxProfit([7, 1, 5, 3, 6, 4]))

# 3)
# Просто алгоритм Кадане (базовый) - найти максимальный подмассив
# def kadane(lst):
#     current_sum = lst[0]
#     max_sum = lst[0]
#
#     for i in range(1, len(lst)):
#         current_sum = max(lst[i], current_sum + lst[i])
#         max_sum = max(max_sum, current_sum)
#
#     return max_sum
#
#
# print(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(kadane([7, 1, 5, 3, 6, 4, 27, 2]))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 136. Single Number / EASY

# задача: дан список. Нужно найти в нем значение, которое повторяется 1 раз.

# # 1)
# from typing import List
# from collections import Counter
#
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         cnt = Counter(nums)
#         return next(k for k, v in cnt.items() if v == 1)
#
#
# s = Solution()
# print(s.singleNumber(nums=[2, 2, 1, 1, 4]))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
#

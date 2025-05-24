from typing import List


# # 1. 128. Longest Consecutive Sequence (hash table)
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

# # 2. 1. Two Sum (hash table)
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
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # тут идея в том, что мы делаем проверку что и в предыдущем варе только сразу
#         # на моменте создания хэш таблицы.
#         # пример: nums [2, 7, 11, 15]
#         # при первом проходе: i=0, complement = 7, такого нет в хэш таблице, значит
#         # заносится {2(значение): 0(индекс)}.
#         # второй: i=1, complement = 2 - в хэш таблице есть - выводим
#         # И главное еще тут не нужна проверка на одинаковость индексов. Они точно не могут
#         # быть равны тк i постоянно растет и в кэш таблицу заносятся всегда разные i.
#         hashtable = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashtable:
#                 return [i, hashtable[complement]]
#             hashtable[nums[i]] = i
#         return []
#
#
# s = Solution()
# print(s.twoSum(nums=[2, 7, 11, 15], target=9)) # [0, 1]
# print(s.twoSum(nums=[3, 2, 4], target=6)) # [1, 2]
# print(s.twoSum(nums=[3, 3], target=6)) # [0, 1]

########################################################################################################################

# # 3 3. Longest Substring Without Repeating Characters (sliding window)

# Задача:подается строка,
# нужно найти в ней самую длинную последовательность неповторяющихся символов идущих по порядку.

# Time: O(n^2) | Space: O(n). Есть лучше, за O(n) - алгоритм Мангера или как то так
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # задаем указатели left и right - это наше sliding window
#         # создаем пустой сет в который будем заносить символы
#         # задаем счеткик max_length
#         # далее итерируемся по нашей строке (по индексам)
#         # если текущего символа нет в сете - двигаем указатель right и вычисляем max_length
#         # max_length вычисляется путем сравнивания max_length и right - left + 1. +1 тк индексация идет с 0
#         # если текущий символ есть в сете - циклом двигаем left и удаляем из сета значение s[left]
#         # таким образом в сете остается всегда комбинация уникальных символов, идущих друг за другом
#         left = 0
#         max_length = 0
#         char_set = set()
#
#         for right in range(len(s)):
#             while s[right] in char_set:
#                 char_set.remove(s[left])
#                 left += 1
#             char_set.add(s[right])
#             max_length = max(max_length, right - left + 1)
#
#         return max_length
#
#
# s = Solution()
# print(s.lengthOfLongestSubstring(s="abcabcbb")) # 3
# print(s.lengthOfLongestSubstring(s="bbbbb")) # 1
# print(s.lengthOfLongestSubstring(s="pwwkew")) # 3

########################################################################################################################

# # 4 5. Longest Palindromic Substring (two pointers)

# Time: O(n^2) | Space: O(1).
# Задача: подается строка, нужно найти в ней палиндром максимальной длины.

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if not s:
#             return ''
#
#         start, end = 0, 0  # границы текущего максимального палиндрома
#
#         def expand(left: int, right: int) -> (int, int):
#             # расширяемся пока символы равны и не вышли за границы
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#             # после цикла left и right указывают за пределы палиндрома
#             # реальный палиндром — от left+1 до right-1
#             return left + 1, right - 1
#
#         for i in range(len(s)):
#             # вычисления делаются для нечет и чет тк если оставить только первый - будет проскакивать и не
#             # вычислять нужный ответ
#             # палиндром нечётной длины (центр на i)
#             l1, r1 = expand(i, i)
#             # палиндром чётной длины (центр между i и i+1)
#             l2, r2 = expand(i, i + 1)
#
#             # выбираем больший из найденных
#             if r1 - l1 > end - start:
#                 start, end = l1, r1
#             if r2 - l2 > end - start:
#                 start, end = l2, r2
#
#         # возвращаем срез строки от start до end включительно
#         return s[start:end + 1]
#
#
# s = Solution()
# print(s.longestPalindrome("babad"))  # "bab" или "aba"
# print(s.longestPalindrome("cbbd"))  # "bb"
# print(s.longestPalindrome("a"))  # "a"
# print(s.longestPalindrome("ac"))  # "a" или "c"


########################################################################################################################

# # 4 647. Palindromic Substrings (two pointers)

# Time: O(n^2) | Space: O(n).
# Задача: найти кол-во палиндромов в строке

# Example 2:
#
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         def expand(left, right):
#             counter = 0
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 left -= 1
#                 right += 1
#                 counter += 1
#             return counter
#
#         total_count = 0
#         for i in range(len(s)):
#             total_count += expand(i, i)
#             total_count += expand(i, i + 1)
#
#         return total_count
#
#
# s = Solution()
# print(s.countSubstrings(s="aaa")) # 6 "a", "a", "a", "aa", "aa", "aaa"
# print(s.countSubstrings(s="abc")) # 3 a b c

########################################################################################################################

# # 268. Missing Number (formula)

# Задача: нужно найти число, которое пропущено в последовательности

# Example 1:
# Input: nums = [3,0,1]
# Output: 2 тк [0, 1, 2, 3] - два было пропущено
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
# 2 is the missing number in the range since it does not appear in nums.

# 1)
# Using Indexes Time: O(n) | Space: O(1). Используя формулу суммы ряда

# КАК ВЫЧИСЛИТЬ СУММУ РЯДА
# n = [0, 1, 2, 3, 4, 5, 6] # 0 + 1 + 2 + 3 + 4 + 5 + 6 = 21 - сумма ряда
# print(sum(n))

# ФОРМУЛА
# n = 6 # кол-во натуральных чисел в ряде (натуральные числа - это числа больше 0 идущие по порядку)
# sum_seq = (n * (n + 1)) / 2 # сумма ряда
# print(sum_seq)

# class Solution:
#     def missingNumber(self, nums: List[int]):
#         n = len(nums)
#         sum_seq = n * (n + 1) / 2
#         sum_nums = sum(nums)
#         return sum_seq - sum_nums
#
# s = Solution()
# print(s.missingNumber(nums=[3, 0, 1])) # 2
# print(s.missingNumber(nums=[0, 1, 2, 3])) # 4
# print(s.missingNumber(nums=[0, 1, 2, 3, 5])) # 4

# 2)
# Using Vectors Time: O(n) | Space: O(n).
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         # создаем список той длины, который должен быть включая пропущенный элемент
#         v = [-1] * (len(nums) + 1)
#         print(v)
#
#         # заполняем его с помощью того что задан
#         for num in nums:
#             v[num] = num
#         print(v)
#         # вычисляем оставшуюся единицу
#         for i in range(len(v)):
#             if v[i] == -1:
#                 return i
# #
# s = Solution()
# print(s.missingNumber(nums=[3, 0, 1])) # 2
# print(s.missingNumber(nums=[0, 5, 1, 2, 3])) # 4

########################################################################################################################

# # 11. Container With Most Water (two pointers)

# Задача: Представляем контейнер с водой в котором есть перегородки. Каждая перегородка разной высоты
#         Нужно найти максимальную площадь, которая может быть заполнена водой.
#   1 +
#   2 +
#   3 +         +   --> 6 * 3 = 18
#   4 +     +   +
#   5 +     +   +
#   6 + + + + + +
#     1 2 3 4 5 6

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

# class Solution:
#     def maxArea(self, num_lust: List[int]) -> int:
#         left = 0
#         right = len(num_lust) - 1
#         max_area = 0
#         while left < right:
#             # ширину узнаем через разницу индексов
#             width = right - left
#             # берем минимальную высотку из двух столбцов (чтобы вода не проливалась через край)
#             height = min(num_lust[left], num_lust[right])
#             # вычисляем площадь
#             current_length = width * height
#
#             if max_area < current_length:
#                 max_area = current_length
#
#             # участок кода выше можно записать одной строкой:
#             # max_area = max(max_area, (right - left) * min(height[left], height[right]))
#
#             if num_lust[left] < num_lust[right]:
#                 left += 1
#             else:
#                 right -= 1
#
#         return max_area
#
#
# s = Solution()
# print(s.maxArea(num_lust=[1, 8, 6, 2, 5, 4, 8, 3, 7])) # 49
# print(s.maxArea(num_lust=[1, 1])) # 1

########################################################################################################################

# 15. 3Sum (two pointers)

# Задача:

# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# 1) Time O(n^2) Space O(1)
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         result_lst = []
#
#         for a in range(len(nums)):
#             if a > 0 and nums[a] == nums[a - 1]:
#                 continue
#
#             left = a + 1
#             right = len(nums) - 1
#
#             while left < right:
#                 threeSum = nums[a] + nums[left] + nums[right]
#                 if threeSum > 0:
#                     right -= 1
#                 elif threeSum < 0:
#                     left += 1
#                 else:
#                     result_lst.append([nums[a], nums[left], nums[right]])
#                     left += 1
#                     while nums[left] == nums[left - 1] and left < right:
#                         left += 1
#
#         return result_lst
#
#
# s = Solution()
# print(s.threeSum(nums=[-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
# print(s.threeSum(nums=[0, 1, 1]))  # []
# print(s.threeSum(nums=[0, 0, 0]))  # [[0, 0, 0]]

########################################################################################################################

# 125. Valid Palindrome (two pointers)
#
# tags: two pointers
#
# Задача: подается строк типа "A man, a plan, a canal: Panama". Может содержать что угодно.
# Нужно понять является ли она палиндромом, если убрать все кроме букв и цифр.

# 1) two pointers - Time: O(n^2) Space O(n)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # очень затратная идея копировать так строку тк мы ее пересоздаем постоянно
#         # и именно из-за этого сложность O(n^2)
#         new_s = ''
#         for i in s.lower():
#             if i.isalpha():
#                 new_s += i
#         print(new_s)
#
#         left = 0
#         right = len(new_s) - 1
#         while left < right:
#             if new_s[left] != new_s[right]:
#                 return False
#             left += 1
#             right -= 1
#
#         return True
#
# s = Solution()
# print(s.isPalindrome(s="A man, a plan, a canal: Panama")) # true
# print(s.isPalindrome(s="race a car")) # false
# print(s.isPalindrome(s=" ")) # true

# 2) by reverse Time: O(n^2) Space O(n)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         new_s = ''
#         for i in s.lower():
#             if i.isalnum():
#                 new_s += i.lower()
#
#         return new_s == new_s[::-1]
#
#
# s = Solution()
# print(s.isPalindrome(s="A man, a plan, a canal: Panama")) # true
# print(s.isPalindrome(s="race a car")) # false
# print(s.isPalindrome(s=" ")) # true

# 3) Time O(n) Space O(1)
# class Solution:
#     # используется свой isalnum
#     def isalnum(self, c):
#         return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')
#
#     def isPalindrome(self, s: str) -> bool:
#         left = 0
#         right = len(s) - 1
#         while left < right:
#             # проверка тут на left < right позволяет пройти вот такой кейс "a-----"
#             while left < right and not self.isalnum(s[left]):
#                 left += 1
#             while left < right and not self.isalnum(s[right]):
#                 right -= 1
#             if s[left].lower() != s[right].lower():
#                 return False
#             left += 1
#             right -= 1
#
#         return True
#
#
# s = Solution()
# print(s.isPalindrome(s="A man, a plan, a canal: Panama"))  # true
# print(s.isPalindrome(s="race a car"))  # false
# print(s.isPalindrome(s=" "))  # true

########################################################################################################################

# 121. Best Time to Buy and Sell Stock (sliding window)

# Задача: подается список чисел (значения валют). Нужно найти лучший момент для продажи валюты.
#                   0  1  2  3  4  5
# К примеру prices=[7, 1, 5, 3, 6, 4] - лучший момент купить в 1 и продать в 4 т.е. профит = 6 - 1 = 5

# 1) через цикл while Time: O(n) Space O(1)
# class Solution:
#     # создаем два указателя. Двигаем правый до тех пока не пройдем все значения в списке
#     # а левым просто чекаем является ли он минимальным каждый раз.
#     # Если да - вычисляем профит, обновляем счетчик. Если нет - обновляем новый минимум.
#     # получается система в виде окошка - sliding window
#     def maxProfit(self, prices: List[int]) -> int:
#         left, right = 0, 1
#         max_profit = 0
#
#         while right < len(prices):
#             if prices[left] < prices[right]:
#                 profit = prices[right] - prices[left]
#                 max_profit = max(max_profit, profit)
#             else:
#                 left = right
#             right += 1
#
#         return max_profit
#
#
#
# s = Solution()
# print(s.maxProfit(prices=[7, 1, 5, 3, 6, 4]))  # 5
# print(s.maxProfit(prices=[7, 1, 5, 3, 6, 0, 8]))  # 8
# print(s.maxProfit(prices=[7, 6, 4, 3, 1]))  # 0

# 1) через цикл for Time: O(n) Space O(1)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = float('inf') # + бесконечность
#         max_profit = 0
#
#         for price in prices:
#             # если текущая цена меньше, чем ранее встретившаяся минимальная,
#             # обновляем минимальную цену
#             if price < min_price:
#                 min_price = price
#             else:
#                 # иначе вычисляем профит
#                 profit = price - min_price
#                 # и обновляем максимальную
#                 if profit > max_profit:
#                     max_profit = profit
#
#         return max_profit
#
#
# s = Solution()
# print(s.maxProfit(prices=[7, 1, 5, 3, 6, 4]))  # 5
# print(s.maxProfit(prices=[7, 6, 4, 3, 1]))  # 0
# print(s.maxProfit(prices=[1, 0, 1]))  # 1
# print(s.maxProfit(prices=[7, 1, 5, 3, 6, 0, 8]))  # 5

########################################################################################################################

# 217. Contains Duplicate (hash map)

# Задача: подается список интов. Если в списке есть повторяющиеся значения - вернуть false,
# если все уникальны - false

# еще можно решить через сортировку и брут форс, увеличивая Time, но уменьшая Space
# 1) hash_map Time: O(n) Space: O(n)
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
# s = Solution()
# print(s.containsDuplicate(nums=[1, 2, 3, 1])) # true
# print(s.containsDuplicate(nums=[1, 2, 3, 4])) # false
# print(s.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2])) # true

########################################################################################################################

# 238. Product of Array Except Self (formula: multiply

# Задача: подается список интов. Нужно вернуть список состоящий из произведений всех элементов, кроме текущего i.
# сделать нужно без использования деления.
# к примеру массив [1, 2, 3, 4].
# Для i=0 --> 2 * 3 * 4 = 24
# Для i=1 --> 1 * 3 * 4 = 12
# Для i=2 --> 1 * 2 * 4 = 8
# Для i=3 --> 1 * 2 * 3 = 8

# 1) с делением Time: O(n) Space: O(n)
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         total_product = 1
#         zero_count = 0
#
#         # считаем произведение всех НЕ нулевых чисел и количество нулей
#         for num in nums:
#             if num == 0:
#                 zero_count += 1
#             else:
#                 total_product *= num
#
#         print(zero_count)
#         print(total_product)
#         result = []
#
#         for num in nums:
#             # если нулей 2 и более - значит все произведения будут 0
#             if zero_count > 1:
#                 result.append(0)
#             # если один нуль, то два варика:
#             # либо произведение 0, либо текущий num=0 и нужно посчитать произведение оставшихся
#             elif zero_count == 1:
#                 if num == 0:
#                     result.append(total_product)
#                 else:
#                     result.append(0)
#             # если нет нулей, то произведение оставшихся вычисляется через целочисленное деление
#             else:
#                 result.append(total_product // num)
#
#         return result
#
#
# s = Solution()
# print(s.productExceptSelf(nums=[1, 2, 3, 4]))  # [24,12,8,6]
# print(s.productExceptSelf(nums=[-1, 1, 0, -3, 3]))  # [0,0,9,0,0]

# 2) через префиксы и суффиксы Time: O(n) Space: O(n)
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#
#         # составляем начальный массив префиксов [1, 1, 1, 1]
#         # идем по нему и вычисляем prefix[i]
#         # prefix[i] = предыдущий элемент в списке prefix на предыдущий элемент в списке nums
#         # начинаем идти с 1, а не с нуля.
#         prefix = [1] * n
#         for i in range(1, n):
#             prefix[i] = prefix[i - 1] * nums[i - 1]
#
#         print(prefix) # [1, 1, 2, 6]
#
#         # делаем то же самое в обратном порядке
#         # range(n - 2, -1, -1) --> start: n-2 - первый индекс (второй справа тк будем брать предыдущего справа i + 1)
#         #                      -->  stop: -1 - идет пока i > stop
#         #                      -->  step: -1 - каждый раз отнимаем -1
#         suffix = [1] * n
#         for i in range(n - 2, -1, -1):
#             suffix[i] = suffix[i + 1] * nums[i + 1]
#
#         print(suffix) # [24, 12, 4, 1]
#
#         # конечный список составляем путем перемножения элементов массива prefix и suffix
#         result = [1] * n
#         for i in range(n):
#             result[i] = prefix[i] * suffix[i]
#
#         return result
#
#
# s = Solution()
# print(s.productExceptSelf(nums=[1, 2, 3, 4]))  # [24,12,8,6]
# print(s.productExceptSelf(nums=[-1, 1, 0, -3, 3]))  # [0,0,9,0,0]

# 3) через префиксы и суффиксы + оптимизация по памяти Time: O(n) Space: O(1)
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#
#         result = [1] * n
#
#         # также составляем массив префиксов, но только заносим сразу в result
#         for i in range(1, n):
#             result[i] = result[i - 1] * nums[i - 1]
#
#         print(result) # [1, 1, 2, 6]
#
#         # не составляем массив суффиксов, а сразу идем по result в обратном направлении
#         suf = 1
#         # идем в обратном порядке по [1, 2, 3, 4]
#         for i in range(n - 1, -1, -1):
#             result[i] *= suf
#             suf *= nums[i]
#
#         return result
#
#
# s = Solution()
# print(s.productExceptSelf(nums=[1, 2, 3, 4]))  # [24,12,8,6]
# print(s.productExceptSelf(nums=[-1, 1, 0, -3, 3]))  # [0,0,9,0,0]


########################################################################################################################

# 53. Maximum Subarray

# Задача: подается массив интов, нужно найти внутри подмассив с максимальной суммой элементов.

# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# 1) Брут форс Time: O(n^2) Space: O(1)
# class Solution:
#     # Медленный способ: для каждого элемента проходим цикл по всем элементам массива.
#     # Так ты составляешь как бы все возможные массивы. По пути считаешь новый добавленный элемент current_sum
#     # И сравниваешь его с max_sum. Пройдя по всем выводишь max_sum
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         max_sum = float('-inf')  # очень маленькое значение для старта
#
#         for start in range(n):
#             current_sum = 0
#             for end in range(start, n):
#                 current_sum += nums[end]
#                 max_sum = max(max_sum, current_sum)
#
#         return max_sum
#
# s = Solution()
# print(s.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6 # The subarray [4,-1,2,1] has the largest sum 6.
# print(s.maxSubArray(nums=[1]))  # 1
# print(s.maxSubArray(nums=[5, 4, -1, 7, 8]))  # 23

# 2) Брут форс Time: O(n^2) Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:




s = Solution()
print(s.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6 # The subarray [4,-1,2,1] has the largest sum 6.
print(s.maxSubArray(nums=[1]))  # 1
print(s.maxSubArray(nums=[5, 4, -1, 7, 8]))  # 23
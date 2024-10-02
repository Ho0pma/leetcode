from cgitb import reset
from encodings import search_function
from math import sqrt, ceil, floor
from typing import List, Optional


# 1. Two Sum / Easy

# задача: задается список и target. Нужно найти пары чисел, которые в сумме = target и вывести их индексы.
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         d = {}
#
#         for index, value in enumerate(nums):
#             diff = target - value
#             if diff in d and d[diff] != index:
#                 return [d[diff], index]
#
#             d[value] = index
#
#
# s = Solution()
# print(s.twoSum(nums=[2, 7, 11, 15], target=9))
# print(s.twoSum(nums=[3, 2, 4], target=6))
# print(s.twoSum(nums=[3, 3], target=6))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 9. Palindrome Number / Easy

# задача: нужно вычислить является ли число палиндромом
# 1) через конверт в строку
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         string = str(x)
#         return string == string[::-1]
#
#
# s = Solution()
# print(s.isPalindrome(x=121))
# print(s.isPalindrome(x=-121))
# print(s.isPalindrome(x=10))
# print(s.isPalindrome(x=1221))

# 2) чуть лучше по скорости, хуже по памяти
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#
#         reversed_num = 0
#         temp = x
#
#         while temp != 0:
#             digit = temp % 10
#             reversed_num = reversed_num * 10 + digit
#             temp //= 10
#
#         return reversed_num == x
#
# s = Solution()
# print(s.isPalindrome(x=121))
# print(s.isPalindrome(x=-121))
# print(s.isPalindrome(x=10))
# print(s.isPalindrome(x=1221))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 13. Roman to Integer / EASY

# задача: перевести число из римских в обычные.
# 1)
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         d1 = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000,
#         }
#         s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
#         s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
#         s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')
#
#         roman = 0
#         for i in s:
#             roman += d1[i]
#
#         return roman
#
#
# s = Solution()
# print(s.romanToInt(s="III"))
# print(s.romanToInt(s="LVIII"))
# print(s.romanToInt(s="MCMXCIV"))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 14. Longest Common Prefix / EASY

# задача: найти максимальный префикс у слов
# 1)
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         prefix = ''
#         # print(list(zip(*strs)))
#         for elements in zip(*strs):
#             if all(x == elements[0] for x in elements):
#                 prefix += elements[0]
#             else:
#                 break
#
#         return prefix
#
#
# s = Solution()
# print(s.longestCommonPrefix(strs=["flower", "flow", "flight"])) # fl
# print(s.longestCommonPrefix(strs=["dog", "racecar", "car"])) # ''

# 2) сильно лучше
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         # сортируем в лексикографическом порядке тк если все слова имеют один префикс
#         # можно будет взять первое и последнее слово. Если слова в разнобой - так не получится.
#         strs = sorted(strs)
#         result = ""
#         first = strs[0]
#         last = strs[-1]
#         # берем минимальный range из двух слов. Цикл должен выполняться только до конца
#         # самой короткой строки, тк общий префикс не может быть длиннее самой короткой строки.
#         for i in range(min(len(first), len(last))):
#             if first[i] != last[i]:
#                 return result
#             result += first[i]
#         return result
#
#
# s = Solution()
# print(s.longestCommonPrefix(strs=["flower", "flow", "flight"]))  # fl
# print(s.longestCommonPrefix(strs=["dog", "racecar", "car"]))  # ''

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 20. Valid Parentheses / EASY

# задача: проверить правильность написания скобок в строке
# 1)
# class Solution:
#     def isValid(self, s: str) -> bool:
#         d = {
#             ')': '(',
#             ']': '[',
#             '}': '{',
#         }
#         stack = []
#         for i in s:
#             if i in d: # или in ')}]'
#                 if stack and d[i] != stack.pop():
#                     return False
#             else:
#                 stack.append(i)
#
#         if stack:
#             return False
#         else:
#             return True
#
#
# s = Solution()
# print(s.isValid(s="()"))
# print(s.isValid(s="()[]{}"))
# print(s.isValid(s="(]"))
# print(s.isValid(s="[()]"))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 21. Merge Two Sorted Lists / EASY

# задача: подаются два объекта типа ListNode, которые образуют связные списки
# скажем list1 = [1, 2, 4], list2 = [1, 3, 4], нужно вернуть в list1 смержить эти два массива и отсортировать

# 1)
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         # создаем голову результирующего списка
#         head = ListNode()
#         # указатель на текущий элемент рез списка. В целом можно тащить и head, но логичнее
#         # создать "текущий" указатель
#         node = head
#
#         # проходим по спискам. В моменте у нас есть только ссылка на текущий элемент
#         while list1 and list2:
#             if list1.val < list2.val:
#                 node.next = list1 # добавляем узел list1 в результирующий
#                 list1 = list1.next # переходим к следующему в list1
#             else:
#                 node.next = list2
#                 list2 = list2.next
#
#             node = node.next # обновляем указатель в рез списке
#
#         # проверяем остатки списков
#         if list1:
#             node.next = list1
#         elif list2:
#             node.next = list2
#
#         # next тк мы создали голову с дефолтным значением 0 (которого нет в списке)
#         return head.next
#
#
# # создаем связные списки
# list1 = ListNode(1, ListNode(2, ListNode(4)))
# list2 = ListNode(1, ListNode(3, ListNode(4)))
#
# s = Solution()
# head_of_list = s.mergeTwoLists(list1, list2)
# node = head_of_list
#
# while node.next:
#     print(node.val, end=' ')
#     node = node.next

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 26. Remove Duplicates from Sorted Array / EASY

# задача: на вход поступает массив, в нем числа, сортированные по возрастанию, повторяются. Нужно сделать так, чтобы
# в том же массиве остались только уникальные числа и размер массива остался изначальным (дубликаты поменять на любой
# символ) Те из [1, 1, 2] --> [1, 2, _]. На выходе вывести кол-во уникальных элементов.
# 1)
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         uniq_nums = sorted(set(nums))
#         empty_space = len(nums) - len(uniq_nums)
#         nums[:] = uniq_nums + empty_space * ['_']
#         # print(nums) # для просмотра
#         return len(uniq_nums)
#
#
# s = Solution()
# s.removeDuplicates(nums=[1, 1, 2]) # Output: 2, nums = [1,2,_]
# s.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

# 2) лучше
# через два указателя. Указатель i проходит список с 1го элемента и сравниваем с предыдущим
# если значения равны - идет дальше. Если не равны - перезаписывает значение в массиве по указателю j
# по заданию сказано, что не важно что остается в конце массива.
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         j = 1
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 nums[j] = nums[i]
#                 j += 1
#         return j
#
# s = Solution()
# s.removeDuplicates(nums=[1, 1, 2]) # Output: 2, nums = [1,2,_]
# s.removeDuplicates(nums=[0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 27. Remove Element / EASY

# задача: задача убрать val из nums IN PLACE и вернуть кол-во элементов != val

# 1)
# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         counter = 0
#         for i in nums:
#             if i != val:
#                 nums[counter] = i
#                 counter += 1
#
#         return counter
#
#
# s = Solution()
# print(s.removeElement(nums=[3, 2, 2, 3], val=3))  # Output: 2, nums = [2,2,_,_]
# print(s.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))  # Output: 5, nums = [0,1,4,0,3,_,_,_]

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 28. Find the Index of the First Occurrence in a String / EASY

# задача: найти первое вхождение в строку, если его нет - вернуть -1

# 1) в лоб
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.find(needle)
#
#
# s = Solution()
# print(s.strStr(haystack="sadbutsad", needle="sad"))  # Output: 0
# print(s.strStr(haystack="leetcode", needle="leeto"))  # Output: -1

# 2) это решение лучше только тем, что есть контроль над процессом поиска
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if len(haystack) < len(needle):
#             return -1
#
#         for i in range(len(haystack)):
#             if haystack[i:i + len(needle)] == needle:
#                 return i
#
#         return -1
#
#
# s = Solution()
# print(s.strStr(haystack="butsad", needle="sad"))  # Output: 0
# print(s.strStr(haystack="leetcode", needle="leeto"))  # Output: -1

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 35. Search Insert Position / EASY

# задача: задача либо найти в списке заданный target, либо найти место где его нужно вставить
# по порядку. Список подается отсортированный

# 1) O(n)
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#
#         for i in nums:
#             if i > target:
#                 return nums.index(i)
#
#         return len(nums)
#
#
# s = Solution()
# print(s.searchInsert(nums=[1, 3, 5, 6], target=5))  # Output: 2
# print(s.searchInsert(nums=[1, 3, 5, 6], target=2))  # Output: 1
# print(s.searchInsert(nums=[1, 3, 5, 6], target=7))  # Output: 4

# 2) O(log n) бинарный поиск
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#
#         left = 0
#         right = len(nums) - 1
#
#         while left <= right:
#             mid = (left + right) // 2
#
#             if nums[mid] == target:
#                 return mid
#             # если значение по индексу в массиве больше таргета - отметаем все что справа
#             elif nums[mid] > target:
#                 right = mid - 1
#             # иначе отметаем все что слева
#             else:
#                 left = mid + 1
#
#         return left
#
#
# s = Solution()
# print(s.searchInsert(nums=[1, 3, 5, 6], target=5))  # Output: 2
# print(s.searchInsert(nums=[1, 3, 5, 6], target=2))  # Output: 1
# print(s.searchInsert(nums=[1, 3, 5, 6], target=7))  # Output: 4

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# binary search

# def binary_search(lst, target):
#     left = 0
#     right = len(lst) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if lst[mid] == target:
#             return mid
#         if lst[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1
#
#     return 'Not found'
#
#
# print(binary_search([1, 3, 5, 6], 1))

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 58. Length of Last Word

# задача: узнать длину последнего слова в поступаемой строке

# 1) короткое решение, но если будет большая строка - беда
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.split()[-1])
#
#
# s = Solution()
# print(s.lengthOfLastWord(s="Hello World")) # Output: 5
# print(s.lengthOfLastWord(s="   fly me   to   the moon  "))  # Output: 4
# print(s.lengthOfLastWord(s="luffy is still joyboy")) # Output: 6

# 2) Минус - пересоздается строка. Ищем с конца строки до первого пробела, работает быстрее
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s.strip() # убираем пробелы вначале и в конце
#         counter = 0
#         # проходим строку с конца и на скокойничах считаем буковки, проверяя что i != пробел
#         for i in s[::-1]:
#             if i != ' ':
#                 counter += 1
#             else: break
#
#         return counter
#
#
# s = Solution()
# print(s.lengthOfLastWord(s="Hello World")) # Output: 5
# print(s.lengthOfLastWord(s="   fly me   to   the moon  "))  # Output: 4
# print(s.lengthOfLastWord(s="luffy is still joyboy")) # Output: 6

# 3) через два указателя. Скорость такая же, но память лучше, чем во втором варе, тк in place
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         if s.isspace():
#             return -1 # 'No words in string'
#
#         end = len(s) - 1
#
#         # сначала ищем указатель на конец последнего слова в строке
#         # те это проверка на пробелы в конце
#         while s[end] == ' ':
#             end -= 1
#
#         # теперь проверяем для нового указателя так же проверяем на буквы
#         # если буквы - уменьшаем указатель
#         counter = end
#         while counter >= 0 and s[counter] != ' ':
#             counter -= 1
#
#         # разница между указателями как раз и будет последнее слово
#         return end - counter
#
#
# s = Solution()
# print(s.lengthOfLastWord(s=" ")) # Output: 5
# print(s.lengthOfLastWord(s="  hi   Hello World  ")) # Output: 5
# print(s.lengthOfLastWord(s="Hello World")) # Output: 5
# print(s.lengthOfLastWord(s="   fly me   to   the moon  "))  # Output: 4
# print(s.lengthOfLastWord(s="luffy is still joyboy")) # Output: 6

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 66. Plus One

# задача: подается массив [1,2,4] нужно прибавить единицу к числу 124, чтобы получился массив [1, 2, 5]

# 1) плохой вар, в лоб
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         digit = ''
#         for i in digits:
#             digit += str(i)
#
#         result = int(digit) + 1
#
#         return [int(i) for i in str(result)]
#
#
# s = Solution()
# print(s.plusOne(digits=[1, 2, 3])) # Output: [1,2,4]
# print(s.plusOne(digits=[4, 3, 2, 1])) # Output: [4,3,2,2]
# print(s.plusOne(digits=[9])) # Output: [1,0]

# 2)
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#
#         # первый вар цикла
#         for i in range(len(digits) - 1, -1, -1):
#
#             if digits[i] + 1 != 10:
#                 digits[i] += 1
#                 return digits
#
#             digits[i] = 0
#
#             if i == 0:
#                 return [1] + digits
#
#         # # второй вар цикла (просто чуть по другому реализовано)
#         # for i in range(len(digits) - 1, -1, -1):
#         #     if digits[i] == 9:
#         #         digits[i] = 0
#         #     else:
#         #         digits[i] = digits[i] + 1
#         #         return digits
#         #
#         #     if i == 0:
#         #         return [1] + digits
#         #
#         # return digits
#
#
# s = Solution()
# print(s.plusOne(digits=[9, 9])) # Output: [1, 0, 0]
# print(s.plusOne(digits=[9, 0, 9, 0])) # Output: [9, 0, 9, 1]
# print(s.plusOne(digits=[1, 2, 3])) # Output: [1,2,4]
# print(s.plusOne(digits=[4, 3, 2, 1])) # Output: [4,3,2,2]
# print(s.plusOne(digits=[9])) # Output: [1,0]

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# 69. Sqrt(x)

# задача:

# 1)
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         return floor(sqrt(x))
#
#
# s = Solution()
# s.mySqrt(x=4)  # Output: 2
# s.mySqrt(x=2)  # Output: 2

# 2)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left, right = 1, x

        while left <= right:
            mid = left + (right - left) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                right = mid - 1
            else:
                left = mid + 1

        return right


s = Solution()
print(s.mySqrt(x=4))  # Output: 2
print(s.mySqrt(x=8))  # Output: 2

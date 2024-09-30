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
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

s = Solution()
s.removeDuplicates(nums=[1, 1, 2]) # Output: 2, nums = [1,2,_]
s.removeDuplicates(nums=[0, 0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
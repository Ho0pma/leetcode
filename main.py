# # 13. Roman to Integer
# # Перевод римских чисел в арабские.
# этот вар хороший по памяти, но плохой по скорости
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         result = 0
#         prev_value = 0
#
#         d = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
#
#         for i in s:
#             value = d[i]
#
#             if value > prev_value:
#                 result += value - 2 * prev_value
#                 prev_value = value
#             else:
#                 result += d[i]
#                 prev_value = value
#
#         return result
#
# s = Solution()
# # print(s.romanToInt('III'))
# print(s.romanToInt('LVIII'))
# print(s.romanToInt('MCMXCIV'))


# ВТОРОЙ ВАРИК
# хуже по памяти, но лучше по скорости
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         translations = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         number = 0
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#         for char in s:
#             number += translations[char]
#         return number

# -------------------------------------------------------------------------------------------------------------------- #
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        markers = {'(': ')', '{': '}', '[': ']'}

        dq = deque()

        for i in s:
            if i in '([{':
                dq.append(i)
            else:
                try:
                    drop = dq.pop()
                except IndexError as e:
                    return False
                if i != markers[drop]:
                    return False

        return False if dq else True


s = Solution()
print(s.isValid('(()'))


























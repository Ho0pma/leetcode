from typing import List


# 167. Two Sum II - Input Array Is Sorted

# Задача: продолжение задачи two nums. Подается список чисел numbers и target. Нужно найти два числа, которые
# в сумме дают target. Отличие от основы, что тут подается отсортированный список и индексы идут не с 0, а с 1.

# 1) Time O(n) Space O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int):
        left = 0
        right = len(numbers) - 1

        for i in range(len(numbers)):
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return None


s = Solution()
print(s.twoSum(numbers=[1, 3, 4, 5, 7, 10, 11], target=9))  # [3, 4]
print(s.twoSum(numbers=[2, 7, 11, 15], target=9))  # [1, 2]
print(s.twoSum(numbers=[2, 3, 4], target=6))  # [1, 3]
print(s.twoSum(numbers=[-1, 0], target=-1))  # [1, 2]

####################################################################################################################



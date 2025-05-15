from typing import List


# 1. Two Sum

# Задача: подается список чисел nums и target. Нужно найти два числа, которые в сумме дают target.
# Вернуть индексы этих чисел. Нельзя вернуть один и тот же индекс.

# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# 1) two pass hash table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # создаем дикт
        # проходим циклом по nums, заносим в созданный дикт {значение: индекс}
        # вторым циклом проходим опять по nums выясняя есть ли "разница" в дикте
        # если есть - выводим
        nums_set = {}

        for i in range(len(nums)):
            nums_set[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_set and nums_set[diff] != i:
                return [i, nums_set[diff]]
        return []


s = Solution()
print(s.twoSum(nums=[2, 7, 11, 15], target=9)) # [0, 1] or [1, 0]
print(s.twoSum(nums=[3, 2, 4], target=6)) # [1, 2]
print(s.twoSum(nums=[3, 3], target=6)) # [0, 1]

# 2) one pass hash table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_set:
                return [i, nums_set[diff]]
            nums_set[nums[i]] = i

        return []


s = Solution()
print(s.twoSum(nums=[2, 7, 11, 15], target=9)) # [0, 1] or [1, 0]
print(s.twoSum(nums=[3, 2, 4], target=6)) # [1, 2]
print(s.twoSum(nums=[3, 3], target=6)) # [0, 1]

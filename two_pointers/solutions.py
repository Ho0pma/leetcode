from typing import List


# 167. Two Sum II - Input Array Is Sorted

# Задача: продолжение задачи two nums. Подается список чисел numbers и target. Нужно найти два числа, которые
# в сумме дают target. Отличие от основы, что тут подается отсортированный список и индексы идут не с 0, а с 1.

# 1) Time O(n) Space O(1)
# class Solution:
#     def twoSum(self, numbers: List[int], target: int):
#         left = 0
#         right = len(numbers) - 1
#
#         for i in range(len(numbers)):
#             if numbers[left] + numbers[right] > target:
#                 right -= 1
#             elif numbers[left] + numbers[right] < target:
#                 left += 1
#             else:
#                 return [left + 1, right + 1]
#         return None
#
#
# s = Solution()
# print(s.twoSum(numbers=[1, 3, 4, 5, 7, 10, 11], target=9))  # [3, 4]
# print(s.twoSum(numbers=[2, 7, 11, 15], target=9))  # [1, 2]
# print(s.twoSum(numbers=[2, 3, 4], target=6))  # [1, 3]
# print(s.twoSum(numbers=[-1, 0], target=-1))  # [1, 2]

####################################################################################################################

# 15. 3Sum

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
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result_lst = []

        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            left = a + 1
            right = len(nums) - 1

            while left < right:
                threeSum = nums[a] + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result_lst.append([nums[a], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result_lst


s = Solution()
print(s.threeSum(nums=[-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
print(s.threeSum(nums=[0, 1, 1]))  # []
print(s.threeSum(nums=[0, 0, 0]))  # [[0, 0, 0]]

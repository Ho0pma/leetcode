from typing import List


# 1. ☠️ 26. Remove Duplicates from Sorted Array

# task: remove duplicates from a sorted list. The list must remain the same, i.e. do it in-place.
#       the remaining elements can be ignored, or mark them with "_" as in the example
# example:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]

# example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

# 1) Complexity: Time: O(n), Memory O(1)
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         # discard the edge case
#         if len(nums) == 1:
#             return 1
#
#         # register two pointers (reader - i, writer - slow)
#         # go through the array
#         # if i == i - 1 --> skip
#         # if i != i - 1 --> write the value at index i to pointer slow
#         # this way we get in-place, the first elements are unique
#         # time complexity will = one pass through the array, i.e. O(n)
#         # memory = the introduced variables, i.e. i and slow, i.e. O(1)
#         slow = 1
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 continue
#             else:
#                 nums[slow] = nums[i]
#                 slow += 1
#
#         # second pass through the array for pretty output, can also not do it per the problem
#         for j in range(slow, len(nums)):
#             nums[j] = "_"
#
#         return slow, nums
#
#
# s = Solution()
# print(s.removeDuplicates([0, 1]))  # (2, [0, 1])
# print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # (5, [0, 1, 2, 3, 4, '_', '_', '_', '_', '_'])

# ----------------------------------------------------------------------------------------------------------------------#

# 2. ☠️ 27. Remove Element

# task: an array of unsorted elements (nums) and a number (val) are given
#       need to return the count of elements not equal to val
#       do it in-place

# example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

# example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]

# 1) Complexity: Time: O(n), Memory O(1)
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         # set two pointers: i (moving), slow (writing)
#         # if i matches val - write the value from i at slow
#         slow = 0
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 continue
#             else:
#                 nums[slow] = nums[i]
#                 slow += 1
#
#         # second pass through the array for the pretty output
#         for i in range(slow, len(nums)):
#             nums[i] = '_'
#
#         return slow, nums
#
# 2) same complexity, but reads a bit cleaner
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
# print(s.removeElement(nums=[3, 2, 2, 3], val=3))  # (2, [2, 2, '_', '_'])
# print(s.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))  # (5, [0, 1, 3, 0, 4, '_', '_', '_'])

# ----------------------------------------------------------------------------------------------------------------------#

# 3) 28. Find the Index of the First Occurrence in a String

# task: подается строка1 (haystack) и строка2 (needle).
#       нужно вернуть индекс первого сопоставления needle в haystack

# example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0

# example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1

#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


s = Solution()
print(s.strStr(haystack="leetcode", needle="leeto"))
print(s.strStr(haystack="2112", needle="11"))
#                        012345678910
print(s.strStr(haystack="mississippi", needle="issipi"))
print(s.strStr(haystack="a", needle="a"))

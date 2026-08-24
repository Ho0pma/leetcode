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
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # discard the edge case
        if len(nums) == 1:
            return 1

        # register two pointers (reader - i, writer - slow)
        # go through the array
        # if i == i - 1 --> skip
        # if i != i - 1 --> write the value at index i to pointer slow
        # this way we get in-place, the first elements are unique
        # time complexity will = one pass through the array, i.e. O(n)
        # memory = the introduced variables, i.e. i and slow, i.e. O(1)
        slow = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            else:
                nums[slow] = nums[i]
                slow += 1

        # second pass through the array for pretty output, can also not do it per the problem
        for j in range(slow, len(nums)):
            nums[j] = "_"

        return slow, nums


s = Solution()
print(s.removeDuplicates([0, 1]))  # (2, [0, 1])
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # (5, [0, 1, 2, 3, 4, '_', '_', '_', '_', '_'])

#----------------------------------------------------------------------------------------------------------------------#


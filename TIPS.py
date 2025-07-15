#############################################################################################################
# разница между defaultdict и обычным dict при добавлении элемента, который не существует.
# результат один и тот же

# nums = [4, 1, -1, 2, -1, 2, 3]
# nums_counter_1, nums_counter_2 = {}, {}
# for num in nums:
#     nums_counter_1[num] = 1 + nums_counter_1.get(num, 0)
# print(nums_counter_1)
#
# nums_counter_2 = defaultdict(int)
# for num in nums:
#     nums_counter_2[num] += 1
# print(nums_counter_2)

#############################################################################################################

# import itertools
# target = 12
# integer_array = [2, 8, 4, 7, 9, 5, 1]
# for numbers in itertools.combinations(integer_array, 3):
#     if sum(numbers) == target:
#         print([integer_array[number] for number in numbers])

target = 12
nums = [2, 8, 4, 7, 9, 5, 1]
def indices_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(i+2, len(nums)):
                if nums[i]+nums[j]+nums[k] == target:
                    return [nums[i], nums[j], nums[k]]
                
print (indices_sum(nums, target))

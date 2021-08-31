src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
nums = {}
for i in src:
    if i in nums:
        nums[i] += 1
    else:
        nums[i] = 1
nums_res = [i for i in src if nums[i] == 1]
print(nums_res)

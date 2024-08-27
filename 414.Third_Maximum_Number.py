nums = [3,2,1,2]
nums=list(set(nums))
if len(nums)>=3:
    nums.sort(reverse=True)
    print(nums[2])
else:
    print(max(nums))


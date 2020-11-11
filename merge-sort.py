nums = [5,3,2,22,1]

for i in range(len(nums)):
    for j in range(len(nums)):    
        if nums[i] < nums[j]: 
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        j += 1
    i += 1

print(nums)

nums = [5,3,2,22,1,5,3,2,1,55,123,2]

max = 0

for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]

countingLib = [0] * (max+1)

for i in range(len(nums)):
    countingLib[nums[i]] += 1


result = [0] * len(nums) 

count = 0

i = 0
while i < len(countingLib):
    if countingLib[i] != 0: 
        result[count] = i
        countingLib[i] -= 1
        count += 1
        i -= 1
    i += 1

nums = result
print(nums)

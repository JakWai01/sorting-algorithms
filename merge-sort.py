def mergesort(nums): 
    if len(nums) <= 1:
        return nums
    
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]

    left = mergesort(left)
    right = mergesort(right)

    nums = [0] * (len(left)+len(right))
    j = 0
    k = 0

    for i in range(len(nums)): 
        if j >= len(left):
            nums[i] = right[k]
            k += 1
            continue
        if k >= len(right):
            nums[i] = left[j]
            j += 1
            continue
        if left[j] > right[k]:
            nums[i] = right[k]
            k += 1
        else:
            nums[i] = left[j]
            j += 1
    return nums

nums = [5,9,1,3,4,6,6,3,2]
print(mergesort(nums))

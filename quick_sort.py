def pivot(arr, start, end):

    pivot = arr[start]
    low = start + 1
    high = end

    while True:
        while low <= high and arr[high] >= pivot:
            high = high - 1

        while low <= high and arr[low] <= pivot:
            low = low + 1

        if low <= high: 
            arr[low], arr[high] = arr[high], arr[low]
        else: 
            break

    arr[start], arr[high] = arr[high], arr[start]

    return high

def quick_sort(arr, start, end):
    if start >= end: 
        return
    
    p = pivot(arr, start, end)
    quick_sort(arr, start, p - 1)
    quick_sort(arr, p+1, end)

arr = [3,2,6,7,1,8]

quick_sort(arr, 0, len(arr) - 1)
print(arr)

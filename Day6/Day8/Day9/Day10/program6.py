# merge sort
# def merge(left, right):
#   result = []
#   i = 0
#   j = 0
#   while i < len(left) and j < len(right):
#       if left[i] <= right[j]:
#           result.append(left[i])
#           i += 1
#       else:
#           result.append(right[j])
#           j += 1
#   result.extend(left[i:])
#   result.extend(right[j:])
#   return result
# def merge_sort(nums):
#   if len(nums) <= 1:
#       return nums
#   mid = len(nums) // 2
#   left = merge_sort(nums[:mid])
#   right = merge_sort(nums[mid:])
#   return merge(left, right)

# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1
# def quick_sort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quick_sort(arr, low, pi - 1)
#         quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
arr=[5,4,3,2,1]
quick_sort(arr,0,len(arr)-1)
print("sorted array:",arr)
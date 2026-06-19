# def Bubblesort(nums):
#     pass
# nums=[5,4,3,1,2]
# print(Bubblesort(nums))

# def Bubblesort(nums):
#     L=len(nums)
#     for i in range(L):
#         for j in range(L-i-1):
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
#     return nums
# nums=[5,4,3,1,2]
# print(Bubblesort(nums))

# def Bubblesort(nums):
#     L=len(nums)
#     c=0
#     for j in range(L):
#         for i in range(L-1-j):
#             c+=1
#             if nums[i]>nums[i+1]:
#                 nums[i],nums[i+1]=nums[i+1],nums[i]
#             print(c,j,i,nums)    
#     return nums
# nums=[5,4,3,1,2]
# print(Bubblesort(nums))

# def Bubblesort(nums):
#     L=len(nums)
#     c=0
#     for j in range(L):
#         for i in range(L-1):
#             c+=1
#             if nums[i]>nums[i+1]:
#                 nums[i],nums[i+1]=nums[i+1],nums[i]
#             print(c,j,i,nums)    
#     return nums
# nums=list(range(80))
# print(Bubblesort(nums))

# def Bubblesort(nums):
#     L=len(nums)
#     c=0
#     for j in range(L):
#         swapped=False
#         for i in range(L-1):
#             c+=1
#             if nums[i]<nums[i+1]:
#                 nums[i],nums[i+1]=nums[i+1],nums[i]
#             print(c,j,i,nums)
#             swapped =True
#         if not swapped:
#             break
#     return nums
# nums= [3,1,2]
# print(Bubblesort(nums))

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#         print(f"Pass {i+1}: {arr}")
#     return arr
# arr = [2,5,6,7,2,4,67,9 ]
# print("Sorted:", selection_sort(arr))

# def insertion_sort(nums):
#     n = len(nums)
#     for i in range(1, n):
#         key = nums[i]
#         j = i - 1
#         while j >= 0 and nums[j] > key:
#             nums[j + 1] = nums[j]
#             j -= 1
#         nums[j + 1] = key
#         print(f"Pass {i}: {nums}")
#     return nums
# nums = [5, 4, 1, 2, 3]
# print("Sorted:", insertion_sort(nums))

# i=1
# while i<=10:
#     print(i)
#     i+=1

# i=10
# for i in range(10,0,-1):
#     print(i)

# def print_numbers(n):
#     if n > 10: 
#         return
#     print(n)
#     print_numbers(n + 1)  # Recursive call
# print_numbers(1)

# i = 20
# while i > 10:
#     print(i - 10)
#     i -= 1

# i=11
# while i>10:
#     print(10)
#     print(9)
#     break

# def count(n):
#     if n==0:
#         return
#     print(n)
#     count(n-1)
# count(10)

# def Hello():
#     for i in range(5):
#         print(i)
#         if i==2:
#             return
# print('Hello')

# def Hello():
#     for i in range(5):
#         print(i)
#         if i == 2:
#             return
# Hello()

# def count(n):
#     if n == 0:
#         return
#     print(n)
#     count(n - 1)
# count(5)

# def sum_n(n):
#     if n <= 0:
#         return 0
#     return n + sum_n(n - 1)
# print(sum_n(5))
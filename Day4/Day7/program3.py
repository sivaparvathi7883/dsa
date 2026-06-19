# find min and max
# a = 10
# b = 25
# c = 15

# print("Maximum value:", max(a, b, c))
# print("Minimum value:", min(a, b, c))

# n = input( )  

# print("Minimum digit:", min(n))
# print("Maximum digit:", max(n))

# nums=input().slit()
# print("1">"2")

# nums = list(map(int, input().split()))

# print("Max:", max(nums))
# print("Min:", min(nums))

# nums = input().split()
# print(nums)
# for i in range(len(nums)):
#     nums[i]=int(nums[i])*2
# else:
#     nums[i]=int(nums[i])*3
# print(nums)

# nums = list(map(int, input().split()))
# for i in range(1,len(nums)):
#     nums[i]=nums[i]**2
# print(nums)

# nums = list(map(int, input().split()))
# for i in range(1,len(nums)):
#     if i*i>=len(nums):
#         break
#     nums[i*i]=nums[i*i]**2
# print(nums)

# 1. Space Complexity
# - What is it?: Just like Time Complexity measures how long an algorithm takes based on input size N, Space Complexity measures how much *extra memory* an algorithm requires as N grows.
# - Auxiliary Space: The extra space or temporary space used by an algorithm, excluding the space taken by the input itself. 
# - O(1) Space: If an algorithm only uses a fixed number of variables (like a few counters or pointers) regardless of how large the input array is, its space complexity is O(1). All three sorting algorithms learned today (Bubble, Selection, Insertion) sort the array "in-place", meaning they have O(1) space complexity.
# - O(N) Space: If you create a new array of the same size as the input to help you solve the problem, the space complexity is O(N).

# nums = list(map(int, input().split()))
# list2=[]
# for i in range(1,len(nums)):
#     if i*i>=len(nums):
#         break
#     nums[i*i]=nums[i*i]**2
#     list2.append(nums[i])
# print(list2)

# nums = list(map(int, input().split()))
# print(nums)

# nums = list(map(int, input().split()))
# curr_min = float('inf')
# for i in range(len(nums)):
#     if nums[i] < curr_min:
#         curr_min = nums[i]
# print(curr_min)

# num = 3
# if num % 2 == 0:
#     if num > 1:
#         print("even positive")
#     else:
#         print("even negative")
# else:
#     if num > 0:
#         print("odd positive")
#     else:
#         print("odd negative")

# num=2
# if num%2==0 and num>1:
#     print("super number")
#     if 100%num==0:
#         print("duper number")
# elif num%2==0 and num<0:
#     print("even negative")
# elif num%2==1 and num<0:
#     print("odd negative")
# elif num%2==1 and num<1:
#     print("odd negative")

# class Solution:
#     def search(self, nums, target):
#         left = 0
#         right = len(nums) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1

# def h():
#     for i in range(3):
#         print(i)
# result=(h())
# print(result)    

# class Solution:
#     def search(self, nums, target):
#         left = 0
#         right = len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1
    

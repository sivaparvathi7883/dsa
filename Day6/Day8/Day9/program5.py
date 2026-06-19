# product of all numbers
# class ProductOfNumbers:
#     def __init__(self):
#         self.prefix = [1]
#     def add(self, num: int) -> None:
#         if num == 0:
#             self.prefix = [1]
#         else:
#             self.prefix.append(self.prefix[-1] * num)
#     def getProduct(self, k: int) -> int:
#         if k >= len(self.prefix):
#             return 0
#         return self.prefix[-1] // self.prefix[-k - 1]

# def product(nums):
#     result = 1
#     for num in nums:
#         result *= num
#     return result

# numbers=[2,6,9,1,5]
# product =1
# for num in numbers:
#     product*=num
# print("product:",product)

# numbers=[2,6,9,1,5]
# factorial =1
# for num in numbers:
#     factorial*=num
# print("factorial:",factorial)

# def factorial(n):
#     if n==0:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(10))

# nums = [5, 4, 3, 1, 2, 8]
# for i in range(len(nums) - 1):
#     if nums[i] > nums[i + 1]:
#         nums[i], nums[i + 1] = nums[i + 1], nums[i]
# print(nums)

# nums = [5, 4, 3, 1, 2, 8]
# for num in nums:
#     print([num])

# nums = [5, 4, 3, 1, 2, 8]
# result = [[num] for num in nums]
# print(result)

# nums = [5, 4, 3, 1, 2, 8]
# nums.sort()  
# result = [[num] for num in nums]  
# print(result)

# nums = [5, 4, 3, 1, 2, 8]
# size=2
# parts=[nums[i:i+size]for i in range(0, len(nums),size)]
# print(parts)

# nums=[1,2,0,4,3]
# def split(nums):
#     l=len(nums)
#     return nums[0:l//2],nums[l//2:l]
# print(split(nums))

# nums=[1,2,0,4,3]
# def s(nums):
#     if len(nums)<=1:return nums
#     L=len(nums)
#     Left=nums[:L//2]
#     Right=nums[L//2:]
#     print(s(Left),s(Right))

# nums = [1, 2, 0, 4, 3]
# def s(nums):
#     L = len(nums)
#     return nums[:L//2], nums[L//2:]
# left, right = s(nums)
# print("Left:", left)
# print("Right:", right)

# nums = [1, 2, 0, 4, 3]
# def s(nums):
#     if len(nums) <= 1:
#         print(nums)
#         return
#     L = len(nums)
#     left = nums[:L//2]
#     right = nums[L//2:]
#     s(left)
#     s(right)
# s(nums)

# nums=[5,4,3,1,2]
# def s(nums):
#     if len(nums)<=1:return nums
#     L=len(nums)
#     Left=nums[:L//2]
#     Right=nums[L//2:]
#     print(s(Left),s(Right))
#     return nums
# s(nums)
    
# nums = [5,4,3,1,2]
# def s(nums):
#     if len(nums) <= 1:
#         return nums
#     L = len(nums)
#     left = nums[:L//2]
#     right = nums[L//2:]
#     print("Left:", left, "Right:", right)
#     s(left)
#     s(right)
# s(nums)

# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     mid = len(nums) // 2
#     left = merge_sort(nums[:mid])
#     right = merge_sort(nums[mid:])
#     return sorted(left + right)
# nums = [1, 3, 4, 6, 2, 5, 7, 9]
# print(merge_sort(nums))

list1 = [1, 3, 4, 6]
list2 = [2, 5, 7, 9]
# def merge(list1, list2):
#     i = 0
#     j = 0
#     result = []
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             result.append(list1[i])
#             i += 1
#         else:
#             result.append(list2[j])
#             j += 1
#     result.extend(list1[i:])
#     result.extend(list2[j:])
#     return result
# print(merge(list1, list2))

# l1 = [1, 3, 4, 6]
# l2 = [2, 5, 7, 9]
# result = sorted(l1 + l2)
# print(result)

# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         def merge_sort(arr):
#             if len(arr) <= 1:
#                 return arr
#             mid = len(arr) // 2
#             left = merge_sort(arr[:mid])
#             right = merge_sort(arr[mid:])
#             return merge(left, right)
#         def merge(left, right):
#             i = j = 0
#             res = []
#             while i < len(left) and j < len(right):
#                 if left[i] <= right[j]:
#                     res.append(left[i])
#                     i += 1
#                 else:
#                     res.append(right[j])
#                     j += 1
#             res.extend(left[i:])
#             res.extend(right[j:])
#             return res
#         return merge_sort(nums)
    
# class Solution:
# def sortArray(self, nums: List[int]) -> List[int]:
#     return sorted(nums)

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         left, right = 0, len(numbers) - 1
#         while left < right:
#             curr_sum = numbers[left] + numbers[right]
#             if curr_sum == target:
#                 return [left + 1, right + 1]
#             elif curr_sum < target:
#                 left += 1
#             else:
#                 right -= 1

# class Solution:
#     def reverse(self, x: int) -> int:
#         rev = 0
#         while x != 0:
#             digit = x % 10 if x > 0 else -(abs(x) % 10)
#             x = x // 10 if x > 0 else -((-x) // 10)
#             if rev > 214748364 or (rev == 214748364 and digit > 7):
#                 return 0
#             if rev < -214748364 or (rev == -214748364 and digit < -8):
#                 return 0
#             rev = rev * 10 + digit
#         return rev


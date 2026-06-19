# nums=[1,2,3,4,5,6]
# for i in range(len(nums) -1,-1,-1):
#     print(nums[i])

# nums=input().split()
# L=len(nums)
# nums=nums[::-1]
# print(nums)

# nums=input().split()
# L=len(nums)
# list2=[]
# for i in range(1, L+1):
#     list2.append(nums[L-i])
# print(list2)

# nums=input().split()
# L=len(nums)
# list2=[]
# for i in range(1, L+1):
#     list2.append(nums[L-i])
# nums=list2
# for i in range(L):
#     for j in range(i+1,L):
#         print(nums[i],nums[j])

# nums=input().split()
# L=len(nums)
# list2=[]
# for i in range(1, L+1):
#     list2.append(nums[L-i])
# nums=list2
# for i in range(L):
#     for j in range(i+1,L):
#         print(nums[L-i-1])

# nums=input().split()
# L=len(nums)
# c=0
# for i in range(L):
#     for j in range(i+1,L):
#         c+=1
#         print(c,i,j,nums[L-i-1])

# c=0
# for j in range(10):
#     for i in range(10):
#         c+=1
#     print(c,j,i)

# c=0
# for j in range(1,5):
#     for i in range(6,10):
#         c+=1
#     print(c,j,i)

# t1 = 'ACb'
# t2 = 'Abc'
# t1 = t1.lower()
# t2 = t2.lower()
# if sorted(t1) == sorted(t2):
#     print("Anagram")
# else:
#     print("Not Anagram")
#     # Time Complexity:** The measure of how the execution time of an algorithm grows with the input size (n).

# n=int(input())
# for i in range(3):
#     print(i)

# n=int(input())
# for i in range(n):
#     for i in range(n):
#         print(i)

# num = int(input("Enter a number: "))
# print("Factors are:")
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)

# num = int(input("Enter a number: "))
# print("Factors of", num, "are:")
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)

# n=int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# n=int(input())
# c=0
# for i in range(1,2,5):
#         print(i)

# n=int(input())
# c=0
# for i in range(1,n//2+1):
#         if n%i==0:
#                 c+=1
#         print(c,i)
# print(n)   

# n = int(input())
# c = 0
# for i in range(1, n//2 + 1):
#     if n % i == 0:
#         c += 1
#         print(c, i)
# print(c + 1, n)
# if c == 1:
#     print("Prime Number")
# else:
#     print("Not Prime Number")

# arr = list(range(1, 1000000))  
# 000
# key = int(input("Enter element to search: "))

# for i in range(len(arr)):
#     if arr[i] == key:
#         print("Element found at index", i)
#         break
# else:
#     print("Element not found")

# list1=[]
# for i in range(1,1000000):
#     list1.append(i)
# target=99000
# list2=list(range(1,1000000))
# print(target in list2)    

# list1=[]
# for i in range(1,1000000):
#     list1.append(i)
# target=99000
# list2=list(range(1,1000000))
# for i in list2:
#     if i==target:
#         print("found")
#     else:
#         print("not found")    
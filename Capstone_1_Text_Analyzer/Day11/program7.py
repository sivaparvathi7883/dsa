# word = "madam" 
# print(word == word[::-1])

# x = 15 
# if x > 10:
#      if x < 20: 
#              print("A")  
# else:
#     print("B")

# arr = [1, 2, 3] 
# arr.append(4) 
# arr.pop(1) 
# print(arr)

# num = 8 
# if num % 2 == 0: 
#        print("Even") 
# else:
#        print("Odd")

# for num in nums:
#     print(num)

# s = "Programming" 
# print(s[3:8])

# for i in range(3): 
#     for j in range(2): 
#              print(i, j)

# a = 5
# b = a 
# a = 10
# print(a) 
# print(b)

# arr = [5, 3, 1] 
# min_idx = 0 
# for j in range(1, len(arr)): 
#       if arr[j] < arr[min_idx]: 
#                   min_idx = j 
# arr[0], arr[min_idx] = arr[min_idx], arr[0] 
# print(arr)

# count = 0 
# for i in range(5): 
#        count += 1 
# print(count)

# total = 0 
# for i in range(1, 5): 
#        total += i 
# print(total)

# def solve(n): 
#          if n == 1: 
#                return 1
#          return n + solve(n - 1)

# stack=[]
# stack.append(5)
# stack.append(6)
# print(stack)
# stack.pop()
# print(stack)
# stack.append(7)
# stack.append(4)
# print('stack',stack)
# print(stack[-1])
# print(len(stack)==0)

# stack=[5,7,6,4,3] ,T=7
# for i in stack:
#     if stack.pop()==7:
#         print("found")
#         break
# stack = [5, 7, 6, 4, 3]
# T = 7
# for i in stack:
#     if i == T:
#         print("found")

# stack = [5, 7, 6, 4, 3]
# T = 7
# print(T in stack)

# stack=[5,7,6,4,3] 
# T=7
# for i in stack:
#     if stack.pop()==7:
#         print("found")

# stack=[5,3,8,2,9]
# l=len(stack)
# t=8
# for i in stack:
#     if stack.pop()==t:
#         print("found")
#         break

# https://lovable.dev/   https://bracket-balancers-buddy.lovable.app/

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print(self.name)
# class Dog(Animal):
#     pass
# d1 = Dog("rex")
# d1.speak()

# class Student:
#     def __init__(self, name, age, branch):
#         self.name = name
#         self.age = age
#         self.branch = branch
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Branch:", self.branch)
# s1 = Student("Ravi", 20, "CSE")
# s1.display()

# class College:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
#     def display(self):
#         print("College Name:", self.name)
#         print("Location:", self.location)
# c1 = College("ABC College", "Guntur")
# c1.display()

# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print(self.name, " Woof Woof")
# d1 = Dog("Buddy")
# d2 = Dog("Max")
# d3 = Dog("Rocky")
# d1.speak()
# d2.speak()
# d3.speak()

# class Dog:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound
#     def speak(self):
#         print(self.name, "says", self.sound)
# d1 = Dog("Buddy", "Woof Woof")
# d2 = Dog("Max", "Bark Bark")
# d3 = Dog("Rocky", "Bow Bow")
# d1.speak()
# d2.speak()
# d3.speak()

# class MinStack:
#     def __init__(self):
#         self.s = []
#     def push(self, val):
#         self.s.append(val)
#     def pop(self):
#         self.s.pop()
#     def top(self):
#         return self.s[-1]
#     def getMin(self):
#         return min(self.s)

# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.minStack = []
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if not self.minStack:
#             self.minStack.append(val)
#         else:
#             self.minStack.append(min(val, self.minStack[-1]))
#     def pop(self) -> None:
#         self.stack.pop()
#         self.minStack.pop()
#     def top(self) -> int:
#         return self.stack[-1]
#     def getMin(self) -> int:
#         return self.minStack[-1]
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# print(obj.getMin())  # -3
# obj.pop()
# print(obj.top())     # 0
# print(obj.getMin())  # -2

# from collections import deque
# q=deque()
# q.append(10)
# q.append(20)
# q.append(30)
# print(q.popleft())
# print(q [0])
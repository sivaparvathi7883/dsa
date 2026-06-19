# class MaxStack:
#     def __init__(self):
#         self.s = []
#     def push(self, x):
#         self.s.append(x)
#     def pop(self):
#         return self.s.pop()
#     def top(self):
#         return self.s[-1]
#     def peekMax(self):
#         return max(self.s)
#     def popMax(self):
#         m = max(self.s)
#         self.s.remove(m)
#         return m
# st = MaxStack()
# st.push(1)
# st.push(2)
# st.push(3)
# print(st.peekMax())  # 5
# print(st.popMax())   # 5
# print(st.top())      # 1

# L1 = [3, [4, 5, 6, [1, [2, 3]]]]
# print(L1[1][3][1])

# front=0
# rear=len(2)-1
# rear=-1
# print("rear")

# def Enqueue(value):
#     global rear, size, queue
#     if size == len(queue):
#         return False
#     rear += 1
#     size += 1
#     queue[rear] = value
#     return True
# def dequeue(value)

# queue = [4] * 10
# rear = 1
# size = 8
# def Enqueue(value):
#     global rear, size, queue
#     if size == len(queue):
#         return "Queue Overflow"
#     rear += 1
#     queue[rear] = value
#     size += 1
# print(queue)
# print(rear)
# print(size)

# class CircularQueue:
#     def __init__(self, k):
#         self.queue = [0] * k
#         self.size = k
#         self.front = -1
#         self.rear = -1
#     def isFull(self):
#         return (self.rear + 1) % self.size == self.front
#     def isEmpty(self):
#         return self.front == -1
#     def enqueue(self, value):
#         if self.isFull():
#             return False
#         if self.isEmpty():
#             self.front = 0
#         self.rear = (self.rear + 1) % self.size
#         self.queue[self.rear] = value
#         return True
#     def dequeue(self):
#         if self.isEmpty():
#             return False
#         value = self.queue[self.front]
#         if self.front == self.rear:
#             self.front = self.rear = -1
#         else:
#             self.front = (self.front + 1) % self.size
#         return value
#     def peek(self):
#         if self.isEmpty():
#             return None
#         return self.queue[self.front]   

# class MyCircularQueue:

#     def __init__(self, k: int):
#         self.queue = [0] * k
#         self.size = k
#         self.front = -1
#         self.rear = -1

#     def enQueue(self, value: int) -> bool:
#         if self.isFull():
#             return False

#         if self.isEmpty():
#             self.front = 0

#         self.rear = (self.rear + 1) % self.size
#         self.queue[self.rear] = value
#         return True

#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False

#         if self.front == self.rear:
#             self.front = self.rear = -1
#         else:
#             self.front = (self.front + 1) % self.size

#         return True

#     def Front(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.queue[self.front]

#     def Rear(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.queue[self.rear]

#     def isEmpty(self) -> bool:
#         return self.front == -1

#     def isFull(self) -> bool:
#         return (self.rear + 1) % self.size == self.front

# class MyCircularQueue:
#     def __init__(self, k: int):
#         self.queue = [0] * k
#         self.k = k
#         self.front = 0
#         self.rear = -1
#         self.size = 0
#     def enQueue(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         self.rear = (self.rear + 1) % self.k
#         self.queue[self.rear] = value
#         self.size += 1
#         return True
#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False
#         self.front = (self.front + 1) % self.k
#         self.size -= 1
#         return True
#     def Front(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.queue[self.front]
#     def Rear(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.queue[self.rear]
#     def isEmpty(self) -> bool:
#         return self.size == 0
#     def isFull(self) -> bool:
#         return self.size == self.k

# class MyCircularQueue:
#     def __init__(self, k: int):
#         self.queue = [0] * k
#         self.k = k
#         self.front = 0
#         self.rear = -1
#         self.size = 0
#     def enQueue(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         self.rear = (self.rear + 1) % self.k
#         self.queue[self.rear] = value
#         self.size += 1
#         return True
#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False
#         self.front = (self.front + 1) % self.k
#         self.size -= 1
#         return True
#     def Front(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.queue[self.front]
#     def Rear(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.queue[self.rear]
#     def isEmpty(self) -> bool:
#         return self.size == 0
#     def isFull(self) -> bool:
#         return self.size == self.k
# q = MyCircularQueue(3)
# print(q.enQueue(10))  
# print(q.enQueue(20)) 
# print(q.enQueue(30))  
# print(q.enQueue(40))  
# print(q.Rear())       
# print(q.isFull())     
# print(q.deQueue())    
# print(q.enQueue(40)) 
# print(q.Rear())      
# print(q.Front())     

# class MyLinkedList:
#     def __init__(self):
#     def get(self, index: int) -> int:
#     def addAtHead(self, val: int) -> None:
#     def addAtTail(self, val: int) -> None:
#     def addAtIndex(self, index: int, val: int) -> None:
#     def deleteAtIndex(self, index: int) -> None:
        
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# Node1=Node(10)
# Node2=Node(20)
# Node1.data=30
# Node1.next=Node2
# Node1.next=None
# print(Node1.next)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# Node1 = Node(10)
# Node2 = Node(20)
# Node3 = Node(30)
# Node1.next = Node2
# Node2.next = Node3
# print(Node1.next.data)
# print(Node2.data)
# print(Node3.data)

l1=[4,5,3,7,6]
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def createList(l1):
    head=None
    temp=head
    for i in l1:
        newNode=Node(i)
    if head is None:
        head=newNode
        temp=head
        return
    if temp.next:
        temp=temp.next
    temp.next=newNode
createList(l1)

# l1 = [4, 5, 3, 7, 6]
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# def createList(l1):
#     head = None
#     temp = None
#     for i in l1:
#         newNode = Node(i)
#         if head is None:
#             head = newNode
#             temp = newNode
#         else:
#             temp.next = newNode
#             temp = newNode
#     return head
# head = createList(l1)
# current = head
# while current:
#     print(current.data, end=" -> ")
#     current = current.next
# print("None")
      































































































































































































































































































































































































































































































































































































































































































































































































































































































































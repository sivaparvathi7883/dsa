# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class SingleLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0

#     # INSERT AT START
#     def InsertAtstart(self, value):
#         newNode = Node(value)

#         if self.head is None:
#             self.head = self.tail = newNode
#         else:
#             newNode.next = self.head
#             self.head = newNode

#         self.size += 1

#     # INSERT AT END (without tail)
#     def InsertAtEnd(self, value):
#         newNode = Node(value)

#         if self.head is None:
#             self.head = self.tail = newNode
#         else:
#             curr = self.head
#             while curr.next:
#                 curr = curr.next
#             curr.next = newNode
#             self.tail = newNode

#         self.size += 1

#     # INSERT AT END (with tail)
#     def InsertAtEndwithtail(self, value):
#         newNode = Node(value)

#         if self.head is None:
#             self.head = self.tail = newNode
#         else:
#             self.tail.next = newNode
#             self.tail = newNode

#         self.size += 1

#     # DELETE START
#     def DeleteStart(self):
#         if self.head is None:
#             return -1

#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.size -= 1

#         if self.head is None:
#             self.tail = None

#     # DELETE END
#     def DeleteFromEnd(self):
#         if self.head is None:
#             return -1

#         if self.head.next is None:
#             self.head = self.tail = None
#             self.size -= 1
#             return

#         curr = self.head
#         while curr.next.next:
#             curr = curr.next

#         curr.next = None
#         self.tail = curr
#         self.size -= 1

#     # DELETE AT INDEX
#     def deleteAtIndex(self, index):
#         if self.head is None or index < 0 or index >= self.size:
#             return -1

#         if index == 0:
#             temp = self.head
#             self.head = self.head.next
#             temp.next = None
#             self.size -= 1

#             if self.head is None:
#                 self.tail = None
#             return

#         curr = self.head

#         for _ in range(index - 1):
#             curr = curr.next

#         temp = curr.next
#         curr.next = temp.next
#         temp.next = None

#         self.size -= 1

#         if curr.next is None:
#             self.tail = curr

#     # DISPLAY
#     def display(self):
#         curr = self.head

#         if curr is None:
#             print("List is empty")
#             return

#         while curr:
#             print(curr.data, end=" -> ")
#             curr = curr.next

#         print("None")
# sll = SingleLinkedList()

# sll.InsertAtstart(30)
# sll.InsertAtstart(20)
# sll.InsertAtstart(10)

# sll.InsertAtEnd(70)

# sll.display()

# sll.deleteAtIndex(3)

# sll.display()


# def reverseList(head):
#     prev = None
#     curr = head

#     while curr:
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nxt

#     return prev

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # Swap the pair
            first.next = second.next
            second.next = first
            prev.next = second

            # Move to the next pair
            prev = first

        return dummy.next
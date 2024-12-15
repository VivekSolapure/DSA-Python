class Node:
    def __init__(self,data):
        self.data=data
        self.next= None

node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

node1.next=node2
node2.next=node3
node3.next=node4

head=node1
current=head


# #Delete and begning
# head=node1.next
# current=head

# while current is not None:
#     print(current.data,end="->")
#     current=current.next
# print("None")


#Delete and end

# ahead=current.next

# while ahead is not None:
#     if ahead.next==None:
#         current.next=None
#         break
#     current=ahead
#     ahead=ahead.next

# current=head
# while current is not None:
#     print(current.data,end="->")
#     current=current.next
# print("None")


#Delete and particular

while current.next.data != 30:
    current=current.next
current.next=current.next.next

current=head
while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")
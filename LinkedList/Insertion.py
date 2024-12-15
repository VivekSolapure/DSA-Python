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

# Insert in beginng time complexity O(1/c)
# new_node=Node(5)
# new_node.next=head
# head=new_node
# current=head

# while current.next is not None:
#     print(current.data,end="->")
#     current=current.next
# print("None")


# Insert in end time complexity O(n)
# new_node=Node(50)
# current=head

# while current.next is not None:
#     current=current.next
    
# current.next=new_node
# current=head
# while current is not None:
#     print(current.data,end="->")
#     current=current.next
# print("None")


# Insert in specific time complexity O(n)
new_node=Node(50)
current=head

while current.next.data !=30:
    print(current.data,end="->")
    current=current.next

print(current.data)
new_node.next=current.next    
current.next=new_node

current=head
while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")

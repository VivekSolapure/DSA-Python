while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")
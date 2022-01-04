# Stacks follow a LIFO (Last In First Out) method


list1 = [0,1,2,3,4,5]

# Think of list1 as the following:
# Top -> 0
#        1
#        2
#        3
#        4
#        5

# Basic operations of a stack are insert, append, pop, remove, count, reverse, sort, clear, etc.
print("List =",list1,"\n")

list1.insert(0,-1)
print("Insert: Adds an element at the specified index. The '-1' is added at index 0. \n", list1)

list1.append(6)
print("Append: Adds item at end of list\n", list1)

list1.pop()
print("Pop: removes the last item from list, or the specified index.\n", list1)

list1.remove(-1)
print("Remove: Takes away the specified item from list\n", list1)

print("Count: returns the number of times the specified element appears in the list. (Count the # of times 3 appears in the list.\n",list1.count(3))

list1.reverse()
print("Reverse: reverse the list\n", list1)

list1.append(-5)
list1.append(-3)
list1.sort()
print("Sort: organize list in ascending or descending order. \n", list1)

list1.clear()
print("Clear: empty all items in list\n", list1)

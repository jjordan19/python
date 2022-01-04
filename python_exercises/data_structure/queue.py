import queue
my_queue = queue.Queue() # max item in queue is 5, default is unlimited.

# A queue is a FIFO (First In First Out — the element placed at first can be accessed at first) structure.

# Adds item in queue
my_queue.put(1)

#Check if queue is full
print("Is queue full:", my_queue.full())


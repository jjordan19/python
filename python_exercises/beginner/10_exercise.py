# Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list



def new_list(list1, list2):
    print(list1)
    print(list2)
    print("\n")
    results = []
    for i in list1:
        if i % 2 != 0:
            results.append(i)

    for i in list2:
        if i % 2 == 0:
            results.append(i)

    print("New list: ", results)


x = [10, 20, 25, 30, 35]
y = [40, 45, 60, 75, 90]

new_list(x,y)

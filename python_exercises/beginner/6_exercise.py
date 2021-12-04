#Display numbers divisible by 5 from a list

def num_div_by_5(numList):
    print("Given List: ", numList)
    for i in numList:
        if i % 5 == 0:
            print(i)

listd = [5,10,15,20,21]

num_div_by_5(listd)

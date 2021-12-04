# Check if the first and last number of a list is the same

def check_list(numberList):
    print("Given List: ", numberList)
    if numberList[0] == numberList[-1]:
        return True
    else:
        return False


given = [1,2,3,4,5,1]
given2 = [1,2,3]
print(check_list(given))
print(check_list(given2))

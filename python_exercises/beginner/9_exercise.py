# check for palindrome number

def palindrome_num(number):
    x = number
    if x == number[::-1]:
        print(number + " is a palindrome number")
    else:
        print(number + " is not a palindrome number")


p = input("Enter palindrome number: ")
palindrome_num(p)

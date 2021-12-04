#Write a Program to extract each digit from an integer in the reverse order.

def rev_num(number):
    for i in number[::-1]:
        print(i, end=" ")

x = input("Enter number: ")

rev_num(x)

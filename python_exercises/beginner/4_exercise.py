# program to remove characters from a string starting from zero up to n and return a new string

def remove_chars(str, int):
    print(str[int:])

x = input("Enter word > ")
y = int(input("Enter number > "))

if y > len(x):
    print("pick a number that's less than the total chars of your word")
    y = input("enter number again > ")
    
    remove_chars(x,y)
else:
    remove_chars(x,y)


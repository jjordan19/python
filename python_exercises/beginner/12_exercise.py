'''
Calculate income tax for the given income by adhering to the below rules

Taxable Income	Rate (in %)
First $10,000	0
Next $10,000	10
The remaining	20
'''

def income_tax(number):
    print("Taxable Income:", number)
    if int(number) < 10000:
        print("$" + number)

    if int(number) > 10000:
        x = int(number) - 10000
        zero_percent = 10000 * 0.00
        y = x - 10000 
        ten_percent = 10000 * 0.10
        remaining_percent = y * 0.20

    print("Payment:", zero_percent + ten_percent + remaining_percent)

income = input("Enter number > ")
income_tax(income)

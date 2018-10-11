## This program interacts with the customer for grocery shopping.


print('Hello!')


# input, assignment
name = input('What is your name?\n')
# \n starts a new line
print('\nHi, %s.\n' % name)


print("Fruits are healthy! What fruits would you like to buy?")
# dictionary of prices
prices = {'apple':0.40, 'orange':0.25, 'peach':0.50, 'banana':0.40}
apple = int(input('How many apples would you like?\n'))
orange = int(input('How many oranges would you like?\n'))
peach = int(input('How many peaches would you like?\n'))
banana = int(input('How many bananas would you like?\n'))
purchase = {'apple':apple, 'orange':orange, 'peach':peach, 'banana':banana}
grocery_bill = sum(prices[fruit] * purchase[fruit]
                    for fruit in purchase)
print('\nThat will be $%.2f\n' % grocery_bill)


# triple-quoted strings, while loop
print('Halloween is coming up and there is a giveaway to our customers!\n')
print('Would you like to participate?')
yes_no = input('Y or N?\n')
if yes_no == 'Y':
        print('\nHALLOWEEN GIVEAWAY!')
        candy_drain = '''
        %d candy packets on the table,
        take one down, pass it around,
        %d candy packets left!
        '''
    candy_packets = 20
    while candy_packets > 1:
        print(candy_drain % (candy_packets,
                             candy_packets - 1))
        candy_packets -= 1
else:
    print("You're no fun!\n")


# time, conditionals, from, import, for, else
print('\nWe always offer discounts according to the time you shop.\n')
from time import localtime
discount = {7: '10% off',
            8: '10% off',
            11: '2% off',
            12: '2% off',
            9: '5% off',
            10: '5% off',
            1: '50% off'}
current_time = localtime()
hour = current_time.tm_hour
for discount_time in sorted(discount.keys()):
    # runs activities time in sorted time
    if hour < discount_time:
        print(discount[discount_time])
    else:
        print('No discount :(')
    break


# discount calculations
#for total_cost in discount:
 #   if discount == '10% off':
 #       total_cost == grocery_bill*0.9
 #   elif discount == '5% off':
 #       total_cost == grocery_bill*0.95
 #   elif discount == '2% off':
 #       total_cost == grocery_bill*0.98
 #   print(total_cost)


# grocery prices csv
#import csv
# to write grocery data:
#grocery = csv.writer(open('grocery.csv', 'wb', buffering=0))
#grocery.writerows([
#        ('apple','fruta', 0.40, 1.36, 4.51)
#        ('orange','tropicana', 0.25, 1.14, 3.68)
#        ('peach','naked', 0.50, 1.43, 4.81)
#        ('banana','daily', 0.40, 1.04, 4.45)
#        ])
# to read grocery data:
#grocery_r = csv.reader(open('grocery.csv', 'wb')) 
#labels = {'fruit', 'company', 'per fruit', 'per bag', 'big bag'}
   

# def init, deposit, withdraw, overdrawn classes
print('\nDid you find everything you needed?')    
yes_no1 = input('Y or N?\n')
if yes_no1 == 'Y':
    class wallet(object):
        def __init__(money, initial_balance=0):
            money.balance = initial_balance
            # needs attribute balance
        def deposit(money, amount):
            money.balance += amount
        def withdraw(money, amount):
            money.balance -= amount
        def overdrawn(money):
            return money.balance < 0  
else:
    print('\nPlease ask a worker for help.')
wallet_now = wallet(20)
wallet_now.withdraw(5)
wallet_now.deposit(2)
print('\nYou owe ', wallet_now.balance)    
print('\nRight now, we only accept cash.')
payment = int(input('How much would you like to give me?\n'))
change =  payment - wallet_now.balance
print("Thank you. Here's you change of ", change, ".\n")
    
    
# goodbye according to time
from time import localtime
current_time = localtime()
hour = current_time.tm_hour
if hour < 10:
   print('Have a great day!')
elif hour < 18:
   print('Good night!')
else:
   print('Sweet dreams!')

'''import logic

logic.add(2,3)
logic.sub(2,3)
logic.mul(2,3)
logic.div(2,3)
logic.rem(2,3)
logic.exp(2,3)


import logic as lg

lg.add(2,3)
lg.sub(2,3)
lg.mul(2,3)
lg.div(2,3)
lg.rem(2,3)
lg.exp(2,3)



from logic import add,sub

add(2,3)
sub(4,2)
'''
'''
from logic import *

add(2,3)
sub(2,3)
mul(2,3)
div(2,3)
rem(2,3)
exp(2,3)
'''
import logic as lg

if lg.login():
    print("Welcome to the ATM")
    while True:
        lg.menu()
        ch = input("Enter the choice: ").upper()
        if ch=='C':
            lg.checkbalance()
        elif ch == 'D':
            lg.deposit()
        elif ch == 'W':
            lg.withdraw()
        elif ch == 'V':
            lg.viewtransactions()
        elif ch == 'E':
            print("--------Thankyou, Visit Again-------")
            break
        else:
            print("Enter the valid choice")

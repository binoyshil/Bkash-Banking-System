import sys

def valid_money(money,total_money):
     correct_money = False
     while correct_money == False:
        if total_money>money:

            if money >0:
                money = money
                correct_money = True
            else:
                money = int(input("Invalid Amount . Enter Valid Amount = "))
                correct_money = False
        else:
            print("Insufficient Balance . ")
            sys.exit()
            
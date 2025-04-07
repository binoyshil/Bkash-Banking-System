import random
import sys
from datetime import date
from important_info import total_amount,actual_pinn
from valid_ac_nb import valid_ac
from valid_money  import valid_money
from total_balance import update_balance


# This class is designed to make objects of "send money" program.

# Feathers are :
# step 1 : Enter the receiver account number :
# step 2: Enter the amount of money .
#step 3: Enter Reference
#step 4: Enter pin :
# step 5: Transaction successful .

def  send_money():

       total_money = total_amount()
       actual_pin = actual_pinn()
       transaction_ids = "".join(random.choice(["TXN1234567890ABCDE","TXN0987654321ZYXWV","TXN5678901234LMNOP","TXN2468135790QWERT", "TXN1357924680ASDFG","TXN9753186420HJKLO","TXN8642097531ZXCVB","TXN3141592653PIELO", "TXN1928374650MNBVC","TXN5566778899QAZWS" ]))
       from datetime import date

       today_date = date.today()
       

       
       ac_num = input("Enter Receiver Bkash Account Number : ")
       valid_ac(ac_num)


       money = int(input("Enter The Amount = "))
       valid_money(money,total_money)
    

       reference = str(input("Enter Reference = "))
       

       pin = int(input(" Enter Your PIN Number = "))
       if pin == actual_pin :
           total_money = total_money - money-5
           update_balance(total_money)
           print(f"Send money TK {money} to {ac_num} successful.\n Fee TK 5.00 . Balance TK {total_money}. \n  Reference : {reference}. TrxlD : {transaction_ids}. Date :{today_date}. ")
       else:
           print(" Your request is failed due to incorrect PIN number.")





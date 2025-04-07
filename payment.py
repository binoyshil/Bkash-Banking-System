#TAKE INPUT MARCENT BKASH ACCOUNT NUMBER / 
from datetime import date
from valid_ac_nb import valid_ac
from valid_money import valid_money 
import random
from important_info import actual_pinn,total_amount,trans_id
import sys
from total_balance import update_balance





def payment():
    marcent_ac_no =input("Enter Marcent Bkash Account Number = ")
    amount = int(input("Enter the Amount = "))
    
    
    total_money = total_amount()
    
   
    today_date = date.today()
    
    
    transaction_ids ="".join(random.choice(["TXN1234567890ABCDE","TXN0987654321ZYXWV","TXN5678901234LMNOP","TXN2468135790QWERT", "TXN1357924680ASDFG","TXN9753186420HJKLO","TXN8642097531ZXCVB","TXN3141592653PIELO", "TXN1928374650MNBVC","TXN5566778899QAZWS" ]))
    
   
    valid_ac(marcent_ac_no)

    
    
    valid_money(amount,total_money)
    
    
    actual_pin = actual_pinn()
  
    reference = str(input("Enter Reference = "))
    pin = int(input(" Enter Your PIN Number = "))
    if pin == actual_pin :
        total_money = total_money - amount
        update_balance(total_money)
        
        print(f"Payment TK {amount} TO {marcent_ac_no} successful.\n Fee TK 0.00 . Balance TK {total_money}. \n  Reference : {reference}. TrxlD : {transaction_ids}. Date :{today_date}. ")
    else:
        print(" Your request is failed due to incorrect PIN number.")



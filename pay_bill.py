from datetime import date
from valid_ac_nb import valid_ac
from valid_money import valid_money 
import random
from important_info import actual_pinn,total_amount,trans_id
from total_balance import update_balance
import sys


def payment():
    marcent_ac_no =input("Enter  Account Number = ")
    amount = int(input("Enter the Amount = "))
    month_of_bill= input("Enter Bill Month = ")
    
    
    total_money = total_amount()
    
   
    today_date = date.today()
    
    
    transaction_ids ="".join(random.choice(["TXN1234567890ABCDE","TXN0987654321ZYXWV","TXN5678901234LMNOP","TXN2468135790QWERT", "TXN1357924680ASDFG","TXN9753186420HJKLO","TXN8642097531ZXCVB","TXN3141592653PIELO", "TXN1928374650MNBVC","TXN5566778899QAZWS" ]))
    
   
    

    
    
    valid_money(amount,total_money)
    
    
    actual_pin = actual_pinn()
  
    reference = str(input("Enter Reference = "))
    pin = int(input(" Enter Your PIN Number = "))
    if pin == actual_pin :
        total_money = total_money - amount
        update_balance(total_money)
        print(f"Bill TK {amount} TO {marcent_ac_no} successful for Month { month_of_bill }.\n Fee TK 0.00 . Balance TK {total_money}. \n  Reference : {reference}. TrxlD : {transaction_ids}. Date :{today_date}. ")
    else:
        print(" Your request is failed due to incorrect PIN number.")

# Pay Bill 
#1. Electricity(Prepaid)
#2 .  Electricity (postpaid)
#3.  Gass
#4. Water 
#5. Internet and Phone 
#6. TV
#7. City Services 
#8. Education 
#9. Financial Services . 
def pay_bill():
    bill_of = int(input("Pay Bill \n \n 1. Electricity(Prepaid) \n 2. Electricity (postpaid) \n 3.  Gass \n 4. Water \n 5. Internet and Phone \n 6. TV7. City Services \n 8. Education \n 9. Financial Services .\n\n Enter == "))
    if bill_of ==1:
        payment()
    elif bill_of == 2:
        payment()
        
    elif bill_of == 3:
        payment()
        
    elif bill_of == 4:
        payment()
        
    elif bill_of == 5:
        payment()
        
    elif bill_of == 6:
        payment()
        
    elif bill_of == 7:
        payment()
    elif bill_of == 8:
        payment()
    elif bill_of == 9:
        payment()

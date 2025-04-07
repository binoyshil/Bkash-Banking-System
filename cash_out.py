from datetime import date
from valid_ac_nb import valid_ac
from valid_money import valid_money 
import random
from important_info import actual_pinn,total_amount,trans_id
import sys
from total_balance import update_balance


def cash_out_charge(amount):
       withdraw_amount = amount
       fees = round(float((amount/1000)*18),3)
       return fees


def payment():
    marcent_ac_no =input("Enter Agent Bkash Account Number = ")
    
    if len(marcent_ac_no)==11:
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
                total_money = total_money - amount-cash_out_charge(amount)
                update_balance(total_money)
                print(f"Cashout TK {amount} to {marcent_ac_no} successful.\n Fee TK {cash_out_charge(amount)} . Balance TK {total_money}. \n  Reference : {reference}. TrxlD : {transaction_ids}. Date :{today_date}. ")
            else:
                print(" Your request is failed due to incorrect PIN number.")
    else: 
        print("Invalid Number . Try Again.")
        sys.exit()    
          


# 1. From Agent 2. From ATM  3. Priyo agent Number  4. Set-up priyo agent number . 
def from_agent():
    payment()
    
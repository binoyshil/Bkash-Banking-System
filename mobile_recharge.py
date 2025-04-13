from datetime import date
from valid_ac_nb import valid_ac
from valid_money import valid_money 
import random
from important_info import actual_pinn, total_amount, trans_id
import sys
from total_balance import update_balance




def sim_check(marcent_ac_no,sim):
    if len(marcent_ac_no) == 11:
        prefix_of_sim = ['018', '016', '017', '015', '019', '013']
        
        correct_prefix = prefix_of_sim[sim-1]
        if correct_prefix == marcent_ac_no[0:3]:
                pass
            
        else:        
            print("Invalid Phone Number. Try again.")
            sys.exit()  
    else: 
        print("Invalid Number. Try Again.")
        sys.exit()    

def payment(sim):
    marcent_ac_no = input("Enter Your Phone Number = ")
    sim_check(str(marcent_ac_no),sim)
    amount = int(input("Enter the Amount = "))
    
    total_money = total_amount()
    today_date = date.today()
    
    transaction_ids = random.choice([
        "TXN1234567890ABCDE", "TXN0987654321ZYXWV", "TXN5678901234LMNOP", "TXN2468135790QWERT", 
        "TXN1357924680ASDFG", "TXN9753186420HJKLO", "TXN8642097531ZXCVB", "TXN3141592653PIELO", 
        "TXN1928374650MNBVC", "TXN5566778899QAZWS"
    ])
    
    valid_ac(marcent_ac_no)
    valid_money(amount, total_money)
   
    
    
    actual_pin = actual_pinn()
  
    pin = int(input("Enter Your PIN Number = "))
    if pin == actual_pin:
        total_money = total_money - amount
        update_balance(total_money)
        print(f"Mobile Recharge TK {amount} to {marcent_ac_no} successful.\n Fee TK 0.00 . Balance TK {total_money}. \n TrxlD : {transaction_ids}. Date :{today_date}. ")
    else:
        print("Your request is failed due to incorrect PIN number.")
        

def best_offers():
    offers = [
        "Bkash \n\n",
        "1. 1.5 GB Internet @ 129 Tk (7 days)\n",
        "2. 100 minutes @ 78 Tk (7 days)\n",
        "3. 1 GB Internet + 50 minutes @ 108 Tk (3 days)\n",
        "4. 2 GB Internet @ 129 Tk (7 days)\n",
        "5. 90 minutes @ 69 Tk (7 days)\n",
        "6. 3 GB Internet @ 148 Tk (7 days)\n",
        "7. 100 minutes @ 89 Tk (10 days)\n",
        "8. 1 GB Internet + 100 minutes @ 148 Tk (7 days)\n",
        "9. 500 MB Internet + 25 minutes @ 56 Tk (3 days)\n",
        "10. 70 minutes @ 50 Tk (7 days)\n"
    ]
    
    offers_with_out = "\n".join(offers)
    return print(offers_with_out)

def internet_packs():
    internet_offers = [
        "Bkash \n\n",
        "1. 1.5 GB Internet @ 129 Tk (7 days)\n",
        "2. 2 GB Internet @ 129 Tk (7 days)\n",
        "3. 3 GB Internet @ 148 Tk (7 days)\n",
        "4. 1 GB Internet @ 49 Tk (3 days)\n",
        "5. 2 GB Internet @ 99 Tk (10 days)\n",
        "6. 500 MB Internet @ 56 Tk (3 days)\n",
        "7. 1 GB Internet @ 89 Tk (5 days)\n",
        "8. 3 GB Internet @ 120 Tk (14 days)\n",
        "9. 1 GB Internet @ 38 Tk (3 days)\n",
        "10. 2.5 GB Internet @ 159 Tk (15 days)\n",
        "11. 5 GB Internet @ 189 Tk (15 days)\n",
        "12. 3 GB Internet @ 220 Tk (30 days)\n",
        "13. 4 GB Internet @ 240 Tk (30 days)\n",
        "14. 6 GB Internet @ 299 Tk (30 days)\n",
        "15. 10 GB Internet @ 399 Tk (30 days)"
    ]

    offers_with_out = "\n".join(internet_offers)
    return print(offers_with_out)
    
def voice_packs():
    voice_offers = [
        "Bkash \n\n",
        "1. 100 minutes @ 78 Tk (7 days)\n",
        "2. 90 minutes @ 69 Tk (7 days)\n",
        "3. 100 minutes @ 89 Tk (10 days)\n",
        "4. 70 minutes @ 50 Tk (7 days)\n",
        "5. 150 minutes @ 99 Tk (15 days)\n",
        "6. 200 minutes @ 149 Tk (15 days)\n",
        "7. 250 minutes @ 179 Tk (30 days)\n",
        "8. 300 minutes @ 199 Tk (30 days)\n",
        "9. 500 minutes @ 299 Tk (30 days)\n",
        "10. 150 minutes @ 129 Tk (10 days)\n"
    ]
    
    offers_with_out = "\n".join(voice_offers)
    return print(offers_with_out)

def bundle_packs():
    offers = [
        "Bkash \n",
        "1. 5 GB Internet + 500 minutes @ 499 Tk (30 days)\n",
        "2. 10 GB Internet + 1000 minutes @ 899 Tk (30 days)\n",
        "3. 7 GB Internet + 700 minutes @ 699 Tk (30 days)\n",
        "4. 15 GB Internet + 1500 minutes @ 1199 Tk (30 days)\n",
        "5. 20 GB Internet + 2000 minutes @ 1599 Tk (30 days)\n",
        "6. 3 GB Internet + 300 minutes @ 349 Tk (15 days)\n",
        "7. 10 GB Internet + 500 minutes @ 599 Tk (15 days)\n",
        "8. 6 GB Internet + 500 minutes @ 499 Tk (15 days)\n",
        "9. 4 GB Internet + 400 minutes @ 349 Tk (15 days)\n",
        "10. 2.5 GB Internet + 250 minutes @ 199 Tk (15 days)\n",
        "11. 12 GB Internet + 1200 minutes @ 999 Tk (30 days)\n",
        "12. 8 GB Internet + 800 minutes @ 649 Tk (30 days)\n",
        "13. 25 GB Internet + 2500 minutes @ 1999 Tk (30 days)\n",
        "14. 18 GB Internet + 1500 minutes @ 1699 Tk (30 days)\n",
        "15. 5 GB Internet + 400 minutes @ 599 Tk (30 days)\n"
    ]
    
    offers_with_out = "\n".join(offers)
    return print(offers_with_out)

def inside_sim(sim):
    recharge_type = int(input("Bkash \n 1. Prepaid \n 2. Postpaid \n 3. Auto_Recharge \n 4. Best Offers \n 5. Internet Packs \n 6. Voice Packs \n 7. Bundle Packs \n 0. Exit \n \n Enter = "))
    
    if recharge_type == 1:
        payment(sim)
    elif recharge_type == 2:
        payment(sim)
    elif recharge_type == 3:
        payment(sim)
    elif recharge_type == 4:
        best_offers()
    elif recharge_type == 5:
        internet_packs()
    elif recharge_type == 6:
        voice_packs()
    elif recharge_type == 7:
        bundle_packs()
    elif recharge_type == 0:
        print("Thank You.\n EXIT")
        sys.exit()
    else:
        print("Invalid Input. Try Again.")

# Robi, Airtel, Banglalink, Grameen, Teletalk. Main menu 
def main_recharge():
    print("Bkash \n")
    sim = int(input(" 1. Robi \n 2. Airtel\n 3. Grameen \n 4. Teletalk \n 5. Banglalink \n Enter = "))
    if 0 < sim < 6:
        
        inside_sim(sim)
    else:
        print("Invalid Input. Try again.")


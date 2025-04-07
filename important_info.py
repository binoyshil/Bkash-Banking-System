from reset_pin import actual_pin
import random
from total_balance import total_money

def actual_pinn():
    pin = actual_pin()
    return int(pin)


def total_amount():
      total = int(total_money())
      return int(total)
  
  

def reference_function ():
     reference = str(input("Enter Reference = "))
     return reference
 
 
def trans_id():
     transaction_ids ="".join(random.choice(["TXN1234567890ABCDE","TXN0987654321ZYXWV","TXN5678901234LMNOP","TXN2468135790QWERT", "TXN1357924680ASDFG","TXN9753186420HJKLO","TXN8642097531ZXCVB","TXN3141592653PIELO", "TXN1928374650MNBVC","TXN5566778899QAZWS" ]))
     return trans_id
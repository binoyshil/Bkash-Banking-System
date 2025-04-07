# Make a program as like bkash mobile version.

#Main feathers of the program are
# 1.Send money
#2. Send money to Non-bkash user
#3. Mobile Recharge
#4. Payment
#5. Cashout
#6. Pay Bill

#8. Download Bkash App
#9. My Bkash
#10. Reset PIN .
from send_money import send_money
from send_money_to_non_user import send_money_to_non
from mobile_recharge import main_recharge
from payment import payment
from cash_out import from_agent

from pay_bill import pay_bill
from download_bkash_app import download_bkash_app
from my_bkash import main_my_bkash
from reset_pin import main_pin_reset

import sys

# Main function for bKash menu
def bkash_menu():
    while True:
        print("\nWelcome to the bKash Main Menu!")
        print("1. Send Money")
        print("2. Send Money to Non-bKash User")
        print("3. Mobile Recharge")
        print("4. Payment")
        print("5. Cashout")
        print("6. Pay Bill")
       
        print("7. Download bKash App")
        print("8. My bKash")
        print("9. Reset PIN")
        print("10. Exit")

        # Take user input for selection
        choice = int(input("Enter your choice (1-11): "))

        if choice == 1:
          
            send_money()

        elif choice == 2:
           
            send_money_to_non()

        elif choice == 3:
            
            main_recharge()

        elif choice == 4:
           
            payment()
           

        elif choice == 5:
            from_agent()

        elif choice == 6:
            
            pay_bill()

        elif choice == 7:
           
            download_bkash_app()

        elif choice == 8:
            main_my_bkash()

        elif choice == 9:
            
            main_pin_reset()

    

        elif choice == 10:
            # Exit the program
            print("\nThank you for using bKash. Goodbye!")
            sys.exit()

        else:
            # Invalid input handling
            print("\nInvalid input. Please try again.")
            
            
bkash_menu()
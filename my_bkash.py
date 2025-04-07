# Feathers 
# 1. Check Balance 
# 2. Change Pin 
# 3. Priyo Numbers 
# 4. Helpline 

from total_balance import total_money
from reset_pin import main_pin_reset
import sys

def check_balance():
    total_money()
    return total_money()

def change_pin():
    main_pin_reset()

def priyo_number():
    priyo_numberr = ["01812345678", "01845667956"]  # Initial list of Priyo Numbers
    while True:
        # Menu for user interaction
        which_one = int(input("1. ADD Priyo Number\n2. View Saved Priyo Number\n3. Exit \nEnter: "))
        
        if which_one == 1:
            # Add a new Priyo number
            priyo_num = input("Enter the Number: ")
            priyo_numberr.append(priyo_num)
        elif which_one == 2:
            # View all saved Priyo numbers
            new_priyo_num = " ".join(priyo_numberr)
            print(f"Saved Priyo Numbers: {new_priyo_num}")
        elif which_one == 3:
            print("Thank You.")
            sys.exit()
        else:
            # Invalid input handling, but loop continues
            print("Invalid Input. Please try again.")
            continue

def bkash_helpline():
    while True:
        # Menu for user interaction
        print("\n MY BKASH")
        print("1. Check Balance")
        print("2. Customer Care Contact")
        print("3. Check bKash Offers")
        print("4. Exit")
        
        # Take user input
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            # Simulate checking balance
            print("\nChecking your balance...")
            # In real-world, this would connect to a system that fetches balance info.
            print(f"Your current balance is: BDT {check_balance()}")
        
        elif choice == 2:
            # Display customer care contact
            print("\nFor customer support, call 16247 or visit the nearest bKash agent.")
        
        elif choice == 3:
            # Simulate checking available offers
            print("\nHere are the current bKash offers:")
            print("1. Free transfer of up to BDT 5,000 for the next 30 days!")
            print("2. Get 10% cashback on payments for the next 7 days!")
            print("3. Enjoy 5% bonus on every mobile recharge!")
        
        elif choice == 4:
            # Exit the program
            print("\nThank you for using bKash Helpline. Have a great day!")
            break
        
        else:
            # Invalid input handling
            print("\nInvalid input. Please try again.")

def main_my_bkash():
    while True:
        # Main menu for user interaction
        print("\nMY Bkash")
        print("1. Check Balance")
        print("2. Change Pin")
        print("3. Priyo Numbers")
        print("4. Helpline")
        print("5. Exit")
        
        # Take user input
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            # Check balance
            print(f"Your current balance is: BDT {check_balance()}")
        
        elif choice == 2:
            # Change pin
            change_pin()
        
        elif choice == 3:
            # Priyo numbers
            priyo_number()
        
        elif choice == 4:
            # Helpline
            bkash_helpline()
        
        elif choice == 5:
            # Exit the program
            print("Thank you for using bKash Services. Goodbye!")
            break
        
        else:
            # Invalid input handling
            print("Invalid choice. Please try again.")

# Calling the main function to start the program

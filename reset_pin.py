
import os

FILE_NAME = "password.txt"
def actual_pin():
   FILE_NAME = "password.txt"
   with open(FILE_NAME, "r") as file:
      return file.read().strip()
  
  
  

   

def get_password():
    """Reads the stored password from the file."""
    if not os.path.exists(FILE_NAME):  # If file doesn't exist, set a default password
        with open(FILE_NAME, "w") as file:
            file.write("default123")  # Default password
    with open(FILE_NAME, "r") as file:
        return file.read().strip()
    
    
    
    
    

def set_password(new_password):
    """Updates the password in the file."""
    with open(FILE_NAME, "w") as file:
        file.write(new_password)
    print("Password updated successfully!")
    
    
    
    

def main_pin_reset():
    """Main program loop."""
    while True:
        print("\n1. View PIN")
        print("2. Change PIN")
        print("3. Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current Password:", get_password())

        elif choice == "2":
            new_pass = input("Enter new password: ")
            set_password(new_pass)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")
    

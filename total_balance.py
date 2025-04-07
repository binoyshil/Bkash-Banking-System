import os

BALANCE_FILE = "balance.txt"  # File to store balance

def total_money():
    """Loads the balance from file or sets a default initial balance."""
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as file:
            return float(file.read().strip())  # Read balance from file
    else:
        return 5000  # Default balance if file doesn't exist

def save_balance(balance):
    """Saves the updated balance to the file."""
    with open(BALANCE_FILE, "w") as file:
        file.write(str(balance))

def update_balance(net_money):
     with open(BALANCE_FILE, "w") as file:
        file.write(str(net_money))
# Example usage

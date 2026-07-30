from database import load_data,save_data
from helper import find_customer
def Deposit(customer):
    customers = load_data()
    try:
        amount = float(input("enter your amount to deposit:"))
    except ValueError:
        print("Invalid Input")
        return
    if amount<= 0:
        print("amount greater than 0")
        return
    
    for c in customers:
    
        if c["accountNo"] == customer["accountNo"]:
            c["balance"]+= amount
            c["history"]. append(f"deposited PKR{amount:,.2f}")
            save_data(customers)

            print("Deposit is successfully")
            print(f"current balance is:PKR{c['balance']:,.2f}")
            return  

def Withdraw(customer):
    customers = load_data()
    try:
        amount = float(input("enter your amount to withdraw:"))
    except ValueError:
        print("Invalid Input")
        return
    if amount<= 0:
        print("amount greater than 0")
        return
    for c in customers:
        if c["accountNo"] == customer["accountNo"]:
            if amount > c["balance"]:
                print("Insufficient Balance")
                return
                    
            c["balance"]-= amount
            c["history"]. append(f"Withdraw PKR{amount:,.2f}")
            save_data(customers)
    
            print("Withdraw Successfull")
            print(f"current balance is:PKR{c['balance']:,.2f}")
            return
    
def Transfer(customer):
    customers = load_data()
    try:
        receiver_account = int(input("Enter Receiver Account Number: "))
    except ValueError:
        print("Invalid Input")
        return
    receiver = find_customer(receiver_account)
    if not receiver:
        print("account not found")
        return
    if receiver["accountNo"] == customer["accountNo"]:
        print("you cannot transfer money in same account")
        return
    try:
        amount = float(input("enter your amount to transfer:"))
    except ValueError:
        print("Invalid Input")
        return
    if amount<=0:
        print("amount should be grater than 0")
        return
    if amount> customer["balance"]:
        print("amount should be less")
        return
    for c in customers:
        if c["accountNo"] == customer["accountNo"]:
            c["balance"] -= amount

        elif c["accountNo"] == receiver["accountNo"]:
            c["balance"] += amount
    for c in customers:
        if c["accountNo"] == customer["accountNo"]:
            c["history"].append(f"transferred PKR{amount:,.2f} to account no:{receiver['accountNo']}")

        elif c["accountNo"] == receiver["accountNo"]:
            c["history"].append(f"received PKR{amount:,.2f} from account no:{c['accountNo']}")
    save_data(customers)
    print("Transfer Successful")
    print(f"Current Balance: PKR {customer['balance']:,.2f}")
    return

def Change_PIN(customer):
    customers = load_data()
    old_pin = input("enter current pin:").strip()
    if customer["pin"] != old_pin:
        print("Incorrect Pin")
        return
    new_pin = input("Enter new pin: ").strip()
    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must be exactly 4 digits.")
        return
    if old_pin == new_pin:
        print("New PIN cannot be the same as the old PIN.")
        return
    confirm_pin = input("Enter confirm pin:").strip()
    if confirm_pin!= new_pin:
        print("pin is not matched")
        return
    for c in customers:
        if c["accountNo"] == customer["accountNo"]:
            c["pin"] = new_pin
            c["history"].append("PIN Changed Successfully")
            save_data(customers)
            print("PIN Changed Successfully")
            return

def Check_Balance(customer):
    print("="*60)
    print("Check Balance".center(60))
    print("="* 60)
    print(f"Customer Name  : {customer['name']}")
    customer = find_customer(customer["accountNo"])
    print(f"Balance        : PKR {customer['balance']:,.2f}")
    print("=" * 60)

def History(customer):
    customer = find_customer(customer["accountNo"])
    print("-" * 50)
    print("Transaction History".center(50))
    print("-" * 50)
    if not customer["history"]:
        print("no customer history found")
        return
    for transaction in customer["history"]:
        customer = find_customer(customer["accountNo"])
        print(transaction)
        print("-"*60)

def Delete_Account(customer):
    customers = load_data()
    pin = input("Enter pin to remove customer:").strip()
    if pin != customer["pin"]:
        print("Incorrect pin")
        return
    choice = input("Are you sure to remove account ? (Y/N): ").strip().upper()
    if choice =="Y":
        for c in customers:
            if c["accountNo"] == customer["accountNo"]:
                customers.remove(c)
                save_data(customers)
                print("Account Deleted Successfully")
                return
    else:
        print("Account deletion cancelled.")
    
    
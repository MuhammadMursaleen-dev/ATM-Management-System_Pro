from database import load_data,save_data
from atm import Check_Balance,Deposit,Withdraw,Delete_Account,History,Change_PIN,Transfer
from helper import display_customer,find_customer

def Create_Account():
    customers = load_data()
    try:
        accountNo = int(input("enter your account number:"))
    except ValueError:
        print("invalid input")
        return
    
    if accountNo<= 0:
        print("account number should be positive intiger")
        return
    for customer in customers:
        if customer["accountNo"] == accountNo:
            print("account number already found")
            return
    name = input("enter customer name:").strip().upper()
    if name == "":
        print("customer name should not be emppty:")
        return
    try:
        mobile = input("Enter Mobile Number: ").strip()

        if len(mobile) != 11 or not mobile.isdigit():
            print("Mobile number must be exactly 11 digits.")
            return
    except ValueError:
        print("invalid input")
        return
    try:
        CNIC = int(input("enter CNIC no:"))
        if len(str(CNIC)) != 13:
            print("CNIC should be  13 intiger")
            return
    except ValueError:
        print("invalid input")
        return
    pin = input("enter your pin:").strip()
    if len(pin) != 4 or not pin.isdigit():
        print("PIN must be exactly 4 digits.")
        return
    try:
        initial_bal = float(input("enter your initial balance:"))
    except ValueError:
        print("invalid input")
        return
    if initial_bal<= 0:
        print("balance  should not be negative intiger")
        return
    print("account creaated succisfully")
    
    new_customer = {
    "accountNo": accountNo,
    "name": name,
    "mobile": mobile,
    "CNIC": CNIC,
    "pin": pin,
    "balance": initial_bal,
    "history": [],
    "attempts": 0
}
    customers.append(new_customer)
    

    save_data(customers)
    print("=" * 50)
    print("Account Created Successfully!")
    print(f"Account Number : {accountNo}")
    print(f"Customer Name  : {name}")
    print(f"Current Balance: PKR {initial_bal:,.2f}")
    print("=" * 50)

def Search_Account():
    customers = load_data()
    if not customers:
        print("No account found")
        return
    try:
        accountNo = int(input("enter account no:"))
    except ValueError:
        print("invalid input")
        return
    customer = find_customer(accountNo)
    if customer:
        display_customer(customer)
    else:
        print("access not found")

def Login_Account():
    customers = load_data()
    if not customers:
        print("Accounts not found")
        return
    try:
        accountNo = int(input("Enter Account No:"))
    except ValueError:
        print("Invalid Input:")
        return
    customer = None

    for c in customers:
        if c["accountNo"] == accountNo:
            customer = c
            break
    if not customer:
        print("No Account Found")
        return
    if customer["attempts"] >= 3:
        print("Your Account is Locked.")
        print("Please Contact Bank.")
        return
    
    pin = input("enter your pin:").strip()
    if pin == "":
        print("pin should not empity")
        return
    if customer["pin"] == pin:
        customer["attempts"] = 0
        print(customer["attempts"])
        save_data(customers)
        print("Login Successfully")
        return customer
    else:
        customer["attempts"] += 1
        save_data(customers)
        
        print(f"Attempts Left : {3 - customer['attempts']}")
        return

            
def Show_All_Accounts():
    customers = load_data()
    if not customers:
        print("Accounts Not Founds ")
        return
    for customer in customers:
        display_customer(customer)

def ATM_Menu(customer):
    while True:
        print("========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Change PIN")
        print("6. Transaction History")
        print("7. Delete Account")
        print("8. Logout")
        print("="*60)
        choice = input("Enter your choice:").strip()
        if choice == "1":
            Check_Balance(customer)

        elif choice == "2":
            Deposit(customer)

        elif choice == "3":
            Withdraw(customer)
        elif choice == "4":
            Transfer(customer)
        elif choice == "5":
            Change_PIN(customer)
        elif choice == "6":
            History(customer)
        elif choice == "7":
            Delete_Account(customer)
        elif choice == "8":
            print("thank you for using ATM system")
            break
        



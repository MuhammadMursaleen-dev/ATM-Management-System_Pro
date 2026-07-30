from database import load_data

def find_customer(accountNo):
    customers = load_data()
    for customer in customers:
        if customer["accountNo"] == accountNo:
            return(customer)
        
    return None

def display_customer(customer):
    print("-" * 40)
    print("customer information".center(40))
    print("-" * 40)
    print(f"Account Number : {customer['accountNo']}")
    print(f"Customer Name  : {customer['name']}")
    print(f"Mobile Number  : {customer['mobile']}")
    print(f"CNIC           : {customer['CNIC']}")
    print(f"Balance        : PKR {customer['balance']:,.2f}")
    print("-" * 40)
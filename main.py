from customr import (Create_Account,Search_Account,Show_All_Accounts,Login_Account,ATM_Menu)
while True:
    print("Main Menu".center (50,"-"))

    print("1. Create Account")
    print("2. Login Account")
    print("3. Search Account")
    print("4. Show All Accounts")
    print("5. Exit")

    choice = input("enter your choice:")
    if choice == "1":
        Create_Account()
    elif choice == "2":
        customer = Login_Account()
        if customer:
            ATM_Menu(customer)
    elif choice == "3":
        Search_Account()
    elif choice == "4":
        Show_All_Accounts()
    elif choice == "5":
        print("thank you for your support")
        break


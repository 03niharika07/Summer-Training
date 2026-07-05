users = {
    "1001": {"name": "Neha", "pin": "1234", "balance": 15000},
    "1002": {"name": "Rahul", "pin": "5678", "balance": 10000},
    "1003": {"name": "Aman", "pin": "4321", "balance": 8000},
    "1004": {"name": "Priya", "pin": "1111", "balance": 20000},
    "1005": {"name": "Niharika", "pin": "8675", "balance": 15000},
    "1006": {"name": "Sam", "pin": "0101", "balance": 5000}
}

account = input("Enter Account Number: ")
pin = input("Enter 4-digit PIN: ")

if account in users and users[account]["pin"] == pin:

    print(f"\nWelcome, {users[account]['name']}!")

    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        print("==============================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print(f"Current Balance: ₹{users[account]['balance']}")

        elif choice == "2":
            amount = int(input("Enter amount to deposit: ₹"))

            if amount > 0:
                users[account]["balance"] += amount
                print("Deposit Successful!")
                print(f"Current Balance: ₹{users[account]['balance']}")
            else:
                print("Please enter a valid amount.")

        elif choice == "3":
            amount = int(input("Enter amount to withdraw: ₹"))

            if amount <= 0:
                print("Please enter a valid amount.")

            elif amount <= users[account]["balance"]:
                users[account]["balance"] -= amount
                print("Please collect your cash.")
                print(f"Remaining Balance: ₹{users[account]['balance']}")

            else:
                print("Insufficient Balance!")

        elif choice == "4":
            new_pin = input("Enter New 4-digit PIN: ")

            if len(new_pin) == 4 and new_pin.isdigit():
                users[account]["pin"] = new_pin
                print("PIN Changed Successfully!")
            else:
                print("PIN must contain exactly 4 digits.")

        elif choice == "5":
            print("Thank you for using our ATM. Have a nice day!")
            break

        else:
            print("Invalid Choice! Please select an option between 1 and 5.")

else:
    print("Invalid Account Number or PIN!")
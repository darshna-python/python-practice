balance = 1000

print("1. Check balance")
print("2. Deposit")
print("3. withdraw")

choice = int(input("Enter your choice: "))
if choice == 1:
    print("Balance = ", balance)

elif choice == 2:
    amount = int(input("Enter amount: "))
    balance = balance + amount
    print("New balance = ", balance)

elif choice == 3:
        amount = int(input("Enter amount: "))
        if amount <= balance:
             balance = balance - amount
             print("Remaining balance: ", balance)
        else:
             print("Insufficient balance")

else:
    print("Invalid choice")
    


        

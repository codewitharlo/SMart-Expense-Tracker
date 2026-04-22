print("Hello Mohit")
print("Welcome to Smart Expense Tracker Skeleton")

expenses=[]

while True:
    category=input("Enter Category (Or type [done] to Stop: ")
    if category=="done":
        print("Thank You for Using Smart Expense Tracker Skeleton")
        break
    amount=int(input("Enter Amount in Rupees: "))
    print("You spent", amount, "on", category)

    expenses.append([category, amount])
    print("New list of expenses:", expenses)
    
    total=0
    for expense in expenses:
        total=total+expense[1]
    print("Total Money Spent: ", total)
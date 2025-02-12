"""
    Your code goes below
"""


def main():
    print("Welcome to the Budget Planner and Expense Tracker!")
    monthly_income = get_monthly_income()
    expenses = {}  # Empty dictionary to store expenses

    while True:
        print("\nMenu:")
        print("1) Add an expense")
        print("2) View budget summary")
        print("3) Exit")
        
        user_choice = input("Enter your choice: ")
        
        if user_choice == "1":
            add_expense(expenses)
        elif user_choice == "2":
            display_summary(monthly_income, expenses)
        elif user_choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def get_monthly_income():
    while True:
        try:
            monthly_income = float(input("Enter your monthly income: "))
            if monthly_income >= 0:
                return monthly_income
            else:
                print("Invalid input. Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add_expense(expenses):
    category = input("Enter expense category: ")
    
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount >= 0:
                expenses[category] = expenses.get(category, 0) + amount
                print("Expense added.")
                break
            else:
                print("Invalid expense amount. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_summary(monthly_income, expenses):
    total_expenses = sum(expenses.values())
    remaining_budget = monthly_income - total_expenses
    
    print("\nBudget Summary:")
    print(f"Total Monthly Income: ${monthly_income:.2f}")
    print("Expenses:")
    
    if expenses:
        for category, amount in expenses.items():
            percentage = (amount / monthly_income) * 100 if monthly_income > 0 else 0
            print(f"{category}: ${amount:.2f} ({percentage:.2f}%)")
    else:
        print("No expenses recorded.")
    
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")

if __name__ == "__main__":
    main()




"""
function main()
    display "Welcome to the Budget Planner and Expense Tracker!"
    monthlyIncome = getMonthlyIncome()
    expenses = empty dictionary 

    loop forever:
        display menu:
            1) Add an expense
            2) View budget summary
            3) Exit 

        userChoice = read input
        if userChoice == 1:
            addExpense(expenses)
        elif userChoice == 2:
            displaySummary(monthlyIncome, expenses)
        elif userChoice == 3:
            display "Goodbye!"
            break
        else:
            display "Invalid choice. Try again."

function getMonthlyIncome():
    loop forever:
        monthlyIncome = read input
        if monthlyIncome is a valid float and >= 0:
            return monthlyIncome
        else: 
            display "Invalid input. Please enter a non-negative number."

function addExpense(expenses): 
    category = read category input 
    loop forever: 
        amount = read input 

        if amount is valid float and >=0:
            expenses[category] = expenses.get(category, 0) + amount
            display "Expense added."
            break 
        else:
            display "Invalid expense amount. Try again."

function displaySummary(monthlyIncome, expenses):
    totalExpenses = sum of all values in expenses 
    remainingBudget = monthlyIncome - totalExpenses

    display total monthlyIncome
    display each category and amount spent, plus percentage 
    display total expenses 
    display remaining budget
    
"""



"""
    Your code goes below
"""

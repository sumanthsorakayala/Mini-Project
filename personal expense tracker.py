import json
from datetime import datetime

# File to save expenses
EXPENSE_FILE = 'expenses.json'

# Load expenses from file
def load_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (e.g., Food, Transport, etc.): ")
        date_str = input("Enter date (YYYY-MM-DD) or leave empty for today: ")
        
        if date_str:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        else:
            date = datetime.now()

        expense = {
            "amount": amount,
            "category": category,
            "date": date.strftime("%Y-%m-%d")
        }
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")
    
    except ValueError:
        print("Invalid input. Please try again.")

# View summary of expenses
def view_summary(expenses):
    print("\n1. View total spending by category")
    print("2. View total overall spending")
    choice = input("Choose an option: ")

    if choice == '1':
        category = input("Enter category to view total spending: ")
        total = sum(e['amount'] for e in expenses if e['category'] == category)
        print(f"Total spending for {category}: ${total:.2f}")

    elif choice == '2':
        total = sum(e['amount'] for e in expenses)
        print(f"Total overall spending: ${total:.2f}")

# Main menu
def menu():
    expenses = load_expenses()
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

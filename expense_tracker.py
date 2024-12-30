import os  

class ExpenseTracker:  
    expenses_file = "expenses.txt"  

    def __init__(self):  
        self.expenses = []  
        self.load_expenses()  

    def load_expenses(self):  
        if os.path.exists(self.expenses_file):  
            with open(self.expenses_file, "r") as file:  
                for line in file:  
                    category, amount, date = line.strip().split(",")  
                    self.expenses.append({  
                        'category': category,  
                        'amount': float(amount),  
                        'date': date  
                    })  

    def save_expenses(self):  
        with open(self.expenses_file, "w") as file:  
            for expense in self.expenses:  
                file.write(f"{expense['category']},{expense['amount']},{expense['date']}\n")  

    def add_expense(self, category, amount, date):  
        self.expenses.append({'category': category, 'amount': amount, 'date': date})  
        self.save_expenses()  
        print("Expense added successfully!")  

    def view_expenses(self):  
        print("\nExpenses:")  
        categories = {}  
        for expense in self.expenses:  
            if expense['category'] not in categories:  
                categories[expense['category']] = 0  
            categories[expense['category']] += expense['amount']  

        for category, total in categories.items():  
            print(f"{category}: {total}")  
    
    def monthly_summary(self):  
        print("\nMonthly Summary:")  
        total_expenses = sum(expense['amount'] for expense in self.expenses)  
        print(f"Total Expenses: {total_expenses}")  

    def menu(self):  
        while True:  
            print("\nWelcome to Personal Expense Tracker!")  
            print("1. Add Expense")  
            print("2. View Expenses")  
            print("3. Monthly Summary")  
            print("4. Exit")  
            choice = input("Enter your choice: ")  

            if choice == "1":  
                category = input("Enter category: ")  
                amount = float(input("Enter amount: "))  
                date = input("Enter date (YYYY-MM-DD): ")  
                self.add_expense(category, amount, date)  
            elif choice == "2":  
                self.view_expenses()  
            elif choice == "3":  
                self.monthly_summary()  
            elif choice == "4":  
                print("Goodbye!")  
                break  

if __name__ == "__main__":  
    tracker = ExpenseTracker()  
    tracker.menu()

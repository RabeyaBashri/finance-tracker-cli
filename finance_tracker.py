from BL.transaction_manager import TransactionManager
from utilities.lists import transaction_categories
from utilities.enums import TransactionType
from functools import partial
import matplotlib.pyplot as pyplot

transaction_manager = TransactionManager()

def load_categorys(transaction_type) -> None :
     print(
            *[f"for {category},  enter :  {index}" 
                for index, category in  enumerate(transaction_categories[transaction_type], start=1)],
            sep = "\n"
          )
     
def add_transaction(transaction_type : str) -> None:

    load_categorys(transaction_type)

    category = int(input(f"Enter {transaction_type} category: "))
    amount = float(input(f"Enter {transaction_type} amount: "))

    transaction_manager.add_transaction(transaction_type, category, amount)

    print(f"✅ {transaction_type.capitalize()} added: {amount} ({transaction_categories[transaction_type][category - 1]})")

def check_budget() -> None:

    limit = float(input("Budget limit: "))
    total_expense = transaction_manager.check_budget()
    
    if total_expense > limit:
        print(f"⚠️ Budget Alert! You exceeded the limit of ${limit}.")
        print(f"   Current Expenses: ${total_expense}")
        print(f"   Over by: ${total_expense - limit}")
    else:
        print(f"✅ You are within budget. (${limit - total_expense} remaining)")

def exit_program() -> None:

    print("👋 Exiting program.")
    exit()

def monthly_summary()-> None:

    year = input("Enter year (YYYY): ")
    month = input("Enter month (MM): ")
    monthly_income, monthly_expense = transaction_manager.monthly_summary(year, month)

    total_income = sum(tx["amount"] for tx in monthly_income)
    total_exp = sum(tx["amount"] for tx in monthly_expense)
    savings = total_income - total_exp

    print(f"\n📅 Summary for {year}-{month}:")
    print(f"Total Income : ${total_income}")
    print(f"Total Expense: ${total_exp}")
    print(f"Savings      : ${savings}")

    # Pie chart for categories
    if monthly_expense:
        categories = {}
        for tx in monthly_expense:
            categories[tx["category"]] = categories.get(tx["category"], 0) + tx["amount"]

        pyplot.pie(categories.values(), labels=categories.keys(), autopct="%1.1f%%")
        pyplot.title(f"Expenses Breakdown {year}-{month}")
        pyplot.show()
    else:
        print("No expenses recorded this month.")

def plot_show_report(transaction_type : None) -> None:
       
       categories, amounts = transaction_manager.plot_show_report(transaction_type)
      
       if not categories and not  amounts:
            print("No data to plot.")
      
       if not transaction_type:
            
            total_income,total_exp,savings = amounts[0],amounts[1],amounts[2]
            print("\n📊 Report:")
            print(f"Total Income: ${total_income}")
            print(f"Total Expense: ${total_exp}")
            print(f"Savings: ${savings}")

            pyplot.bar(categories, amounts, color=["green", "red", "blue"])
            pyplot.title("Finance Overview")
            pyplot.ylabel("Amount ($)")
            pyplot.show()
       
       else:
            
            pyplot.figure(figsize=(6, 4))
            pyplot.bar(categories, amounts)
            pyplot.xlabel("Category")
            pyplot.ylabel("Amount Spent")
            pyplot.title(f"{transaction_type} by Category")
            pyplot.show()

def view_transactions(transaction_type : None) -> None :
     
     data = transaction_manager.view_transactions()
    
     if transaction_type:
            
            print(f"\n--- {transaction_type.capitalize()} Transactions ---")
            for i, tx in enumerate(data[transaction_type], start=1):
                print(f"{i}. {tx['category']} - ${tx['amount']}")
     else:
            
            print("\n--- All Transactions ---")
            for t_type, tx_list in data.items():
                print(f"\n{t_type.capitalize()}:")
                for i, tx in enumerate(tx_list, start=1):
                    print(f"{i}. {tx['category']} - ${tx['amount']}")

navigation = {
    "1": partial(add_transaction, TransactionType.Income.value),
    "2": partial(add_transaction, TransactionType.Expense.value), 
    "3": monthly_summary,
    "4": partial(plot_show_report, TransactionType.Income.value),
    "5": partial(plot_show_report, TransactionType.Expense.value),
    "6": partial(plot_show_report,None),
    "7": partial(view_transactions, TransactionType.Income.value),
    "8": partial(view_transactions, TransactionType.Expense.value),
    "9": partial(view_transactions,None),
    "10": check_budget, 
    "11": exit_program
}

def navigate():

    while True:

        print("\n--- Personal Finance Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Monthly Summary")
        print("4. Income by Category (Report)")
        print("5. Expenses by Category (Report)")
        print("6. Show full report")
        print("7. View Income Transactions")
        print("8. View Expense Transactions")
        print("9. View All Transactions")
        print("10. Check Budget")
        print("11. Exit")
        
        choice = input("Choose: ").strip()
        action = navigation.get(choice)

        if action:
            action()
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":

    navigate()


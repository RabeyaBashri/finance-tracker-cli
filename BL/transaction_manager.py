## pip install matplotlib

import sys
sys.path.append(r"DL\file_manager")
sys.path.append(r"utilities")
sys.path.append(r"BO")

from json_manager import JsonManager
from csv_manager import CSVManager
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as pyplot
from lists import transaction_categories
from enums import TransactionType
from transaction import Transaction

class TransactionManager:

    def __init__(self):
       
       ##TO ALLOW SAVE AND LOAD DATA USING JSON, UNCOMMENT THE FOLLOWING AND COMMENT CSVManager
        #self.data_manager = JsonManager()
        self.data_manager = CSVManager() 
        self.data = self.data_manager.load()

    def add_transaction(self, transaction_type : str, category : int, amount : float) -> None:
       
       ##TO ALLOW SAVE USING JSON, UNCOMMENT THE FOLLOWING AND COMMENT to_dict_csv
       #self.data[transaction_type].append(transaction.to_dict())
        transaction =  Transaction(transaction_type,category,amount)
        self.data[transaction_type].append(transaction.to_dict_csv())
        self.data_manager.save(self.data)
        
       
    def monthly_summary(self, year : int, month : int) -> tuple[list,list]:
        
        year, month = str(year), f"{int(month):02d}"  

        monthly_income = [tx for tx in self.data[TransactionType.Income.value] if tx["date"].startswith(f"{year}-{month}")]
        monthly_expense = [tx for tx in self.data[TransactionType.Expense.value] if tx["date"].startswith(f"{year}-{month}")]

        return monthly_income, monthly_expense
        

    def plot_show_report(self,transaction_type : None) -> tuple[list,list]:
        
        if not self.data:
            return
        
        categories,amounts = [],[]

        if not transaction_type:
            total_income = sum(transaction["amount"] for transaction in self.data[TransactionType.Income.value])
            total_exp = sum(transaction["amount"] for transaction in self.data[TransactionType.Expense.value])
            savings = total_income - total_exp

            categories = [tt.value for tt in TransactionType]
            amounts = [total_income, total_exp, savings]

        else:
            data = defaultdict(float)
            for transaction in self.data[transaction_type]:
                data[transaction["category"]] += transaction["amount"]

            categories = list(data.keys())
            amounts = list(data.values())

        return categories,amounts

    def view_transactions(self) -> dict[str, list[dict]]:
        return self.data

    def check_budget(self) -> int:
        return sum(transaction["amount"] for transaction in self.data[TransactionType.Expense.value])

        

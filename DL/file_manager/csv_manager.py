import sys
import os
sys.path.append(r"DL")

import csv
from file_manager import FileManager

class CSVManager(FileManager):

    def __init__(self):
    
        self.file_name = r"data\csv\personal_finance_data.csv"

    def load(self) -> dict[str, list[dict]]:

        transactions = {"Income": [], "Expense": []}
        if not os.path.exists(self.file_name):
            return transactions

        with open(self.file_name, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                transactions[row["transaction_type"]].append(row)
        return transactions

    
    def save(self, transactions: dict[str, list[dict]]):

        with open(self.file_name, mode="w", newline="") as file:

            fieldnames = ["date", "transaction_type", "category", "amount"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for t_type, tx_list in transactions.items():
                for tx in tx_list:
                    writer.writerow(tx)
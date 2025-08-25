import sys
sys.path.append(r"utilities")
from datetime import datetime
from lists import transaction_categories

class Transaction:

    def __init__(self,transaction_type : str, category, amount : float):

        self.transaction_type = transaction_type 
        self.category = transaction_categories[transaction_type][category - 1]
        self.amount = amount
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if k != "transaction_type"}
    
    def to_dict_csv(self):
        return self.__dict__

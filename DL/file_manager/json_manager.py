import os, json

import sys
sys.path.append(r"DL")

from file_manager import FileManager

class JsonManager(FileManager):

    def __init__(self):
    
        self.file_name = r"E:\python\PersonalFinanceTracker\Python_Pandas_Matplotlib_Seaborn_CLI_Version\data\json\personal_finance_data.json"

    def load(self) -> dict[str, list[dict]]:
       
        if not os.path.exists(self.file_name):
            return {"Income": [], "Expense": []}
        try:
            with open(self.file_name, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Data file corrupted, starting fresh.")
            return {"Income": [], "Expense": []}

    
    def save(self,data):
        with open(self.file_name, "w") as f:
            json.dump(data, f, indent=4)
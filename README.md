# 💰 Personal Finance Tracker (Python CLI | CSV + JSON | Matplotlib)

A **command-line personal finance tracker** built with Python.  
This project follows a **layered architecture** (Business Objects, Business Logic, Data Layer, Utilities) and supports saving transactions in **CSV or JSON**.  
It also provides **reports and visualizations** with Matplotlib.  

---

## ✨ Features
- 📥 Add **income** and **expense** transactions
- 📄 Save & load from **CSV** or **JSON**
- 📊 Reports:
  - Total income, expenses, and savings
  - Monthly summary by category
  - Budget alerts
- 🥧 Visualizations with Matplotlib
- 🏗️ Clean **3-layer architecture** for maintainability

---

## 📂 Project Structure
finance-tracker-cli/
1. finance_tracker.py # CLI entrypoint
2. BO/ # Business Objects (Transaction model)
3. BL/ # Business Logic (Transaction Manager)
4. DL/ # Data Layer (CSV & JSON managers)
5. utilities/ # Enums, category lists, helpers
6. data/ # Data storage (CSV/JSON files)

Clone the repository:
```bash
git clone https://github.com/RabeyaBashri/finance-tracker-cli.git
cd finance-tracker-cli

Install dependencies:

pip install -r requirements.txt

🤝 Contributing

Pull requests are welcome.

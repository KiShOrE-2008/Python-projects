import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime

DATA_FILE = "expenses.csv"

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        self.root.geometry("850x600")
        self.root.config(bg="#f0f4f7")

        self.transactions = []
        self.setup_ui()
        self.load_data()
        self.update_summary()

    # ------------------------ UI SETUP ------------------------
    def setup_ui(self):
        title = tk.Label(
            self.root,
            text="💰 Personal Expense Tracker",
            font=("Segoe UI", 20, "bold"),
            bg="#f0f4f7",
            fg="#2c3e50"
        )
        title.pack(pady=10)

        # Input frame
        frame = tk.Frame(self.root, bg="white", padx=10, pady=10, relief=tk.RIDGE, bd=2)
        frame.pack(pady=10)

        tk.Label(frame, text="Date (YYYY-MM-DD):", bg="white").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.date_entry = tk.Entry(frame, width=20)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)
        self.date_entry.insert(0, str(datetime.today().date()))

        tk.Label(frame, text="Type:", bg="white").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.type_var = tk.StringVar(value="expense")
        ttk.Combobox(frame, textvariable=self.type_var, values=["income", "expense"], width=18).grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame, text="Category:", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.category_entry = tk.Entry(frame, width=20)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Amount:", bg="white").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.amount_entry = tk.Entry(frame, width=20)
        self.amount_entry.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(frame, text="Description:", bg="white").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.desc_entry = tk.Entry(frame, width=62)
        self.desc_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

        tk.Button(
            frame,
            text="Add Transaction",
            bg="#27ae60",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            command=self.add_transaction
        ).grid(row=3, column=0, columnspan=4, pady=10, ipadx=10)

        # Table frame
        table_frame = tk.Frame(self.root, bg="white", padx=10, pady=10)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("date", "type", "category", "amount", "description")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, anchor="center", width=120)

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<Delete>", self.delete_selected)

        # Summary Frame
        summary_frame = tk.Frame(self.root, bg="#f0f4f7")
        summary_frame.pack(pady=10)

        self.income_label = tk.Label(summary_frame, text="Income: ₹0.00", font=("Segoe UI", 11, "bold"), fg="#27ae60", bg="#f0f4f7")
        self.income_label.grid(row=0, column=0, padx=15)

        self.expense_label = tk.Label(summary_frame, text="Expense: ₹0.00", font=("Segoe UI", 11, "bold"), fg="#c0392b", bg="#f0f4f7")
        self.expense_label.grid(row=0, column=1, padx=15)

        self.balance_label = tk.Label(summary_frame, text="Balance: ₹0.00", font=("Segoe UI", 11, "bold"), fg="#2980b9", bg="#f0f4f7")
        self.balance_label.grid(row=0, column=2, padx=15)

        tk.Button(
            self.root,
            text="Clear All Data",
            bg="#e74c3c",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            command=self.clear_all_data
        ).pack(pady=5)

    # ------------------------ DATA HANDLING ------------------------
    def load_data(self):
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, "r", newline='') as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if len(row) == 5:
                    self.transactions.append(row)
                    self.tree.insert("", "end", values=row)

    def save_data(self):
        with open(DATA_FILE, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount", "Description"])
            writer.writerows(self.transactions)

    # ------------------------ MAIN FUNCTIONS ------------------------
    def add_transaction(self):
        date = self.date_entry.get().strip()
        type_ = self.type_var.get().strip()
        category = self.category_entry.get().strip()
        amount = self.amount_entry.get().strip()
        desc = self.desc_entry.get().strip()

        if not date or not category or not amount:
            messagebox.showerror("Error", "Please fill all required fields.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number.")
            return

        new_txn = [date, type_, category, str(amount), desc]
        self.transactions.append(new_txn)
        self.tree.insert("", "end", values=new_txn)
        self.save_data()
        self.update_summary()

        # Clear input
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def delete_selected(self, event=None):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showinfo("Info", "Select a record to delete.")
            return

        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this record?")
        if not confirm:
            return

        for item in selected_item:
            values = self.tree.item(item, "values")
            if values in self.transactions:
                self.transactions.remove(list(values))
            self.tree.delete(item)

        self.save_data()
        self.update_summary()

    def clear_all_data(self):
        confirm = messagebox.askyesno("Confirm", "This will delete all data. Continue?")
        if confirm:
            self.transactions = []
            for item in self.tree.get_children():
                self.tree.delete(item)
            if os.path.exists(DATA_FILE):
                os.remove(DATA_FILE)
            self.update_summary()

    # ------------------------ SUMMARY ------------------------
    def update_summary(self):
        total_income = 0.0
        total_expense = 0.0
        for txn in self.transactions:
            type_ = txn[1]
            amount = float(txn[3])
            if type_ == "income":
                total_income += amount
            else:
                total_expense += amount

        balance = total_income - total_expense
        self.income_label.config(text=f"Income: ₹{total_income:.2f}")
        self.expense_label.config(text=f"Expense: ₹{total_expense:.2f}")
        self.balance_label.config(text=f"Balance: ₹{balance:.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

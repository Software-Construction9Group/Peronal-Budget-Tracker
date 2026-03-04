# Transaction class → Composition
class Transaction:
    def __init__(self, description, amount):
        if amount < 0:
            raise ValueError("Transaction amount cannot be negative")  # invariant
        self.description = description
        self.amount = amount


# Base BudgetTracker → Encapsulation
class BudgetTracker:
    def __init__(self):
        self.__budget = 0            # private attribute
        self.__transactions = []     # private list of Transaction objects
        self.__total_spent = 0       # private total spent

    # Encapsulated getters
    def get_budget(self):
        return self.__budget

    def get_total_spent(self):
        return self.__total_spent

    def get_transactions(self):
        return self.__transactions.copy()  # avoid direct modification

    # Encapsulated setter with validation → preserves invariance
    def set_budget(self, amount):
        if amount < 0:
            print("Budget cannot be negative.")
        else:
            self.__budget = amount

    # Method to check if budget is exceeded
    def check_budget(self):
        if self.__total_spent > self.__budget:
            print("⚠ WARNING: You have exceeded your budget!")

    # Method to add transactions
    def add_transaction(self, description, amount):
        try:
            transaction = Transaction(description, amount)  # composition
        except ValueError as e:
            print(e)
            return

        self.__transactions.append(transaction)
        self.__total_spent += amount
        print(f"Current Total Spending: UGX {self.__total_spent:.2f}")
        self.check_budget()
        print("----------------------------------")

    # Method to input budget
    def input_budget(self):
        while True:
            try:
                budget = float(input("Enter your weekly budget (UGX): "))
                if budget < 0:
                    print("Budget cannot be negative.")
                else:
                    self.set_budget(budget)
                    return
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Method to input multiple transactions
    def input_transactions(self):
        print("\nEnter at least 5 transactions.")
        print("Type 'done' when finished.\n")

        while True:
            description = input("Enter transaction description: ")
            if description.lower() == "done":
                if len(self.__transactions) < 5:
                    print("You must enter at least 5 transactions.")
                    continue
                else:
                    break

            try:
                amount = float(input("Enter transaction amount (UGX): "))
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            self.add_transaction(description, amount)

    # Method to print summary
    def print_summary(self):
        print("\n==================================")
        print("FINAL FINANCIAL SUMMARY")
        print("==================================")
        print(f"Initial Budget: UGX {self.__budget:.2f}")
        print(f"Total Expenses: UGX {self.__total_spent:.2f}")

        balance = self.__budget - self.__total_spent
        if balance >= 0:
            print(f"Remaining Balance: UGX {balance:.2f}")
        else:
            print(f"Deficit: UGX {abs(balance):.2f}")

        print("\nTransaction Log:")
        for i, t in enumerate(self.__transactions, start=1):
            print(f"{i}. {t.description} - UGX {t.amount:.2f}")


# Inheritance Example: CategoryBudgetTracker
class CategoryBudgetTracker(BudgetTracker):
    def __init__(self):
        super().__init__()  # inherit budget and transactions
        self.categories = {}  # category-wise spending

    # Add transaction with category
    def add_transaction(self, description, amount, category="General"):
        super().add_transaction(description, amount)
        if category not in self.categories:
            self.categories[category] = 0
        self.categories[category] += amount

    # Print category summary
    def print_category_summary(self):
        print("\nCategory-wise Spending:")
        for cat, amt in self.categories.items():
            print(f"{cat}: UGX {amt:.2f}")


# Main program
def main():
    print("==================================")
    print(" UNIVERSITY PERSONAL BUDGET TRACKER")
    print("==================================\n")

    tracker = CategoryBudgetTracker()  # using inheritance
    tracker.input_budget()
    tracker.input_transactions()
    tracker.print_summary()
    tracker.print_category_summary()


if __name__ == "__main__":
    main()
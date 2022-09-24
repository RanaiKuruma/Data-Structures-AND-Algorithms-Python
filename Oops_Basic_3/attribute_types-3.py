class ExpenseTracker:
    # Class Attribute 
    # remains same for all objects
    expense_version_tracker = 0.1
    '''Class Expense Tracker'''

    def __init__(self, tracker_category, opening_balance, budget):
        # Instance or Object attributes 
        #  diff for each object
        # specific to the object/instance
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.balance_budget = budget

home_tracker = ExpenseTracker('home', 0, 10000)
shopping_tracker = ExpenseTracker('shopping', 1000, 5000)

# print(home_tracker.tracker_category)

# print(home_tracker.expense_version_tracker)
# print(shopping_tracker.expense_version_tracker)

home_tracker.expense_version_tracker = 0.2 # Class Attr can be changed with specific def but it will be only applicable to the present obj
print(home_tracker.expense_version_tracker)

# shopping_tracker.expense_version_tracker
print(shopping_tracker.expense_version_tracker)
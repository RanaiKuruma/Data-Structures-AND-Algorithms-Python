class ExpenseTracker:

    # Class attribute
    expense_tracker_version = 0.1

    def __init__(self, tracker_category, opening_balance, budget):
        self.tracker_catergory = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget


home_tracker = ExpenseTracker('home', 3000, 10000)        
print(home_tracker.tracker_catergory)

shopping_tracker = ExpenseTracker('shopping', 1000, 5000)        
print(shopping_tracker.tracker_catergory)

# print(home_tracker.__dict__) # Gives the information of the attributes of the class and the values of the obj

# print(shopping_tracker.__dict__)

print(getattr(home_tracker, 'opening_balance')) # Gives information about a specific attribute

print(hasattr(shopping_tracker, 'opening_balance')) # Checks with a attribute is there or not returns a boolean value


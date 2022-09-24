class ExpenseTracker:
    # class attributes
    expense_version_tracker = 0.1
    '''Class Expense Tracker'''

    def __init__(self, track_category, original_balance, budget):
        # instance/ object attributes
        self.tracker_category = track_category
        self.original_balance = original_balance
        self.budget = budget

    # Instance method
    def get_original_balance(self):
        return self.original_balance 

    # Instance method
    def check_balance(self, limit = 1000):
        if(self.budget >= limit):
            return True
        else:
            return 'Your opening balance is less than limit' 
            
    # @ mention the type of method 
    @staticmethod 
    # Free to take arbitary no of parameters
    # Static Method is bascically creation of method without an object
    def convert_amount(amount):
        return float(amount)               

obj = ExpenseTracker("Home", 0, 1000) 
obj2 = ExpenseTracker("Business", 10000, 100000)       

# print(obj.get_original_balance())
# print(obj2.get_original_balance())
# print(obj.check_balance())

print(obj.convert_amount(1000))
print(obj2.convert_amount(10000))
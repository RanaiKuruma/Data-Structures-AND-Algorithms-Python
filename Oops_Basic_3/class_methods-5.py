class ExpenseTracker:
    
    def __init__(self, track_category, original_balance, budget):
        # instance/ object attributes
        self.tracker_category = track_category
        self.original_balance = original_balance
        self.budget = budget

    # @ mention the type of method 
    @staticmethod 
    # Free to take arbitary no of parameters
    # Static Method is bascically creation of method without an object
    def convert_amount(amount):
        return float(amount) 

    # Factory Method
    # Capable of creating new instance/object
    @classmethod
    # Only applied to the class i.e effects all the instances/object
    # global function which can effect all the instances
    def get_attributes_fromstring(cls,diary_entry:str):
        tracking_category ,opening_balance, tracker_budget = diary_entry.split(' ')   

        return ExpenseTracker(tracking_category.capitalize(),
        cls.convert_amount(opening_balance),
        cls.convert_amount(tracker_budget))


ClassObject = ExpenseTracker.get_attributes_fromstring('shopping 100 5000')
# print(ClassObject.__dict__)

# Effects all the objects/instances
print(ClassObject.tracker_category)
print(ClassObject.original_balance)
print(ClassObject.budget)

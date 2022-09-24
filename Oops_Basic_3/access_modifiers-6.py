class ExpenseTracker:
    
    def __init__(self, track_category, original_balance, budget):
        # instance/ object attributes

        #public Attribute
        self.track_category = track_category

        #private Attribute
        self.__original_balance = original_balance
        self.__budget = budget

    # Instance method
    # private Method
    def __get_original_balance(self):
        return self.original_balance 

home = ExpenseTracker('home', 0, 1000)


# To access private modifiers
# object._classname__attribute
# object._classname__function

# print(home._ExpenseTracker__original_balance)
# print(home._ExpenseTracker__budget)








# class ExpenseTracker:
#     ''' this is a docstring which defines the purpose of class, just like comments'''
#     def __init__(self):
#         pass

# obj1 = ExpenseTracker()

class ExpenseTracker:
    ''' this is a class to do expense tracking'''
    def __init__(self, date, description, transaction_type, amount): # Add class attributes
        self.date = date
        self.description = description
        self.trancsaction_type = transaction_type
        self.amount = amount


obj2 = ExpenseTracker('12 Jan', "Dinner With Friends", "Debit", '500')

obj3 = ExpenseTracker('11 Jan', "Salary Credited", "Credit", '30000')

print(obj2.date)
print(obj3.amount)


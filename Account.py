""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    def get_balance(self):
        return self.balance

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    def calculate_interest(self, months):

        monthly_interest = self.interest /12 / 100
        interest_earned = self.balance * monthly_interest * months
        return interest_earned

    # The method sets the interest gained for the account.
    def set_interest(self, months):
        """Sets the interest gained for the the account"""
        self.interest = interest

    
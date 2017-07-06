"""
An introductory look at OOP through the design of a simple credit card class.
"""

class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acc, limit):
        """
        Creates a new credit card instance with an
        initial balance of zero.

        customer -> the name of the customer
        bank     -> the name of the bank
        acc      -> the account ID
        limit    -> credit card limit
        """
        self._customer = customer
        self._bank = bank
        self._acc = acc
        self._limit = limit
        self._balance = 0

        def get_customer(self):
           """Returns the name of the card's customer."""
           return self._customer

        def get_bank(self):
           """Returns the bank that the card belongs to."""
           return self._bank

        def get_acc(self):
            """Returns the card's account ID."""
            return self._acc

        def get_limit(self):
            """Returns the card's spending limit."""
            return self._limit

        def get_balance(self):
            """Returns the card's current balance."""
            return self._balance

        def charge(self, price):
            """
            Charges the given price to the card, assuming that
            the cost incurred would still be within the customer's
            limit.

            Returns 'True' if the charge was accepted and 'False' otherwise.
            """
            if (price + self._balance <= self._limit):
                self._balance += price
                return True
            else:
                return False

        def make_payment(self, payment):
            """Reduces the card's balance by a given payment amount."""
            self._balance -= payment

class CompoundingCreditCard(CreditCard):
    """An extension to the CreditCard class which compounds interest and adds fees."""

    def __init__(self, customer, bank, acc, limit, apr):
        """
        Creates a new credit card instance with an
        initial balance of zero.

        customer -> the name of the customer
        bank     -> the name of the bank
        acc      -> the account ID
        limit    -> credit card limit
        apr      -> annual percentage rate
        """
        super().__init__(customer, bank, acc, limit)
        self._apr = apr

    def charge(self, price):
        """
        Charges the given price to the card, assuming that
        the cost incurred would still be within the customer's
        limit.

        Returns 'True' if the charge was accepted.
        Returns 'False' and adds a $5 fee otherwise.
        """
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        """Adds monthly interest on outstanding balance."""
        if (self._balance > 0):
            charge = pow(1 + self._apr, 1/12)    # converts APR to a monthly factor
            self._balance *= charge




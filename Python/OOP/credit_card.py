class CreditCard:
    """
     A consumer credit card.
    """

    def __init__(self, customer, bank, account, limit):
        """
         Create a new credit card instance.

         The initial balance is zero.

        :param customer: the name of the customer (e.g., 'John Bowman')
        :param bank: the name of the bank (e.g., 'California Savings')
        :param account: the account identifier (e.g., '5391 0375 9387 5309')
        :param limit: credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

        def get_customer(self):
            """
             Return name of the customer.

            :param self: references the instance of the class.
            :return: customer: the customer name.
            """
            return self._customer

        def get_bank(self):
            """
            Return the bank's name.

            :param self: references the instance of the class.
            :return: bank: the name of the bank.
            """
            return self._bank

        def get_account(self):
            """
            Return the card identifying number (typically stored as a string).

            :param self: references the instance of the class.
            :return: account: the account identifier.
            """
            return self._account

        def get_limit(self):
            """
            Return current credit limit.

            :param self: references the instance of the class.
            :return: limit: the credit limit.
            """
            return self._limit

        def get_balance(self):
            """
            Return current balance.

            :param self: references the instance of the class.
            :return: balance: the current balance of the account.
            """
            return self._balance

        def get_charge(self, price):
            """
            Charge given price to the card, assuming sufficient credit limit.
            Return True if charge was processed; False if charge was denied.

            :param self: references the instance of the class.
            :param price: the price of the item.
            :return: bool: True if charge was processed;
                           False if charge was denied.
            """
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True

        def make_payment(self, amount):
            """
            Process customer payment that reduces balance.

            :param self: references the instance of the class.
            :param amount: the amount to be charged.
            :return: balance: the balance of customer after deducting charge.
            """
            self._balance -= amount

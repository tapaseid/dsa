from parking_lot.exceptions import InvalidPaymentMethod


class PaymentGateway:
    def __init__(self):
        self.payment_methods = ["CASH", "DEBIT CARD", "CREDIT CARD", "UPI"]

    def do_payment(self, total_amount, payment_method):
        if payment_method not in self.payment_methods:
            raise InvalidPaymentMethod
        # returning True as mock data (only for the purpose of this project)
        return True

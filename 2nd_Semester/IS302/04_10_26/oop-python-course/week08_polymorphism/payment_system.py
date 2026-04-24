class Payment_SGB:
    def pay_SGB(self_SGB):
        print("Processing payment")

class CashPayment_SGB(Payment_SGB):
    def pay_SGB(self_SGB):
        print("Payment made using cash")

class CardPayment_SGB(Payment_SGB):
    def pay_SGB(self_SGB):
        print("Payment made using credit card")

payments_SGB = [CashPayment_SGB(), CardPayment_SGB()]
for p_SGB in payments_SGB:
    p_SGB.pay_SGB()
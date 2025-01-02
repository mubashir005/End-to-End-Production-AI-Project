from abc import ABC, abstractmethod

#Step 1: Defijne the strategy interface
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

#Step 2: implement concrete strategies
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"paying {amount} usinf=g Credit Card"
    
class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"paying {amount} usinf=g PayPal"
    
class BitCoinPayment(PaymentMethod):
    def pay(self, amount):
        return f"paying {amount} usinf=g BitCoin"

#Step 3: implement the context
class ShoppingCart:
    def __init__(self,payment_method:PaymentMethod):
        self.payment_method=payment_method
        
    def chekout(self,amount):
        return self.payment_method.pay(amount)
    
#step 4: use this strategy

if __name__ == "__main__":
    cart=ShoppingCart(CreditCardPayment())
    print(cart.chekout(100))
    
    cart = ShoppingCart (PayPalPayment())
    print(cart.chekout(200))
    
    cart =ShoppingCart(BitCoinPayment())
    print(cart.chekout(500))
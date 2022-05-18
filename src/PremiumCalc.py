class PremiumCalc:
    def __init__(self) -> None:
        self.premium = 0
    
    def add(self, number):
        self.premium += number
    
    def rate(self, rate):
        if rate > 1:
            self.premium = (self.premium * rate)
        else:
            self.premium = (self.premium * rate)

    def discount(self, amount):
        self.premium -= amount
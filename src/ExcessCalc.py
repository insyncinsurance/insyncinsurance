class ExcessCalc:
    def __init__(self) -> None:
        self.excess = 0

    def add(self, number):
        self.excess += number

    def rate(self, rate):
        if rate > 1:
            self.excess = (self.excess * rate)
        else:
            self.excess = (self.excess * rate)

    def discount(self, amount):
        self.excess -= amount
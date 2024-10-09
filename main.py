class Calculator:
    def __init__(self, symbol: str, number: float) -> None:
        self.symbol = symbol
        self.number = number

    def add(self, sk) -> float:
        return self.number + sk

    def sub(self) -> float:
        ...

    def div(self) -> float:
        ...

    def mul(self, sk) -> float:
        return self.number * sk

    def calculate(self) -> float:
        ...


print('print 1')
print('print 2')
print('print 3')

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Ділення на нуль неможливе"
        return a / b


calc = Calculator()

a = 10
b = 5

print("Додавання:", calc.add(a, b))
print("Віднімання:", calc.subtract(a, b))
print("Множення:", calc.multiply(a, b))
print("Ділення:", calc.divide(a, b))
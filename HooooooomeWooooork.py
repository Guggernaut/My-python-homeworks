class Fraction:
    def __init__(self,numertor, denumerator):
        self.numertor = numertor
        self.denumerator = denumerator

    def __add__(self, number):
        numerator = (self.numertor * number.denumerator) + (self.denumerator * number.numertor)
        denumerator = self.denumerator * number.denumerator
        return f"{numerator}/{denumerator} = {numerator / denumerator}"
    def __sub__(self, number):
        numerator = (self.numertor * number.denumerator) - (self.denumerator * number.numertor)
        denumerator = self.denumerator * number.denumerator
        return f"{numerator}/{denumerator} = {numerator / denumerator}"
    def __mul__(self, number):
        numerator = self.numertor * number.numertor
        denumerator = self.denumerator * number.denumerator
        return f"{numerator}/{denumerator} = {numerator / denumerator}"
    def __floordiv__(self, number):
        numerator = self.numertor // number.numertor
        denumerator = self.denumerator // number.denumerator
        return f"{numerator}/{denumerator} = {numerator / denumerator}"

num1 = Fraction(1, 2)
num2 = Fraction(1, 2)

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 // num2)
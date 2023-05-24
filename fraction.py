import math


class Frac:
    def __init__(self, n, d=1):
        self.n = n
        self.d = d
        self.reduce()

    def __repr__(self):
        return f'{self.n}/{self.d}'

    def __add__(self, other):
        return Frac(self.n * other.d + other.n * self.d, self.d * other.d)

    def __mul__(self, other):
        return Frac(self.n * other.n, self.d * other.d)

    def __sub__(self, other):
        return self.__add__(Frac(-other.n, other.d))

    def __truediv__(self, other):
        return self.__mul__(Frac(other.d, other.n))

    def reduce(self):
        if self.n is int and self.d is int:
            gcd = math.gcd(self.n, self.d)
            self.n //= gcd
            self.d //= gcd

    def decimal(self, precision=3):
        res = round(self.n / self.d, precision)
        return str(res).replace(".", ",")

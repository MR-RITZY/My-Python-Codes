class Fraction:
    def __init__(self, nr, dr = 1):
        self._nr = nr
        self._dr = dr
    @property
    def _dr(self):
        pass
    @_dr.setter
    def _dr(self, de):
        if not (isinstance(de, int) and isinstance(self._nr, int)):
            raise ValueError('Invalid literal for Fraction class')
        if de == 0:
            raise ZeroDivisionError('Division by Zero')
        elif de < 0:
            de *= -1
            self._nr = -self._nr
        self._de = de
    def gcd(self):
        a, b = max(abs(self._nr), abs(self._de)), \
        min(abs(self._nr), abs(self._de))
        while True:
            if b == 0:
                break
            else:
                a, b = b, a%b
        return a
    def __str__(self):
        fact = self.gcd()
        if abs(self._nr)%abs(self._de) == 0:
            print(f'{self._nr//self._de}')
        else:
            print(f'{self._nr//fact}/{self._de//fact}')
    def __mul__(self, other):
        if isinstance(other, int):
            return Fraction(self._nr*other, self._de)
        elif isinstance(other, Fraction):
            return Fraction(self._nr*other._nr, self._de*other._de)
        else:
            return Fraction(self._nr*other[0], self._de*other[1])
    def __rmul__(self, other):
      return self.__mul__(other)
    def __add__(self, other):
        if isinstance(other, int):
            return Fraction(self._nr + self._de*other, self._de)
        elif isinstance(other, Fraction):
            return Fraction(self._nr*other._de + self._de*other._nr,\
            self._de*other._de)
        else:
            return Fraction(self._nr*other[1] + self._de*other[0], self._de*other[1])
    def __radd__(self, other):
       return self.__add__(other)
    def __sub__(self, other):
        if isinstance(other, int):
            return self.__add__(-other)
        elif isinstance(other, Fraction):
            other._nr, other._de = [-other._nr, other._de]
            return self.__add__(other)
        else:
            other[0], other[1] = [-other[0], other[1]]
            return self.__add__(other)
    def __rsub__(self, other):
        return Fraction(other) - self
    def __truediv__(self, other):
        if isinstance(other, int):
            return self.__mul__(Fraction(1,other))
        elif isinstance(other, Fraction):
            other._nr, other._de = [other._de, other._nr]
            return self.__mul__(other)
        else:
            other[0], other[1] = [other[1], other[0]]
            return self.__mul__(other)
    def __rtruediv__(self, other):
        return Fraction(other)/self
    def __repr__(self):
        fact = self.gcd()
        if abs(self._nr)%abs(self._de) == 0:
            return (f'{self._nr//self._de}')
        else:
            return (f'{self._nr//fact}/{self._de//fact}')
    def reciprocal(self):
        if self._nr == 0:
            raise ZeroDivisionError('Division by Zero')
        return Fraction(self._de, self._nr)
    def negative(self):
        return Fraction(-self._nr, self._de)

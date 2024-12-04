import math
class Fraction:

    """
    A class to represent fractions and perform arithmetic operations with them.

    Attributes:
    ----------
    nume : int
        Numerator of the fraction.
    deno : int
        Denominator of the fraction.

    Methods:
    -------
    gcd():
        Returns the greatest common divisor of the numerator and denominator.
    reciprocal():
        Returns the reciprocal of the fraction.
    negative():
        Returns the negative of the fraction.
    Arithmetic and comparison operators (__add__, __sub__, __mul__, __truediv__, etc.):
        Support operations between fractions, integers, or pairs (numerator, denominator).
    """
    def __init__(self, nume, deno = 1):

        """
        Initializes a Fraction instance. Ensures the denominator is positive
        and validates the input types.
        Raises:
            ValueError: If numerator or denominator are not integers.
            ZeroDivisionError: If the denominator is zero.
        """

        if deno < 0:
            nume = -nume
            deno = -deno
        self._nume = nume
        self._deno = deno
        if not(isinstance(nume, int) and isinstance(deno, int)):
            raise ValueError('Class accept only int type')
        if deno == 0:
            raise ZeroDivisionError('Division by Zero')

    # Property methods for accessing denominator
    @property
    def deno(self):
        return self._deno

    # Property methods for accessing numerator
    @property
    def nume(self):
        return self._nume

    def gcd(self):

        """
        Computes the greatest common divisor (GCD) of the numerator and denominator.
        Returns:
            int: GCD of the numerator and denominator.
        """
        return math.gcd(self._nume, self._deno)

    def __str__(self):

        """
        Returns the string representation of the fraction in simplified form.
        """

        hcf = self.gcd()
        if abs(self._nume)%abs(self._deno) == 0:
            return f'{self._nume//self._deno}'
        else:
            return f'{self._nume//hcf}/{self._deno//hcf}'

    def __repr__(self):

        """
        Returns the string representation for debugging.
        """

        return self.__str__()


    # Arithmetic methods (__add__, __sub__, __mul__, __truediv__) handle
    # operations with fractions, integers, and (numerator, denominator) pairs.
    # Comparison methods (__eq__, __lt__, __le__, etc.) support comparisons.

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self._nume*other._deno+self._deno
            *other._nume, self._deno*other._deno)
        elif isinstance(other, int):
            return Fraction(self._nume+self._deno*other, self._deno)
        else:
            if isinstance(other, (list, tuple)):
                if len(other) == 2 and isinstance(other[0], int) and\
                isinstance(other[1], int):
                    return Fraction(self._nume*other[1]+self._deno
                    *other[0], self._deno*other[1])
                else:
                    raise ValueError('Unsupported operand')
            else:
                raise ValueError('Value not allowed')

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            other._nume, other._deno = [-other._nume, other._deno]
        elif isinstance(other, int):
            other = -other
        else:
            if isinstance(other, (list, tuple)):
                if len(other) == 2 and isinstance(other[0], int) and\
                isinstance(other[1], int):
                    other[0], other[1] = [-other[0], other[1]]
                else:
                    raise ValueError('Unsupported operand')
            else:
                raise ValueError('Value not allowed')
        return self.__add__(other)

    def __rsub__(self, other):
        if isinstance(other, int):
            return Fraction(other) - self
        else:
            if isinstance(other, (list, tuple)):
                if len(other) == 2 and isinstance(other[0], int) and\
                isinstance(other[1], int):
                    return Fraction(other[0],other[1]) - self
                else:
                    raise ValueError('Unsupported operand')
            else:
                raise ValueError('Value not allowed')
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self._nume*other._nume, self._deno*
            other._deno)
        elif isinstance(other, int):
            return Fraction(self._nume*other, self._deno)
        else:
            if isinstance(other, (list, tuple)):
                if len(other) == 2 and isinstance(other[0], int) and\
                isinstance(other[1], int):
                    return Fraction(self._nume*other[0], self._deno*
                    other[1])
                else:
                    raise ValueError('Unsupported operand')
            else:
                raise ValueError('Value not allowed')

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            other._nume, other._deno = [other._deno, other._nume]
        elif isinstance(other, int):
            return self.__mul__(Fraction(1,other))
        else:
            if isinstance(other, (list, tuple)):
                if len(other) == 2 and isinstance(other[0], int) and\
                isinstance(other[1], int):
                    other[0], other[1] = [other[1], other[0]]
                else:
                    raise ValueError('Unsupported operand')
            else:
                raise ValueError('Value not allowed')
        return self.__mul__(other)

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Fraction(other)/self
        else:
            if isinstance(other, (list, tuple)):
                if len(other) == 2 and isinstance(other[0], int) and\
                isinstance(other[1], int):
                    return Fraction(other[0],other[1])/self
                else:
                    raise ValueError('Unsupported operand')
            else:
                raise ValueError('Value not allowed')

    def reciprocal(self):

        """
        Returns the reciprocal of the fraction.
        Raises:
            ZeroDivisionError: If the numerator is zero.
        """

        if self._nume == 0:
            raise ZeroDivisionError('Division by Zero')
        return Fraction(self._deno, self._nume)

    def negative(self):

        """
        Returns the negative of the fraction.
        """

        return Fraction(-self._nume, self._deno)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self._nume/self._deno == other._nume/other._deno
        elif isinstance(other, int):
            return self._nume/self._deno == other
        elif (isinstance(other, (list, tuple))) and len(other) == 2:
            if other[1] != 0:
                return self._nume/self._deno == other[0]/other[1]
            else:
                raise ZeroDivisionError('Division by Zero')
        else:
            raise TypeError('unsupported operand')

    def __req__(self, other):
        return self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self._nume/self._deno < other._nume/other._deno
        elif isinstance(other, int):
            return self._nume/self._deno < other
        elif (isinstance(other, (list, tuple))) and len(other) == 2:
            if other[1] != 0:
                return self._nume/self._deno < other[0]/other[1]
            else:
                raise ZeroDivisionError('Division by Zero')
        else:
            raise TypeError('unsupported operand')

    def __rlt__(self, other):
        if isinstance(other, int):
            return Fraction(other) < self
        else:
            if isinstance(other, (list, tuple)):
                if len(other) == 2 and isinstance(other[0], int) and\
                isinstance(other[1], int):
                    return Fraction(other[0],other[1]) < self
                else:
                    raise ValueError('Unsupported operand')
            else:
                raise ValueError('Value not allowed')

    def __le__(self, other):
        if isinstance(other, Fraction):
            return self._nume/self._deno <= other._nume/other._deno
        elif isinstance(other, int):
            return self._nume/self._deno <= other
        elif (isinstance(other, (list, tuple))) and len(other) == 2:
            if other[1] != 0:
                return self._nume/self._deno <= other[0]/other[1]
            else:
                raise ZeroDivisionError('Division by Zero')
        else:
            raise TypeError('unsupported operand')

    def __rle__(self, other):
        if isinstance(other, int):
            return Fraction(other) <= self
        else:
            if isinstance(other, (list, tuple)):
                if len(other) == 2 and isinstance(other[0], int) and\
                isinstance(other[1], int):
                    return Fraction(other[0],other[1]) <= self
                else:
                    raise ValueError('Unsupported operand')
            else:
                raise ValueError('Value not allowed')

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self._nume/self._deno > other._nume/other._deno
        elif isinstance(other, int):
            return self._nume/self._deno > other
        elif (isinstance(other, (list, tuple))) and \
        len(other) == 2:
            if other[1] != 0:
                return self._nume/self._deno > other[0]/other[1]
            else:
                raise ZeroDivisionError('Division by Zero')
        else:
            raise TypeError('unsupported operand')
    def __rgt__(self, other):
        if isinstance(other, int):
            return Fraction(other) > self
        else:
            if isinstance(other, (list, tuple)):
                if len(other) == 2 and isinstance(other[0], int) and\
                isinstance(other[1], int):
                    return Fraction(other[0],other[1]) > self
                else:
                    raise ValueError('Unsupported operand')
            else:
                raise ValueError('Value not allowed')

    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self._nume/self._deno >= other._nume/other._deno
        elif isinstance(other, int):
            return self._nume/self._deno >= other
        elif (isinstance(other, (list, tuple))) and \
        len(other) == 2:
            if other[1] != 0:
                return self._nume/self._deno >= other[0]/other[1]
            else:
                raise ZeroDivisionError('Division by Zero')
        else:
            raise TypeError('unsupported operand')

    def __rge__(self, other):
        if isinstance(other, int):
            return Fraction(other) >= self
        else:
            if isinstance(other, (list, tuple)):
                if len(other) == 2 and isinstance(other[0], int) and\
                isinstance(other[1], int):
                    return Fraction(other[0],other[1]) >= self
                else:
                    raise ValueError('Unsupported operand')
            else:
                raise ValueError('Value not allowed')

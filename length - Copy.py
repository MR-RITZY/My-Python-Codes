class Length:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return f'{self.feet} {self.inches}'

    def add_length(self,L):
       f = self.feet + L.feet
       i = self.inches + L.inches
       if i >= 12:
           i = i - 12
       f += 1
       return Length(f, i)
    def __add__(self, other):
        if isinstance(other, Length):
            return Length(self.feet + other.feet, self.inches + \
            other.inches)
        if isinstance(other, int):
            return Length(other + self.feet, self.inches)
    def __radd__(self, other):
        return self.__add__(other)
    def add_inches(self,inches):
       f = self.feet + inches // 12
       i = self.inches + inches % 12
       if i >= 12:
           i = i - 12
       f += 1
       return Length(f, i)


length1 = Length(2,10)
length2 = Length(3,5)

print(length1 + length2)
print(length1 + 2)
print(length1 + 20)
print(20 + length1)

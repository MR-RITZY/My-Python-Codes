def collatz(x):
    y = x//2
    if 2*y != x:
      y = 3*x + 1
    print(y)
    return y
print('Enter an integer value for the collatz function')
value = int(input())
while value != 1 and value != 0:
    value = collatz(value)

def mysum(add):
    numbers = []
    add = add.split(sep = ',' '')
    for i, j in enumerate(add):
        number = int(j)
        numbers.append(number)
    addition = sum(numbers)
    return addition

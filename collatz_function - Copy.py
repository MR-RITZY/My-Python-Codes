def collatz_function(x):
    try:
        print(x)
        while x != 1 and x != 0:
            y = x//2
            if x != 2*y:
                y = 3*x + 1
            print(y)
            x = y
    except TypeError:
        print('Error: Invalid argument')




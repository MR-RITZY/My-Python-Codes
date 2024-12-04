def mysum(add, *start):
    if start == ():
       addition = sum(add)
    else:
        start = list(start)
        addition = sum(add) + start[0]
        addition = sum(add) + start[0]
    return addition

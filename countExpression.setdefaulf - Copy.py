def CountExpression(expression):
    count = {}
    import pprint
    for i in expression:
        count[i] = count.setdefault(i,0) + 1
    pprint.pprint(count)
CountExpression('It was a bright cold day in April, and the clocks were striking thirteen.')

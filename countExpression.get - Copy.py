def countExpression(expression):
    import pprint
    count = {}
    for i in expression:
        count[i] = count.get(i,0) + 1
    pprint.pprint(count)
countExpression('It was a bright cold day in April, and the clocks were striking thirteen.')

def printTable(data):
    table = {}
    item = ' '
    for i, j in enumerate(data):
        for k, l in enumerate(j):
            table[k] = table.get(k, '') + l + ' '
    a = list(table.values())
    for i,j in enumerate(a):
        if len(a[i]) > len(a[i-1]):
            b = len(a[i])
    for i, j in table.items():
        print(j.rjust(b))
Data = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]
printTable(Data )
import sys
c = sys.argv
print(c)
print(sys.argv[1])





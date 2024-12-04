def TotalGuestItems(guestRecord):
    items = list(guestRecord.values())
    thing = {}
    for i, item in enumerate(items):
        a = list(item.keys())
        b =list(item.values())
        for j, k in enumerate(a):
            thing[k] = thing.get(k,0) + b[j]
    print('Number of items brought')
    for j, k in thing.items():
        print( j + ' - ' + str(k))
import collatz_function
collatz_function.collatz_function(1000)

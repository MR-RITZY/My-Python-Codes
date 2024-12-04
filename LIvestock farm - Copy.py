def FarmStock(goods):

    goods = goods.lower()

    Farm = [[[['breeder', 'chicken'], [20_000, 10_000]],
[['breeder', 'a-day-old chick'], [300_000, 700]],
[['breeder', '6-month-old chick'], [100_000, 2_000]]],

[[['broiler', 'chicken'], [200_000, 15_000]],
[['broiler', 'a-day-old chick'], [1_000_000, 1_500]],
[['broiler', '6-month-old chick'], [500_000, 4_000]]],

[[['cockreal', 'chicken'], [50_000, 8_000]],
[['cockreal', 'a-day-old chick'],[ 500_000, 300]],
[['cockreal', '6-month-old chick'], [200_000, 1_200]]],

[[['turkey', 'local', 'chicken'], [50_000, 20_000]],
[['turkey', 'imported', 'chicken'], [10_000, 60_000]],
[['turkey', 'local', 'a-day-old chick'], [300_000, 2_000]],
[['turkey', 'imported', 'a-day-old chick'],[ 100_000, 6_000]],
[['turkey', 'local', '6-month-old chick'], [200_000, 6_000]],
[['turkey', 'imported', '6-month-old chick'], [50_000, 10_000]]],

[[['layer', 'chicken'], [20_000, 5_000]],
[['layer', 'a-day-old chick'], [300_000, 700]],
[['layer', '6-month-old chick'], [700_000, 3_000]]],

[[['egg', 'layer egg'],[ 2_000_000, 100]],
[['egg', 'turkey egg'], [500_000, 150]]]]

    Breeder, Broiler, Cockreal, Turkey, Layer, Egg = Farm[0],Farm[1],Farm[2],Farm[3],Farm[4],Farm[5],
    FarmSales = ['breeder', 'broiler', 'cockreal', 'turkey', 'layer', 'egg']

    if goods in FarmSales:
        print('Stock in Store')
        if goods != 'egg':
            age = input('How old, Chicken, a-day-old chick or 6-month-old chick?\n')
            age = age.lower()
            stock = [goods, age]
            if goods == 'turkey':
                locality = input('Which locality, Local or Imported?\n')
                locality = locality.lower()
                stock = [goods, locality, age]
        elif goods == 'egg':
            kind = input('Which kind, layer or turkey egg\n')
            kind = kind.lower()
            stock = [goods, kind]
    else:
        print('not in store')
    if stock == Breeder[0][0]:
        print('They are ' + str(Breeder[0][1][0]) + ' and ' + 'the price is #' + str(Breeder[0][1][1]))
        amount = Breeder[0][1][1]
    elif stock == Breeder[1][0]:
        print('They are ' + str(Breeder[1][1][0]) + ' and ' + 'the price is #' + str(Breeder[1][1][1]))
        amount = Breeder[1][1][1]
    elif stock == Breeder[2][0]:
        print('They are ' + str(Breeder[2][1][0]) + ' and ' + 'the price is #' + str(Breeder[2][1][1]))
        amount = Breeder[2][1][1]
    elif stock == Broiler[0][0]:
        print('They are ' + str(Broiler[0][1][0]) + ' and ' + 'the price is #' + str(Broiler[0][1][1]))
        amount = Broiler[0][1][1]
    elif stock == Broiler[1][0]:
        print('They are ' + str(Broiler[1][1][0]) + ' and ' + 'the price is #' + str(Broiler[1][1][1]))
        amount = Broiler[1][1][1]
    elif stock == Broiler[2][0]:
        print('They are ' + str(Broiler[2][1][0]) + ' and ' + 'the price is #' + str(Broiler[2][1][1]))
        amount = Broiler[2][1][1]
    elif stock == Cockreal[0][0]:
        print('They are ' + str(Cockreal[0][1][0]) + ' and ' + 'the price is #' + str(Cockreal[0][1][1]))
        amount = Cockreal[0][1][1]
    elif stock == Cockreal[1][0]:
        print('They are ' + str(Cockreal[1][1][0]) + ' and ' + 'the price is #' + str(Cockreal[1][1][1]))
        amount = Cockreal[1][1][1]
    elif stock == Cockreal[2][0]:
        print('They are ' + str(Cockreal[2][1][0]) + ' and ' + 'the price is #' + str(Cockreal[2][1][1]))
        amount = Cockreal[2][1][1]
    elif stock == Turkey[0][0]:
        print('They are ' + str(Turkey[0][1][0]) + ' and ' + 'the price is #' + str(Turkey[0][1][1]))
        amount = Turkey[0][1][1]
    elif stock == Turkey[1][0]:
        print('They are ' + str(Turkey[1][1][0]) + ' and ' + 'the price is #' + str(Turkey[1][1][1]))
        amount = Turkey[1][1][1]
    elif stock == Turkey[2][0]:
        print('They are ' + str(Turkey[2][1][0]) + ' and ' + 'the price is #' + str(Turkey[2][1][1]))
        amount = Turkey[2][1][1]
    elif stock == Turkey[3][0]:
        print('They are ' + str(Turkey[3][1][0]) + ' and ' + 'the price is #' + str(Turkey[3][1][1]))
        amount = Turkey[3][1][1]
    elif stock == Turkey[4][0]:
        print('They are ' + str(Turkey[4][1][0]) + ' and ' + 'the price is #' + str(Turkey[4][1][1]))
        amount = Turkey[4][1][1]
    elif stock == Turkey[5][0]:
        print('They are ' + str(Turkey[5][1][0]) + ' and ' + 'the price is #' + str(Turkey[5][1][1]))
        amount = Turkey[5][1][1]
    elif stock == Layer[0][0]:
        print('They are ' + str(Layer[0][1][0]) + ' and ' + 'the price is #' + str(Layer[0][1][1]))
        amount = Layer[0][1][1]
    elif stock == Layer[1][0]:
        print('They are ' + str(Layer[1][1][0]) + ' and ' + 'the price is #' + str(Layer[1][1][1]))
        amount = Layer[1][1][1]
    elif stock == Layer[2][0]:
        print('They are ' + str(Layer[2][1][0]) + ' and ' + 'the price is #' + str(Layer[2][1][1]))
        amount = Layer[2][1][1]
    elif stock == Egg[0][0]:
        print('They are ' + str(Egg[0][1][0]) + ' and ' + 'the price is #' + str(Egg[0][1][1]))
        amount = Egg[0][1][1]
    elif stock == Egg[1][0]:
        print('They are ' + str(Egg[1][1][0]) + ' and ' + 'the price is #' + str(Egg[1][1][1]))
        amount = Egg[1][1][1]
    buy = input('Dear customer, Are you still buying, Yes or No?\n')
    buy = buy.lower()
    if buy == 'yes':
        number = input('How many of it are you buying\n')
        number = int(number)
        pay = number*amount
        print('If so, you are to pay #' + str(pay) + " at the cashier in the finance department.\n Take your ordering paper, don't forget to collect the payment receipt.\n ")
    else:
        print("It's a nice time with you, please patronize us another time")

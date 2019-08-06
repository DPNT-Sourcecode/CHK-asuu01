# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    priceTable = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20,
        'H': 10,
        'I': 35,
        'J': 60,
        'K': 80,
        'L': 90,
        'M': 15,
        'N': 40,
        'O': 10,
        'P': 50,
        'Q': 30,
        'R': 50,
        'S': 30,
        'T': 20,
        'U': 40,
        'V': 50,
        'W': 20,
        'X': 90,
        'Y': 10,
        'Z': 50,
    }

    shoppingList = []
    for item in skus:
        if item not in priceTable.keys():
            return -1
        else:
            shoppingList.append(item)

    # Different savings values for promotions
    discounts = {
        '3A': 20,
        '5A': 50,
        '2B': 15,
        '5H': 5,
        '10H': 20,
        '2K': 10,
        '5P': 50,
        '3Q': 10,
        '2V': 10,
        '3V': 20
    }

    # Gather up discount item and it's count
    discountedItems = {'A': 0,
                       'B': 0,
                       'E': 0,
                       'F': 0,
                       'H': 0,
                       'K': 0,
                       'N': 0,
                       'M': 0,
                       'P': 0,
                       'Q': 0,
                       'R': 0,
                       'U': 0,
                       'V': 0}

    for discItem in discountedItems.keys():
        for item in shoppingList:
            if item == discItem:
                discountedItems[discItem] += 1

    multiplesDicountItems = ('A', 'B', 'H', 'K', 'M' 'P', 'Q', 'U', 'V')
    total = 0
    for item in shoppingList:
        if item not in multiplesDicountItems:
            total += priceTable[item]

    # Item A
    multiplesOf5A = int(discountedItems['A'] / 5)
    discountForA = ((multiplesOf5A * discounts['5A'])
                    + (int((discountedItems['A'] - multiplesOf5A * 5) / 3) * discounts['3A']))
    totalForA = discountedItems['A'] * priceTable['A'] - discountForA

    # Item B
    if discountedItems['B'] - int(discountedItems['E'] / 2) >= 0:
        discountedItems['B'] -= int(discountedItems['E'] / 2)
    else:
        discountedItems['B'] = 0

    totalForB = discountedItems['B'] * priceTable['B'] - int(discountedItems['B'] / 2) * discounts['2B']

    # Item F
    if discountedItems['F'] - int(discountedItems['F'] / 3) >= 0:
        discountedItems['F'] -= int(discountedItems['F'] / 3)
    else:
        discountedItems['F'] = 0

    totalForF = discountedItems['F'] * priceTable['F']

    # Item H
    multiplesOf10H = int(discountedItems['H'] / 10)
    discountForH = ((multiplesOf10H * discounts['10H'])
                    + (int((discountedItems['H'] - multiplesOf5A * 10) / 5) * discounts['5H']))
    totalForH = discountedItems['H'] * priceTable['H'] - discountForH

    # Item K
    multiplesOf2K = int(discountedItems['K'] / 2)
    totalForK = discountedItems['K'] * priceTable['K'] - multiplesOf2K * discounts['2K']

    # Item M
    if discountedItems['M'] - int(discountedItems['N'] / 3) >= 0:
        discountedItems['M'] -= int(discountedItems['N'] / 3)
    else:
        discountedItems['M'] = 0

    totalForM = discountedItems['M'] * priceTable['M']

    # Item P
    multiplesOf5P = int(discountedItems['P'] / 5)
    totalForP = discountedItems['P'] * priceTable['P'] - multiplesOf5P * discounts['5P']

    # Item Q
    if discountedItems['Q'] - int(discountedItems['R'] / 3) >= 0:
        discountedItems['Q'] -= int(discountedItems['R'] / 3)
    else:
        discountedItems['Q'] = 0

    totalForQ = discountedItems['Q'] * priceTable['Q'] - int(discountedItems['Q'] / 3) * discounts['3Q']

    # Item U (could combine with Item F as logic is same)
    if discountedItems['U'] - int(discountedItems['U'] / 3) >= 0:
        discountedItems['U'] -= int(discountedItems['U'] / 3)
    else:
        discountedItems['U'] = 0

    totalForU = discountedItems['U'] * priceTable['U']



    # Item V
    multiplesOf3V = int(discountedItems['V'] / 3)
    discountForV = ((multiplesOf5A * discounts['5A'])
                    + (int((discountedItems['V'] - multiplesOf3V * 3) / 2) * discounts['2V']))
    totalForV = discountedItems['V'] * priceTable['V'] - discountForV

    total = (total
             + totalForA
             + totalForB
             + totalForF
             + totalForH
             + totalForK
             + totalForM
             + totalForP
             + totalForQ
             + totalForU
             + totalForV)


    return total

print(checkout('AAAAABBEE'))



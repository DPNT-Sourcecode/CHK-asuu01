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

    discounts = {
        '3A': 20,
        '5A': 50,
        '2B': 15
    }

    # item: discount pairs
    discountedItems = {'A': 0,
                       'B': 0,
                       'E': 0,
                       'F': 0,
                       'H': 0,
                       'K': 0,
                       'N': 0,
                       'P': 0,
                       'Q': 0,
                       'R': 0,
                       'U': 0,
                       'V': 0}

    for discItem in discountedItems.keys():
        for item in shoppingList:
            if item == discItem:
                discountedItems[discItem] += 1

    total = 0

    for item in shoppingList:
        if item not in discountedItems:
            total += priceTable[item]


        if item == 'A':
            countOfA += 1
        elif item == 'B':
            countOfB += 1
        elif item == 'E':
            countOfE += 1
        elif item == 'F':
            countOfF += 1

    multiplesOf5A = int(countOfA / 5)
    discountForA = (multiplesOf5A * discounts['5A']) + (int((countOfA - multiplesOf5A * 5) / 3) * discounts['3A'])
    totalForA = countOfA * priceTable['A'] - discountForA

    if countOfB - int(countOfE / 2) >= 0:
        countOfB -= int(countOfE / 2)
    else:
        countOfB = 0

    totalForB = countOfB * priceTable['B'] - int(countOfB / 2) * discounts['2B']

    if countOfF - int(countOfF / 3) >= 0:
        countOfF -= int(countOfF / 3)
    else:
        countOfF = 0

    totalForF = countOfF * priceTable['F']

    total = total + totalForA + totalForB + totalForF

    return total

print(checkout('AAAAA'))

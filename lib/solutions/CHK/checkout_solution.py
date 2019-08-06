# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    priceTable = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10
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

    countOfA = 0
    countOfB = 0
    countOfE = 0
    countOfF = 0
    total = 0

    for item in shoppingList:
        if item in ('C', 'D', 'E'):
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

    countOfF -= int(countOfF / 3)
    totalForF = countOfF * priceTable['F']

    total = total + totalForA + totalForB + totalForF

    return total

print(checkout('FFFFFFF'))
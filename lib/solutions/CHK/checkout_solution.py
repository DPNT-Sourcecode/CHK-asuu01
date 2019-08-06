# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    knownItems = ('A', 'B', 'C', 'D', 'E')

    shoppingList = []
    for item in skus:
        if item not in knownItems:
            return -1
        else:
            shoppingList.append(item)

    priceTable = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40
    }

    countOfA = 0
    countOfB = 0
    countofE = 0
    total = 0

    for item in shoppingList:
        total += priceTable[item]

        if item == 'A':
            countOfA += 1
        elif item == 'B':
            countOfB += 1
        elif item == 'E':
            countofE += 1

    total = total - (int(countOfA / 3) * 20) - (int(countOfB / 2) * 15)

    freeBs = int(countOfE / 2)

    if freeBs and countOfB:
        # if countOfB == 1 or countOfB % 2:
        total = total - priceTable['B'] * freeBs

    return total

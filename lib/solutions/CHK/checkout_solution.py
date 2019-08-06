

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    shoppingList = [item for item in skus]

    priceTable = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    countOfA = 0
    countOfB = 0
    total = 0

    for item in shoppingList:
        total += priceTable[item]

        if item == 'A':
            countOfA += 1
        elif item == 'B':
            countOfB += 1

    total = total - (int(countOfA / 3) * 20) - (int(countOfB / 2) * 15)

    return total

print(checkout('AACDDDABB'))



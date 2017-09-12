import sys

def knapsackTable(items, maxWeight):
    finalVals = [[0] * (maxWeight + 1)
                  for i in xrange(len(items) + 1)]

    for i, (value, weight) in enumerate(items):
        #skip the first line because there's no items with 0
        i += 1
        for capacity in xrange(maxWeight + 1):
            #case 1: we can't add it
            if weight > capacity:
                finalVals[i][capacity] = finalVals[i - 1][capacity]
            #case 2: either choose previous capacity, or currItem + val of previous set
            # (but only if it fits, previous capacity - item weight)
            else:
                firstVal = finalVals[i - 1][capacity]
                secondVal = finalVals[i - 1][capacity - weight] + value
                finalVals[i][capacity] = max(firstVal, secondVal)

    # if the value was the same as the one in the previous row, no new item was chosen, do nothing
    # then we move up to the previous row, otherwise, the item is in the knapsack and we
    # subtract its weight from the remaining capacity
    includedItems = []
    i = len(items)
    j = maxWeight
    while i > 0:
        if finalVals[i][j] != finalVals[i - 1][j]:
            includedItems.append(items[i - 1])
            j -= items[i - 1][1]
        i -= 1

    # Return the best value, and the reconstruction list
    return finalVals[len(items)][maxWeight], includedItems

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as file:
        lines = file.readlines()

    maxWeight = int(lines[0])
    items = [map(int, line.split()) for line in lines[1:]]

    finalVals, includedItems = knapsackTable(items, maxWeight)

    finalWeight = 0
    s1 = ('Best Possible Value: ' + repr(finalVals))
    print(s1)
    print('Items in Knapsack:')
    for value, weight in includedItems:
        finalWeight += value
        s2 = ('Value: ' + repr(value) + ', Weight: ' + repr(weight))
        print(s2)
    s2 = ('Final Value in Knapsack: ' + repr(finalWeight))
    print (s2)

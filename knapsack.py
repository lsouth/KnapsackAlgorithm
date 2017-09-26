import sys
import time


def knapsackTable(items, maxWeight):
    finalVals = [[0] * (maxWeight + 1)
                 for i in range(len(items) + 1)]

    t0 = time.time()

    for i, (value, weight) in enumerate(items):
        # skip the first line because there's no items with 0
        i += 1
        for capacity in range(maxWeight + 1):
            # case 1: we can't add it
            if weight > capacity:
                finalVals[i][capacity] = finalVals[i - 1][capacity]
            # case 2: either choose previous capacity, or currItem + val of previous set
            # (but only if it fits, previous capacity - item weight)
            else:
                firstVal = finalVals[i - 1][capacity]
                secondVal = finalVals[i - 1][capacity - weight] + value
                finalVals[i][capacity] = max(firstVal, secondVal)

    t1 = time.time()

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

    t2 = time.time()

    s1 = ('Create Matrix Time: ' + repr(t1 - t0))
    s2 = ('Backtrack time: ' + repr(t2 - t1))
    print(s1)
    print(s2)

    # Return the best value, and the reconstruction list
    return finalVals[len(items)][maxWeight], includedItems
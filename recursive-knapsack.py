import json
import sys
import math
import objgraph

def dict_to_pref_list(prefs):
    """Takes a dict like {'1': [a,b], '2': [c,d], '3': [e,f]} and returns two lists like [[a,b],[c,d],[e,f]]"""
    return [tup[1] for tup in sorted(prefs.items())]

def read_json(filename):
    with open(filename) as f:
        return json.load(f)

output = []

def findSolution(n, capacity, weights, values):
    if n == 1:
        if weights[0] <= capacity:
            output.append([weights[0], values[0]])
            print("\tTake item with weight ", weights[0], " and value ", values[0])
        else:
            print("Don't take item with weight ", weights[0], " and value ", values[0])
    else:
        #We need to build two rows from the larger table. Both will have the same capacity. The first will be the row representing item at index n/2 and the second will be the row representing item at index n.
        row1size = (int)(math.ceil(((n-1) / 2)))
        table1 = [[0 for w in range(capacity + 1)] for j in range(row1size + 1)]
        table2 = [[0 for w in range(capacity + 1)] for j in range(row1size + 1)]

        for i in range(row1size):
            for w in range(capacity + 1):
                weight_i = weights[i]
                value_i = values[i]
                weight_i2 = weights[i + row1size]
                value_i2 = values[i + row1size]
                if weight_i > w:
                    table1[i][w] = table1[i - 1][w]
                else:
                    table1[i][w] = max(table1[i - 1][w], value_i + table1[i - 1][w - weight_i])
                if weight_i2 > w:
                    table2[i][w] = table2[i - 1][w]
                else:
                    table2[i][w] = max(table2[i-1][w], value_i2 + table2[i - 1][w - weight_i2])
        row1 = table1[row1size - 1]
        row2 = table2[row1size - 1]
        maximum = 0
        cut1 = 0
        cut2 = 0

        for i in range(capacity + 1):
            if row1[i] + row2[capacity - i] > maximum:
                maximum = row1[i] + row2[capacity - i]
                cut1 = i
                cut2 = capacity - i
        remainder = (int)(n/2)
        findSolution(remainder, cut1, weights[0:remainder], values[0:remainder])
        findSolution(remainder, cut2, weights[remainder:n], values[remainder:n])


if __name__  == "__main__":
    input = read_json(sys.argv[1])
    W = int(input[0].get("capacity"))
    weights = []
    values = []
    dictionary = dict_to_pref_list(input[1])
    for d in dictionary:
        weights.append(d[1])
        values.append(d[0])
    findSolution(len(values), W, weights, values)
    objgraph.show_most_common_types()
    print(output, sum(item[0] for item in output))
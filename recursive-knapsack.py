import json
import sys

def dict_to_pref_list(prefs):
    """Takes a dict like {'1': [a,b], '2': [c,d], '3': [e,f]} and returns two lists like [[a,b],[c,d],[e,f]]"""
    return [tup[1] for tup in sorted(prefs.items())]

def read_json(filename):
    with open(filename) as f:
        return json.load(f)

def findSolution(n, capacity, weights, values):
    if n == 1:
        print(weights)
        if weights[0] <= capacity:
            print("Take item with weight ", weights[0], " and value ", values[0])
        return
    #We need to build two rows from the larger table. Both will have the same capacity. The first will be the row representing item at index n/2 and the second will be the row representing item at index n.
    row1size = (int)((n-1) / 2)
    table1 = [[0 for w in range(capacity)] for j in range(row1size + 1)]
    table2 = [[0 for w in range(capacity)] for j in range(row1size + 1)]

    for i in range(row1size + 1):
        for w in range(capacity):
            weight_i = weights[i]
            value_i = values[i]
            weight_i2 = weights[i + row1size + 1]
            value_i2 = values[i + row1size + 1]
            if weight_i > w:
                table1[i][w] = table1[i - 1][w]
                table2[i][w] = table2[i - 1][w]
            else:
                table1[i][w] = max(table1[i-1][w], value_i + table1[i-1][w-weight_i])
                table2[i][w] = max(table2[i-1][w], value_i2 + table2[i-1][w-weight_i2])
    row1 = table1[row1size]
    row2 = table2[row1size]
    maximum = 0
    cut1 = 0
    cut2 = 0
    for i in range(capacity):
        if(row1[i] + row2[capacity - 1 - i] > maximum):
            maximum = row1[i] + row2[capacity - 1 - i]
            cut1 = i
            cut2 = capacity -  i
    print("Cutting first subproblem at ", cut1)
    print("Cutting second subproblem at ", cut2)
    remainder = (int)(n/2)
    findSolution(remainder, cut1, weights[0:remainder], values[0:remainder])
    findSolution(remainder, cut2, weights[0:remainder], values[0:remainder])


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

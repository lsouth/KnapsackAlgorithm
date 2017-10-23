import sys
import numpy as np
import time
import json
import generate_problems

#note: modified from stable_matching_helpers.py which was given as a part of Programming Assignment 6.
def dict_to_pref_list(prefs):
    """Takes a dict like {'1': [a,b], '2': [c,d], '3': [e,f]} and returns two lists like [[a,b],[c,d],[e,f]]"""
    return [tup[1] for tup in sorted(prefs.items())]

def generate_json():
    return generate_problems.create_random_problems_json_file()

def write_json(obj, filename):
    with open(filename, mode='w') as f:
        json.dump(obj, f)

def read_json(filename):
    with open(filename) as f:
        return json.load(f)

class Knapsack:
    W = 0  #max capacity
    N = 0  #total available items
    values = []
    weights = []
    table = [[]]

    def __str__(self):
        return np.matrix(self.table)

    def make_table(self):
        self.table = [[0 for x in range(self.W + 1)] for y in range(self.N + 1)]
        #skip the first line because there's no items with 0
        for i in range(0,self.W):
            self.table[0][i] = 0
        for i in range(1,self.N + 1):
            for w in range(self.W + 1):
                weight_i = int(self.weights[i])
                value_i = int(self.values[i])
                #either we set it to the previous value
                if weight_i > w:
                    self.table[i][w] = self.table[i - 1][w]
                #or we check the max between the previous value or new value
                else:
                    self.table[i][w] = max(self.table[i-1][w], value_i + self.table[i-1][w-weight_i])
        return self.table[self.N - 1][self.W - 1]

    def buildTable2(self):
        self.table = [[0 for w in range(self.W + 1)] for j in range(self.N + 1)]

        for j in range(1, self.N + 1):
            wt = self.weights[j - 1]
            vt = self.values[j - 1]
            for w in range(1, self.W + 1):
                #either we set it to the previous value
                if wt > w:
                    self.table[j][w] = self.table[j-1][w]
                #or we check the max between the previous value or new value
                else:
                    self.table[j][w] = max(self.table[j-1][w], self.table[j-1][w - wt] + vt)
        return

    def backtrack2(self):
        #the optimal value is in the bottom right corner
        opt = self.table[self.N][self.W]
        w = self.W
        result = []
        # if the value was the same as the one in the previous row, no new item was chosen, do nothing
        # then we move up to the previous row, otherwise, the item is in the knapsack and we
        # subtract its weight from the remaining capacity
        for i in range(self.N, 0, -1):
            added = self.table[i][w] != self.table[i - 1][w]
            if added:
                result.append([ self.values[i - 1], self.weights[i - 1] ])
                w -= self.weights[i - 1]
                if w < 0:
                    break
        return result

    def backtrack(self):
        opt = self.table[self.N][self.W]
        for i in range(self.N, 0, -1):
            #if you've reached the top
            if self.W == 0:
                return
            check = self.table[i - 1][self.W - int(self.weights[i])]   #0 = value, 1 = weight
            #if the value is included to create optimal value
            if check + int(self.values[i]) == opt:
                print("Take item with value ", self.values[i], " and weight ", self.weights[i])
                self.W -= int(self.weights[i])
                opt = self.table[i][self.W]

if __name__ == "__main__":
    k = Knapsack()
    input = {}
    input = read_json(sys.argv[1])

    #max capacity
    k.W = int(input[0].get("capacity"))
    #total available items
    k.N = int(len(input[1]))

    dictionary = dict_to_pref_list(input[1])
    for d in dictionary:
        k.weights.append(d[1])
        k.values.append(d[0])
    k.weights.insert(0, 0)
    k.values.insert(0, 0)

    t0 = time.process_time()
    k.buildTable2()
    t1 = time.process_time()
    print("Time to build table: ", t1 - t0)
    results = k.backtrack2()
    t2 = time.process_time()
    print("Time to backtrack: ", t2 - t1)

    print("Maximum weight in Knapsack: ", k.W)
    print("%s items in Knapsack: " % len(results))
    print("Total value in Knapsack: ",sum(r[0] for r in results))
    print("Total weight in Knapsack: ",sum(r[1] for r in results))

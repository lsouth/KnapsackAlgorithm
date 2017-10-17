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
    W = 0
    N = 0
    values = []
    weights = []
    table = [[]]

    def __str__(self):
        return np.matrix(self.table)

    def make_table(self):
        self.table = [[0 for x in range(self.W + 1)] for y in range(self.N + 1)]
        for i in range(0,self.W):
            self.table[0][i] = 0
        for i in range(1,self.N + 1):
            for w in range(self.W + 1):

                weight_i = int(self.weights[i])
                value_i = int(self.values[i])
                if weight_i > w:
                    self.table[i][w] = self.table[i - 1][w]
                else:
                    self.table[i][w] = max(self.table[i-1][w], value_i + self.table[i-1][w-weight_i])
        return self.table[self.N - 1][self.W - 1]

    def backtrack(self):
        opt = self.table[self.N][self.W]
    #    current_weight = self.W
        for i in range(self.N, 0, -1):
            if self.W == 0:
                return
            check = self.table[i - 1][self.W - int(self.weights[i])]   #0 = value, 1 = weight
            if check + int(self.values[i]) == opt:
                print("Take item with value ", self.values[i], " and weight ", self.weights[i])
                self.W -= int(self.weights[i])
                opt = self.table[i][self.W]

if __name__ == "__main__":
    k = Knapsack()
    input = {}
    input = read_json(sys.argv[1])
    k.W = int(input[0].get("capacity"))
    print("Capacity is ", k.W)
    k.N = int(len(input[1]))
    print("N is ", k.N)
    dictionary = dict_to_pref_list(input[1])
    for d in dictionary:
        k.weights.append(d[1])
        k.values.append(d[0])
    k.weights.insert(0, 0)
    k.values.insert(0, 0)
    t0 = time.process_time()
    k.make_table()
    t1 = time.process_time()
    k.backtrack()
    t2 = time.process_time()
    print("Time to build table: ", t1 - t0)
    print("Time to backtrack: ", t2 - t1)

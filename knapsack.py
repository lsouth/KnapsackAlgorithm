import sys
import numpy as np
import time
import json
import generate_problems

#note: taken (and modified) from stable_matching_helpers.py which was given as a part of Programming Assignment 6.
def dict_to_pref_list(prefs):
    """Takes a dict like {'a': 0, 'b': 1, 'c': 2} and returns two list like ['a', 'b', 'c']"""
    return [[tup[0] for tup in sorted(prefs.items())],[tup[1] for tup in sorted(prefs.items())]]

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
 #   items = []
    values = []
    weights = []
    table = [[]]

    def __str__(self):
        return np.matrix(self.table)

#    def read_input(self, filename):
        #expected input:
        # W (total capacity)
        # v1 w1
        # v2 w2
        # ...
        # vn wn
        # f = open(filename)
#        with open(filename) as f:
#           self.W = int(f.readline())
#            self.N = int(f.readline())
#            self.items.append([0,0])
#            for i in range(self.N):
#                self.items.append(f.readline().split())
#        self.table = [[0 for x in range(self.W + 1)] for y in range(self.N + 1)]

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
        current_weight = self.W
        for i in range(self.N, 0, -1):
            if current_weight == 0:
                return
#            print("Weights: ",self.weights)
#            print("Values:", self.values)
            check = self.table[i - 1][self.W - int(self.weights[i])]   #0 = value, 1 = weight
            if check + int(self.values[i]) == opt:
                print("Take item with value ", self.values[i], " and weight ", self.weights[i])
                self.W -= int(self.weights[i])
                opt = self.table[i][self.W]

if __name__ == "__main__":
    k = Knapsack()
#    k.read_input(sys.argv[1])
    input = {}
    input = read_json(sys.argv[1])
    k.W = int(input[0].get("capacity"))
    k.N = int(len(input[1]))
    dictionary = dict_to_pref_list(input[1])
    k.weights = dictionary[1]
    k.weights.insert(0, 0)
    k.values = dictionary[0]
    k.values.insert(0, 0)
    t0 = time.process_time()
    k.make_table()
    t1 = time.process_time()
    k.backtrack()
    t2 = time.process_time()
    print("Time to build table: ", t1 - t0)
    print("Time to backtrack: ", t2 - t1)

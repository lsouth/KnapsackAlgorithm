import sys
import numpy as np
import time

class Knapsack:
    W = 0
    N = 0
    items = []
    table = [[]]

    def __str__(self):
        return np.matrix(self.table)

    def read_input(self, filename):
        #expected input:
        # W (total capacity)
        # v1 w1
        # v2 w2
        # ...
        # vn wn
        # f = open(filename)
        with open(filename) as f:
            self.W = int(f.readline())
            self.N = int(f.readline())
            self.items.append([0,0])
            for i in range(self.N):
                self.items.append(f.readline().split())
        self.table = [[0 for x in range(self.W + 1)] for y in range(self.N + 1)]

    def make_table(self):
    #    print(np.matrix(self.items))
        for i in range(0,self.W):
            self.table[0][i] = 0
        for i in range(1,self.N + 1):
            for w in range(self.W + 1):
                weight_i = int(self.items[i][1])
                value_i = int(self.items[i][0])
            #    print("weight_i = ", weight_i, ", w = ", w)
                if weight_i > w:
                    self.table[i][w] = self.table[i - 1][w]
                else:
                    self.table[i][w] = max(self.table[i-1][w], value_i + self.table[i-1][w-weight_i])
        #    print(np.matrix(self.table))
        return self.table[self.N - 1][self.W - 1]

    def backtrack(self):
        opt = self.table[self.N][self.W]
        current_weight = self.W
        for i in range(self.N, 0, -1):
            if current_weight == 0:
                return
            check = self.table[i - 1][self.W - int(self.items[i][1])]
        #    print("Checking table value at n = ", i - 1, "w = ", self.W - int(self.items[i][1]), " : ", check)
            if check + int(self.items[i][0]) != opt:
                print("Do not take item ", i)
            else:
                self.W -= int(self.items[i][1])
                opt = self.table[i][self.W]
                print("Take item ", i)

        #    if self.table[i][current_weight] == opt:
        #        print("Do not take item ", i)
        #    else:
        #        weight_i = int(self.items[i][1])
        #        current_weight -= weight_i

if __name__ == "__main__":
    k = Knapsack()
    k.read_input(sys.argv[1])
    t0 = time.time()
    k.make_table()
    t1 = time.time()
    k.backtrack()
    t2 = time.time()
    print("Time to build table: ", t1 - t0)
    print("Time to backtrack: ", t2 - 1)

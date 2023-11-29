#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplotting import Axes
class SOSModel:
    def __init__(self, n=100):
        self.n = n
        self.lattice = np.random.randint(0, 2, size=(n, n)) - 1
        self.D = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                D_i_j = (np.abs(self.lattice[i, j] + 1) - 4) / 8
                self.D[i, j] = D_i_j
        self.S = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                S_i_j = (np.abs(self.lattice[i, j]) - 2) / 4
                self.S[i, j] = S_i_j

    def update(self):
        for i in range(n):
            for j in range(n):
                if (self.D[i, j] > 1 and self.lattice[i, j] == 0) or \
                   (self.D[i, j] < -1 and self.lattice[i, j] == 1):
                    self.lattice[i, j] = 1 - (np.random.rand() > 0.5) # flip the lattice with 50% probability
        return self

if __name__ == "__main__":
    model = SOSModel(n=500)
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 4, 1)
    ax.imshow(model.S, cmap="coolwarm", extent=[0, model.n, 0, model.n])
    ax.axis("off")
    ax.set_title("Solid on solid model")
    fig.subplots_adjust(bottom=0.2)
    plt.show()

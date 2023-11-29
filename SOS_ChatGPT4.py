#!/usr/bin/env python3
# Created at Wed 29 Nov 2023 02:55:50 PM CST

import numpy as np
import matplotlib.pyplot as plt
import random


def initialize_lattice(size):
    """ Initialize the lattice with zeros. """
    return np.zeros((size, size), dtype=int)


def update_lattice(lattice):
    """ Update the lattice based on SOS model rules. """
    size = lattice.shape[0]
    x, y = random.randint(0, size - 1), random.randint(0, size - 1)

    # Simple rule: Increase or decrease the height randomly
    if random.random() < 0.5:
        lattice[x, y] += 1
    else:
        lattice[x, y] -= 1

    # Ensure the height stays non-negative
    lattice[x, y] = max(0, lattice[x, y])


def simulate_sos_model(size, steps):
    """ Simulate the SOS model for a given number of steps. """
    lattice = initialize_lattice(size)

    for _ in range(steps):
        update_lattice(lattice)

    return lattice


def visualize_lattice(lattice):
    """ Visualize the lattice using a heatmap. """
    plt.imshow(lattice, cmap='viridis')
    plt.colorbar()
    plt.title("Solid-on-Solid Model Simulation")
    plt.show()


# Parameters
lattice_size = 500
simulation_steps = 100000  # Number of steps in the simulation

# Simulate
lattice = simulate_sos_model(lattice_size, simulation_steps)

# Visualize
visualize_lattice(lattice)

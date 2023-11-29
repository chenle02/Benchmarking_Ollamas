#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Define the size of the lattice
L = 500

# Initialize the lattice with random occupancy
occupancy = np.random.randint(0, 2, size=(L, L))

# Set the temperature and other parameters
T = 1.0
alpha = 0.5
beta = 0.5

# Define a function to calculate the energy of a configuration
def energy(occupancy):
  energy = -T * np.sum(occupancy[1:, :] * np.log(occupancy[1:, :])) - T * np.sum(occupancy[:-1, :] * np.log(occupancy[:-1, :]))
  return energy

# Perform a simulation of the SOS model
num_steps = 100000
for i in range(num_steps):
  # Propose a new configuration
  proposed_config = np.copy(occupancy)
  for i in range(L):
    for j in range(L):
      if np.random.rand() < alpha:
        proposed_config[i, j] = 1 - occupancy[i, j]
      elif np.random.rand() < beta:
        proposed_config[i, j] = occupancy[i, j]

  # Calculate the energy of the proposed configuration
  proposed_energy = energy(proposed_config)

  # Accept or reject the proposed configuration based on the Metropolis criterion
  if np.random.rand() < np.exp(-(proposed_energy - occupancy[i, j]) / T):
    occupancy = proposed_config

# Plot the final state of the lattice
plt.figure(figsize=(10, 10))
plt.imshow(occupancy, cmap='gray')
plt.title('Solid-on-Solid Model')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

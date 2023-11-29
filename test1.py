#!/usr/bin/env python3
#
#
import numpy as np

# Set up the lattice of size 500
lattice_size = 500
lattice = np.zeros((lattice_size, lattice_size))

# Define the solid particles and their initial positions
solid_particles = 100
solid_positions = np.random.randint(low=0, high=lattice_size, size=(solid_particles, 2))

# Define the simulation parameters
num_iterations = 10000
time_step = 0.1

# Perform the simulation
for i in range(num_iterations):
    # Move solid particles according to their velocities
    for j, particle in enumerate(solid_particles):
        if lattice[solid_positions[j, 0]][solid_positions[j, 1]] == 0:
            velocity = np.random.uniform(-1, 1, size=(2)) * time_step
            solid_positions[j, :] += velocity

    # Update the lattice by checking for collisions between solid particles and stationary particles
    for j in range(num_iterations):
        if lattice[solid_positions[j, 0]][solid_positions[j, 1]] == 1:
            distance = np.sqrt((solid_positions[j, 0] - solid_positions[j+1, 0])**2 + (solid_positions[j, 1] - solid_positions[j+1, 1])**2)
            if distance < 2:
                lattice[solid_positions[j, 0]][solid_positions[j, 1]] = 0
                lattice[solid_positions[j+1, 0]][solid_positions[j+1, 1]] = 1
                solid_particles -= 1

    # Print the current state of the lattice after each iteration
    if i % 100 == 0:
        print("Iteration", i)
        print(lattice)


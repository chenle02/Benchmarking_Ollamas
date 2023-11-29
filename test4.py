#!/usr/bin/env python3
#
#
import numpy as np

# Set the size of the lattice
L = 500

# Initialize the simulation parameters
num_particles = 1000
max_steps = 10000

# Initialize the lattice
lattice = np.zeros((L, L))

# Initialize the particles
particles = np.random.rand(num_particles, 3) * L / 2

# Set the boundaries of the lattice
lattice[0, :] = 1
lattice[-1, :] = -1
lattice[:, 0] = -1
lattice[:, -1] = 1

# Define the SOS model parameters
sigma = 1.0
alpha = 0.5
beta = 0.2

# Initialize the simulation
t = 0
step_count = 0

while step_count < max_steps:
    # Update the position of each particle
    for i in range(num_particles):
        particle = particles[i]
        x = particle[:, 0] + np.random.randn() * sigma
        y = particle[:, 1] + np.random.randn() * sigma
        z = particle[:, 2] + np.random.randn() * sigma
        particles[i] = np.array([x, y, z])

    # Calculate the interactions between particles
    for i in range(num_particles):
        particle = particles[i]
        for j in range(i+1, num_particles):
            other_particle = particles[j]
            distance = np.linalg.norm(particle - other_particle)
            if distance < alpha * L:
                # Calculate the interaction energy
                energy = beta * (1 + distance / L)
                # Update the particle positions
                particles[i] += energy * (other_particle - particle) / np.linalg.norm(other_particle - particle)

    # Increment the time step counter
    step_count += 1
    t += 1

# Plot the final position of the particles
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 8))
plt.scatter(particles[:, 0], particles[:, 1], particles[:, 2], c='r')
plt.xlabel('X')
plt.ylabel('Y')
plt.zlabel('Z')
plt.show()


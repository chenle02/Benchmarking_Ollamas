#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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


def create_sos_movie(size, steps, interval=50, output='sos_model_simulation.mp4'):
    """ Create a movie of the SOS model simulation. """
    lattice = initialize_lattice(size)
    fig, ax = plt.subplots()
    img = ax.imshow(lattice, cmap='viridis', animated=True)

    def update_fig(*args):
        update_lattice(lattice)
        img.set_array(lattice)
        return img,

    ani = animation.FuncAnimation(fig, update_fig, frames=steps, interval=interval, blit=True)
    ani.save(output, writer='ffmpeg')
    plt.close(fig)

    return output


# Parameters for movie creation
lattice_size = 500
simulation_steps = 500  # Reduced number of steps for demonstration

# Create the movie
movie_file = create_sos_movie(lattice_size, simulation_steps, output='sos_model_simulation.mp4')

movie_file

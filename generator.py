# Imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import random

# Defines the points of the outside boundary for the triangle
triangle_points = np.array([[1, 1], [2, 2.5], [3, 1]])
tri_path = Path(triangle_points)

# Creates graph
plt.figure()

# Picks a random starting point that is within the defined triangle area
def pick_rand_point():
    while True:
        # Pick random point within a square
        rand_point = (random.uniform(1, 3), random.uniform(1, 2.5))
        # If it is also within the triangle boundaries, keep it
        if tri_path.contains_point(rand_point):
            break
    return rand_point

# The algorithm for generating a Sierpinski's triangle.
# Check README for how it works
def create_serpinski():
    x1, y1 = pick_rand_point()
    for i in range(3000):
        rand_corner = random.choice(triangle_points)
        x2, y2 = rand_corner
        midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
        plt.scatter(midpoint[0], midpoint[1], s=5, color="red")

        x1, y1 = midpoint

# Generates the triangle and shows the final graph
# The algorithm may take a while depending on how many points you have and how good your computer is
create_serpinski()
plt.show()
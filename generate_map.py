# File to generate a map where titeenijabas try to capture the flag

from opensimplex import OpenSimplex
import numpy as np
import matplotlib.pyplot as plt
import math
import random

height = 99
width = 99
gen = OpenSimplex()
def noise(nx, ny):
    # Rescale from -1.0:+1.0 to 0.0:1.0
    return gen.noise2d(nx, ny) / 2.0 + 0.5

value = []
for y in range(height):
    value.append([0] * width)
    for x in range(width):
        nx = x/width - 0.5
        ny = y/height - 0.5
        value[y][x] = noise(7.00 * nx, 7.00 * ny) \
            + 0.5 * noise(10.00 * nx, 10.00 * ny) \
            # + 0.25 * noise(15.00 * nx, 15.00 * ny) 
        #value[y][x] = math.pow(e, 0.38)

# F is flag
# B is base 
# rest of them do not matter
def get_terrain(height):
    if height == -3:
        return 'F'
    elif height == -2:
        return 'B'
    elif height >= .80:
        return '#'
    elif height >= .60:
        return '-'
    elif height >= .40:
        return '@'
    else:
        return 'Y'

def fill_flag(x, y, dim, arr):
    rng = range( round(-dim/2), round(dim/2) + 1) 
    print(rng)
    for i in rng:
        for j in rng:
            arr[x + i][y + j] = -2
    

def euclidean(x1, y1, x2, y2):
    return math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)

def generate_bases():
    random.seed()
    x1 = random.randint(0,99)
    x2 = random.randint(0,99)
    y1 = random.randint(0,99)
    y2 = random.randint(0,99)

    while euclidean(x1, y1, x2, y2) < 90:
        x1 = random.randint(5,93)
        x2 = random.randint(5,93)
        y1 = random.randint(5,93)
        y2 = random.randint(5,93)
    
    fill_flag(x1, y1, 5, value)
    fill_flag(x2, y2, 5, value)
    value[x1][y1] = -3
    value[x2][y2] = -3

generate_bases()

with open("map.txt", "w") as f:
    for i in value:
        for j in i:
            f.write(get_terrain(j))
        f.write('\n')


a = np.array(value)
plt.imshow(value, cmap='gray')
plt.show()
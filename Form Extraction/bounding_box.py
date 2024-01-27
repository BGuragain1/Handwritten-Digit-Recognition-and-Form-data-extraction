# -*- coding: utf-8 -*-
"""bounding_box.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rt_4wcGdzXQLtghuFhbok-W-hDxIrmBM
"""

coordinates = [
    [313, 2805], [312, 2806], [310, 2806], [309, 2807], [309, 2808],
    [308, 2809], [308, 2952], [307, 2953], [307, 3107], [306, 3108],
    [306, 3184], [307, 3185], [307, 3187], [308, 3187], [309, 3188],
    [326, 3188], [327, 3189], [403, 3189], [404, 3190], [492, 3190],
    [493, 3191], [609, 3191], [610, 3192], [653, 3192], [654, 3191],
    [656, 3191], [656, 3189], [657, 3188], [657, 3102], [658, 3101],
    [658, 2944], [659, 2943], [659, 2813], [658, 2812], [658, 2810],
    [656, 2810], [655, 2809], [626, 2809], [625, 2808], [524, 2808],
    [523, 2807], [418, 2807], [417, 2806], [321, 2806], [320, 2805]
]

# Separate x and y coordinates
x = [point[0] for point in coordinates]
y = [point[1] for point in coordinates]

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='', markersize=3)
plt.title('Plot of Coordinates')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

# Define the range of x and y
x_range = range(306, 660)
y_range = range(2805, 3194)

# Generate coordinates within the specified range
coordinates = [(x, y) for x in x_range for y in y_range]

# Separate x and y coordinates
x = [point[0] for point in coordinates]
y = [point[1] for point in coordinates]

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='', markersize=3)
plt.title('Plot of Coordinates')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()


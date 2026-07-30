import numpy as np

from geometry import order_points, compute_destination_size

points = np.array(
    [
        [350, 120],
        [120, 80],
        [90, 420],
        [380, 450],
    ],
    dtype= np.float32,
)


ordered_points = order_points(points= points)
print(ordered_points)

width, height = compute_destination_size(ordered_points)
print(width, height)


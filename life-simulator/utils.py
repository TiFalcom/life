import random

def get_area_points(x, y, width, height):
    area_points = []
    for i in range(x, x + width + 1):
        for j in range(y, y + height + 1):
            area_points.append((i, j))
    return area_points

# TODO: refactor to analyse borders not entire area
def random_pair(excluded_points, x_range, y_range, width, height):
    excluded_set = set(excluded_points)
    while True:
        x = random.randint(*x_range)
        y = random.randint(*y_range)
        area_points = set(get_area_points(x, y, width, height))
        if len(area_points - excluded_set) == len(area_points):
            return x, y
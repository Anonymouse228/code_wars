# https://www.codewars.com/kata/5376b901424ed4f8c20002b7

from math import sqrt
from itertools import combinations


def distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def naive_closest_pair(points):
    pairs_with_distances = ((distance(a, b), (a, b)) for a, b in combinations(points, 2))
    return min(pairs_with_distances)[1]


def closest_pair(points):
    if len(points) <= 7:
        return naive_closest_pair(points)

    points = sorted(points)
    left_half, right_half = points[:len(points) // 2], points[len(points) // 2:]
    left_pair, right_pair = closest_pair(left_half), closest_pair(right_half)

    min_distance, min_pair = min((distance(*left_pair), left_pair), (distance(*right_pair), right_pair))
    for left_point in left_half[::-1]:
        if right_half[0][0] - left_point[0] > min_distance:
            break

        for right_point in right_half[:7]:
            if right_point[0] - left_point[0] > min_distance:
                break

            if abs(right_point[1] - left_point[1]) <= min_distance:
                min_distance, min_pair = distance(left_point, right_point), (left_point, right_point)

    return min_pair


if __name__ == '__main__':
    points = (
        (2, 2),
        (2, 8),
        (5, 5),
        (6, 3),
        (6, 7),
        (7, 4),
        (7, 9),
    )
    print(naive_closest_pair(points))
    print(closest_pair(points))

import sys
from collections import defaultdict
import math

def gcd(a, b):
    """Compute gcd of two integers"""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def normalize(dx, dy):
    """Normalize vector to simplest integer form"""
    if dx == 0 and dy == 0:
        return (0, 0)
    g = gcd(dx, dy)
    dx //= g
    dy //= g
    if dx < 0 or (dx == 0 and dy < 0):
        dx, dy = -dx, -dy
    return (dx, dy)


def count_right_triangles(points):
    """Count number of right triangles formed by given points"""
    n = len(points)
    ans = 0
    for i in range(n):
        vec_count = defaultdict(int)
        x0, y0 = points[i]

        #Count all vectors from point i to other points
        for j in range(n):
            if j == i:
                continue
            dx = points[j][0] - x0
            dy = points[j][1] - y0
            vec = normalize(dx, dy)
            vec_count[vec] += 1

        #For each direction vector, check perpendicular vectors
        for (dx, dy), cnt in vec_count.items():
            if (dx, dy) == (0, 0):
                continue
            perp = normalize(-dy, dx)  #Perpendicular vector
            if perp in vec_count:
                ans += cnt * vec_count[perp]

    #Each right triangle is counted twice (once for each perpendicular direction)
    return ans // 2


def main():
    files = ['righttangles_1.txt', 'rightangles_2.txt', 'rightangles_3.txt']
    for file in files:
        try:
            with open(file, 'r') as f:
                n = int(f.readline().strip())
                points = []
                for _ in range(n):
                    x, y = map(int, f.readline().strip().split())
                    points.append((x, y))
            result = count_right_triangles(points)
            print(f"{file}: The number of right triangles is: {result}")
        except FileNotFoundError:
            print(f"{file}: File not found")


if __name__ == "__main__":
    main()
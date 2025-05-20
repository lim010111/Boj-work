from sys import stdin

input = stdin.readline


def press_points(n, points):
    sorted_points = {point: index for index, point in enumerate(sorted(set(points)))}

    pressed_points = [sorted_points[point] for point in points]
    
    return pressed_points

n = int(input())
points = list(map(int, input().split()))

print(*press_points(n, points))
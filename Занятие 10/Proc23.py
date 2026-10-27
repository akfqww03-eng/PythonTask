def quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4

points = [
    (5, 3),
    (-2, 8),
    (-4, -6)
]
for i, (x, y) in enumerate(points, 1):
    q = quarter(x, y)
    print(q)

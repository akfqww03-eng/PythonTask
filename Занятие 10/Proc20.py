import math
def triangle_p(a, h):
    b = math.sqrt((a / 2) ** 2 + h ** 2)
    return a + 2 * b

for i in range(1, 4):
    print(i)
    a = float(input())
    h = float(input())
    perimeter = triangle_p(a, h)
    print(perimeter)


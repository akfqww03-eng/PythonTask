def sum_range(a, b):
    if a > b:
        return 0
    return sum(range(a, b + 1))

A = int(input())
B = int(input())
C = int(input())

sum_AB = sum_range(A, B)
sum_BC = sum_range(B, C)

print(sum_AB)
print(sum_BC)

def shift_left3(a, b, c):
    return b, c, a

set1 = (10, 20, 30)
result1 = shift_left3(*set1)

set2 = (5, 6, 7)
result2 = shift_left3(*set2)

print(result1)
print(result2)

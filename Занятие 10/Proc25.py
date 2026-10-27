
def is_square(k):
    if k <= 0:
        return False
    root = int(k**0.5)
    return root * root == k

numbers = [4, 7, 9, 15, 16, 23, 25, 30, 36, 42]
counts = 0
for num in numbers:
    if is_square(num):
        counts += 1

print(counts)

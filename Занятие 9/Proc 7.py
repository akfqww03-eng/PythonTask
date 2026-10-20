def invert_digits(k):
    return int(str(k)[::-1])
numbers = [12345, 607, 981, 4432, 100]
for num in numbers:
    reversed = invert_digits(num)
print(reversed)
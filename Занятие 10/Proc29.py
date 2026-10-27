def digit_count(k):
    return len(str(k))
numbers = [7, 42, 105, 8888, 123456]
for num in numbers:
    count = digit_count(num)
    print(count)

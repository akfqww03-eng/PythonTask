def even(k):
    if k%2 == 0:
        return True
    numbers = [12, 5, 8, 23, 42, 7, 14, 91, 0, 3]
    counte = 0
    for k in numbers:
        if even(k):
            counte += 1
    print(counte)

def add_left_digit(d, k):
    return int(f"{d}{k}")
K = 456
D1 = 7
D2 = 9

print(K)
K = add_left_digit(D1, K)
print(D1,K)
K = add_left_digit(D2, K)
print(D2,K)

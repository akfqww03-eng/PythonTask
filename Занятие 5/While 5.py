N = int(input())
K = int(input())
while N > 1:
    N //= 2
    K += 1
print(K)

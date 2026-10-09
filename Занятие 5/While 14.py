A = float(input())
K = 1
summ= 1.0
while summ + 1 / (K + 1) < A:
    K += 1
    summ += 1 / K
print(K)
print( summ)

A = float(input())
K = 0
summ = 0.0
while summ <= A:
    K += 1
    summ+= 1 / K
print(K)
print(summ)

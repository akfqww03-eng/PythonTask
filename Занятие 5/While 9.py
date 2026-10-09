N = int(input())
K = 0
curr = 1  
while curr <= N:
    curr *= 3
    K += 1
print(K)

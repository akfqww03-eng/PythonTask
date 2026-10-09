n = int(input())
while n > 1 and n % 3 == 0:
    n //= 3
print(n == 1)

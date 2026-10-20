def power_a234(a):
    return a**2, a**3, a**4
numbers = [23, 11, 43, 2]
for num in numbers:
    d,c, v = power_a234(num)
    print(num,d,c,v)
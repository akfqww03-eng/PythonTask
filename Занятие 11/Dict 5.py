n= {
    'Hello':1,
    'Dog':2,
    'Cat':3
}
k = 'Cat'
if k in n:
    n.pop(k,0)
    print(len(n))
else:
    print(n)

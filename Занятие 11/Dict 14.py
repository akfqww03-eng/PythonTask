
n = {
    "a": 5,
     "b": 12,
    "c": 8,
    "d": 20,
    "e": 10
}
V = 10
nu = {k: v for k, v in n.items() if v >= V}
print(len(nu))

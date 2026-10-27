N = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
M = {
    'c': 30,
    'd': 40,
    'e': 50,
    'f': 60
}

count = len(N.keys()), len(M.keys())
result = {**M, **N}
print(len(result))
print(len(count))

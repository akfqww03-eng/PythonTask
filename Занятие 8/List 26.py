A = [10, 20, 35, 40, 15, 50, 5]
average = sum(A) / len(A)
result = [x for x in A if x > average]
print(average)
print(result)
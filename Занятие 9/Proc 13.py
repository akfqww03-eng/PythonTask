def SortDec3(A, B, C):
  if A < B:
    A, B = B, A
  if B < C:
    B, C = C, B
  if A < B:
    A, B = B, A
  return A, B, C
A1, B1, C1 = 5, 2, 8
A2, B2, C2 = 1, 9, 3
A1, B1, C1 = SortDec3(A1, B1, C1)
A2, B2, C2 = SortDec3(A2, B2, C2)

print(A1, B1, C1)
print(A2, B2, C2)

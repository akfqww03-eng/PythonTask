try:
    num1 = float(input())
    num2 = float(input())
    result = num1 / num2
except (ZeroDivisionError, ValueError):
    print("Посчитать не удалось")
else:
    print(result)

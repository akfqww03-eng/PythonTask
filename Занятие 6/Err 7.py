while True:
    try:
        user_input = input()
        number = int(user_input)
        break
    except ValueError:
        print("Это не число")
print(number)

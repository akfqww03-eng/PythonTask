try:
    text = input()
    index = int(input())
    print(text[index])
except IndexError:
    print("Нет такого символа")

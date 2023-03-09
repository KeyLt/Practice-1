text = input("Введите номер билета:")
b = None
c = None
b = int(text[0]) + int(text[1]) + int(text[2])
c = int(text[3]) + int(text[4]) + int(text[5])
if b == c:
    print("билет счастливый")
else:
    print("билет не счастливый")



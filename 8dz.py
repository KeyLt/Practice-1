m = int(input("Введите m: "))
l = int(input("Введите l: "))
k = int(input("Введите k: "))
if k > m * l:
    print('Не корректно')
elif (m/k)%1 == 0:
    print('Корректно')
elif (l/k)%1 == 0:
    print('Корректно')
else:
    print('Не корректно')
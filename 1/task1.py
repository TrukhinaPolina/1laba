
a = input("введите пароль,  ")
b = input("введите подтверждение пароля ")
c = []

for i in a:
    c += i

for i in c:
    if c.count(i) <= 3:
        if a != b:
            print("Пароли не совпадают")
        if len(a) >= 7:
            if a == b:
                print("Пароль принят")
                break
        else:
            print("Пароль должен состоять минимум из 7 символов")
            break
else:
    print("В пароле не должен повторяться один и тот же символ больше 3-ех раз")
a = float(input("Первый день в км: "))
b = float(input("Желаемый результат: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a / 10
    day += 1
print("Желаемый результат будет на =", day, "день")

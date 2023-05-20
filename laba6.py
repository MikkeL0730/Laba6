#Вариант 12. Вывести все натуральные числа до n, в записи которых встречается ровно одна нечетная цифра на четной позиции.
n = int(input("Введите число n (> 10): "))

for k in range(1,n):
    k = str(k)
    kol_nechetnoe = 0
    for i in range(1, len(k), 2):
        if int(k[i]) % 2 == 1:
            kol_nechetnoe += 1
    if kol_nechetnoe == 1:
        print(k)
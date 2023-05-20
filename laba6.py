def sum_odd_digits_at_even_position(num): #сумма чётных, на нечётных
    num_str = str(num)
    sum_odd = 0
    for i in range(1, len(num_str), 2):
        if int(num_str[i]) % 2 != 0:
            sum_odd += int(num_str[i])
    return sum_odd


def sum_even_digits_at_odd_position(num): #сумма нечётных, на чётных
    num_str = str(num)
    sum_even = 0
    for i in range(0, len(num_str), 2):
        if int(num_str[i]) % 2 == 0:
            sum_even += int(num_str[i])
    return sum_even


def print_numbers_with_odd_even_sum(n): #вывод числа, где чётных больше нечётных
    for num in range(1, n + 1):
        odd_sum = sum_odd_digits_at_even_position(num)
        even_sum = sum_even_digits_at_odd_position(num)
        if odd_sum > even_sum:
            print(num)


n = int(input("Введите число n: "))
print_numbers_with_odd_even_sum(n)
def has_one_odd_digit_at_even_position(num): #одна ли нечётная цифры на чётных позициях
    num_str = str(num)
    count_odd = 0
    for i in range(1, len(num_str), 2):
        if int(num_str[i]) % 2 != 0:
            count_odd += 1
    return count_odd == 1

def is_palindrome(num): #является ли число палиндромом
    num_str = str(num)
    return num_str == num_str[::-1]

def print_numbers_with_one_odd_digit_and_palindrome(n):
    for num in range(1, n+1):
        if has_one_odd_digit_at_even_position(num) and is_palindrome(num):
            print(num)

n = int(input("Введите число n: "))
print_numbers_with_one_odd_digit_and_palindrome(n)

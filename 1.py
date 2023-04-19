def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("Введите число от 0 до 1000: "))
if is_prime(num):
    print("{} является простым.".format(num))
else:
    print("{} не является простым.".format(num))

# 31). Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# 70 = 2*5*7 => [2, 5, 7]
# 140 = 2*2*5*7 => [2, 2, 5, 7]


from math import sqrt


# Вариант 1

def prime_factors_1(n):
    prime_f = []
    divider = 2
    while divider**2 <= n:
        while n % divider != 0:
            divider += 1
        prime_f.append(divider)
        n //= divider
    if n > 1:
        prime_f.append(n)
    return prime_f


# Вариант 2

def prime_factors_2(n):
    prime_f = []
    for i in range(2, int(sqrt(n)) + 1):
        while n % i == 0:
            prime_f.append(i)
            n //= i
    if n > 1:
        prime_f.append(n)
    return prime_f        


print(prime_factors_1(140))
print(prime_factors_2(140))

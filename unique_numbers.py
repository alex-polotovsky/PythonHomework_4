# 32.	Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.


# Представлены две функции, дающие разный результат,
# в зависимости от толкования понятия "неповторяющийся".


# Вариант 1


def unique_numbers_1(numbers):
    return list(set(numbers))

# Вариант 2


def unique_numbers_2(numbers):
    return [i for i in numbers if numbers.count(i) == 1]


user_numbers = [1, 2, 2, 2, 4, 4, 5]

print(unique_numbers_1(user_numbers))
print(unique_numbers_2(user_numbers))

import math
import random
import string

# Вычисление нижней границы S* по формуле 2.
def calculate_lower_bound(P, V, T):
    S_star = (V * T) / P
    return int(S_star)

# Вычисление минимальной длины пароля L по формуле 3.
def calculate_min_password_length(alphabet, S_star):
    A = len(alphabet)
    L = math.ceil(math.log(S_star, A))
    return L

# Реализация программы-генератора паролей.
def generate_password(length, alphabet):
    return ''.join(random.choice(alphabet) for _ in range(length))

# Заданные значения
P = 10**-5
V = 10
T = 7 * 24 * 60
custom_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Вычисление нижней границы S*
lower_bound = calculate_lower_bound(P, V, T)
print(f"Нижняя граница S*: {lower_bound}")

# Вычисление минимальной длины пароля L
min_password_length = calculate_min_password_length(custom_alphabet, lower_bound)
print(f"Минимальная длина пароля L: {min_password_length}")

# Генерация пароля
generated_password = generate_password(min_password_length, custom_alphabet)
print(f"Сгенерированный пароль: {generated_password}")

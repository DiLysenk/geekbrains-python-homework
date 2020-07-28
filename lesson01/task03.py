"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

user_input = input("Введите число >>> ")

if not user_input.isdigit():
    print("Неверный формат числа")
    exit()

# простой пример через диапазон (time => 3.5428000000115034)
result = 0
for x in range(1, 4):
    result += int(user_input * x)

print(result)

# пример длины через while (time => 3.413199999990901)
user_number = int(user_input)
characters_count = 0
temp_number = user_number

while temp_number:
    temp_number //= 10
    characters_count += 1

first_level_multiplication = (10 ** characters_count) + 1
second_level_multiplication = (10 ** (characters_count * 2)) + first_level_multiplication

result = user_number + (user_number * first_level_multiplication) + (user_number * second_level_multiplication)

print(result)

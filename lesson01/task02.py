"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

user_input = input("Введите время в секундах >>> ")

if not user_input.isdigit():
    print("Неверный формат числа")
    exit()

user_seconds = int(user_input)

hours = user_seconds // 3600
minutes = (user_seconds % 3600) // 60
seconds = (user_seconds % 3600) % 60

# hours, minutes, seconds = user_seconds // 3600, (user_seconds % 3600) // 60, (user_seconds % 3600) % 60

print(f"{hours:>02}:{minutes:>02}:{seconds:>02}")

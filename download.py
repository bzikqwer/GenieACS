# Открываем файл для построчного чтения и подсчета значений
file_path = "checkall.txt"

# Инициализируем переменные для подсчета
total_lines = 0
value_counts = {}

# Читаем файл построчно
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        total_lines += 1
        value = line.split(":")[-1].strip()  # Получаем значение после двоеточия
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1

# Выводим количество строк и встречающиеся значения
print(f"Общее количество строк: {total_lines}")
print(f"Количество строк по значениям: {value_counts}")

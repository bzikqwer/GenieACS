import re

# Открытие файла и чтение содержимого
with open('last2.txt', 'r',encoding='utf-8', errors='ignore') as file:
    file_content = file.readlines()

# Регулярное выражение для поиска значения "_id"
pattern = re.compile(r"'_id':\s*'([^']*)'")

# Извлечение значений "_id" из каждой строки
ids = [match.group(1) for line in file_content if (match := pattern.search(line))]

# Вывод результатов
print(ids)

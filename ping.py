import requests
import json

url = 'http://81.88.145.105:7557/tasks'

response = requests.get(url)
tasks = response.json()  # Преобразование текста в JSON

# Выводим только значения _id
for task in tasks:
    if '_id' in task:
        a = "http://81.88.145.105:7557/tasks/"+task['_id']
        print("http://81.88.145.105:7557/tasks/"+task['_id'])
        response = requests.delete(a)

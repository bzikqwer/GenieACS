import requests
import json

# Константы
SERIAL_NUMBER = "22435J1007312"
GENIEACS_URL = 'http://81.88.145.105:7557'
#'http://81.88.145.105:7557/devices/?query=%7B%22_id%22%3A%202351-XC220%2DG3-22435J1012120%22%7D
def get_device_by_id(device_id):
    url = f"{GENIEACS_URL}/devices/"
    query = {"_deviceId._SerialNumber": SERIAL_NUMBER}
    try:
        # Передаем параметр query в виде строки JSON
        response = requests.get(url, params={"query": json.dumps(query)})
        response.raise_for_status()  # Проверка на ошибки
        device = response.json()  # Парсинг JSON ответа
        return device
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Получение информации об устройстве и вывод в консоль
device_info = get_device_by_id(SERIAL_NUMBER)
if device_info:
    print(device_info[0]["_id"])
else:
    print("No device found or an error occurred.")


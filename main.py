import requests

def get_devices():
    url = "http://81.88.145.105:7557/devices"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        devices = response.json()  # Парсинг JSON ответа
        return devices
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Получение списка устройств и вывод в консоль с нумерацией
devices = get_devices()
if devices:
    with open('last.txt', "a", encoding="utf-8") as fl:
        for index, device in enumerate(devices, start=1):
            print(f"{index}. {device}+ \n",file=fl )



else:
    print("No devices found or an error occurred.")

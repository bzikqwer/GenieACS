import requests
import json
import time
# Константы
SERIAL_NUMBER = "22332E1000676"
GENIEACS_URL = 'http://81.88.145.105:7557'
#'http://81.88.145.105:7557/devices/?query=%7B%22_id%22%3A%202351-XC220%2DG3-22435J1012120%22%7D
def get_device_by_id(device_id):
    url = f"{GENIEACS_URL}/devices/"
    query = {"_deviceId._SerialNumber": device_id}
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
    kod = device_info[0]["_id"]
else:
    print("No device found or an error occurred.")
# kod = '202351-XC220%2DG3-22435J1003168'
kod = kod.replace('%', '%25')
url = f"http://81.88.145.105:7557/devices/{kod}/tasks?connection_request"

# Заголовки для запроса
headers = {
    'Content-Type': 'application/json',
}

# Тело запроса
data = {
    "name": "setParameterValues",
    "parameterValues": [
        ["InternetGatewayDevice.IPPingDiagnostics.Host", "www.gogle.ru", "xsd:string"],
        ["InternetGatewayDevice.IPPingDiagnostics.DiagnosticsState", "Requested", "xsd:string"],
        ["InternetGatewayDevice.IPPingDiagnostics.NumberOfRepetitions", 4, "xsd:unsignedInt"],
        ["InternetGatewayDevice.IPPingDiagnostics.Timeout", 1000, "xsd:unsignedInt"]
    ]
}

# Отправка POST-запроса
response = requests.post(url, headers=headers, data=json.dumps(data))

# Вывод кода ответа и текста ответа от сервера
print("Статус-код:", response.status_code)
print("Ответ сервера:", response.text)
# time.sleep(4)

# URL для отправки POST-запроса
url = f"http://81.88.145.105:7557/devices/{kod}/tasks?timeout=3000&connection_request"

# Заголовки для запроса
headers = {
    'Content-Type': 'application/json',
}

# Тело запроса
data = {
    "name": "refreshObject",
    "objectName": ""
}

# Отправка POST-запроса
response = requests.post(url, headers=headers, data=json.dumps(data))

# Вывод кода ответа и текста ответа от сервера
print("Статус-код:", response.status_code)
print("Ответ сервера:", response.text)
# time.sleep(4)


# URL для отправки GET-запроса
url = f"http://81.88.145.105:7557/devices/?query=%7B%22_id%22%3A%22{kod}%22%7D&projection=InternetGatewayDevice.IPPingDiagnostics"

# Заголовки для запроса (если требуется)
headers = {
    'Content-Type': 'application/json',
}

# Отправка GET-запроса
response = requests.get(url)
print(response.text)
# Проверка кода ответа
if response.status_code == 200:
    # Преобразуем ответ сервера из JSON в объект Python
    data = json.loads(response.text)

    # Извлечение значений DiagnosticsState и SuccessCount
    diagnostics_state = data[0]['InternetGatewayDevice']['IPPingDiagnostics']['DiagnosticsState']['_value']
    success_count = data[0]['InternetGatewayDevice']['IPPingDiagnostics']['SuccessCount']['_value']

    # Вывод извлеченных значений
    print("DiagnosticsState:", diagnostics_state)
    print("SuccessCount:", success_count)
else:
    print("Ошибка при выполнении запроса:", response.status_code)
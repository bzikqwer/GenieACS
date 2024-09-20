import requests
import json

while True:
    sn = 'TPLG5151ED88'
    url_forward = f'http://10.100.0.89:8080/check_ont/check_serial_number?serial={sn}'

    sn2 = requests.get(url_forward)

    # Parse the JSON response
    sn2_json = sn2.json()

    # Extract the value of 'serial_number'
    serial_number = sn2_json.get('serial_number')

    print(serial_number)

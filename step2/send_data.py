import requests

url = 'http://217.29.26.60/med_aparats/parser.php'
data = {
    'base': 'your_base_value',
    'app': 'your_app_value',
    'pacient_id': 1
}

response = requests.post(url, data=data)

if response.status_code == 200:
    print('Request successfully sent')
    print('Response:', response.text, response.encoding)
    print(bytes(response.text, 'iso-8859-1').decode('utf-8'))
else:
    print('Request failed with status code:', response.status_code)
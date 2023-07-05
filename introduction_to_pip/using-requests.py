import requests

url = 'https://google.com'
response = requests.get(url)
print(f'Response returned: {response.status_code}')
print(response.text[:200])

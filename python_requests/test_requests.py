"""
This module is for learning about the requests package
Following Real python article linked below,
https://realpython.com/python-requests/#getting-started-with-requests
"""
import requests
from requests.exceptions import HTTPError

response = requests.get('https://api.github.com', timeout=5,
                        params={'q': 'requests+language:python'},
                        headers={'Accept': 'application/vnd.github.v3.text-match+json'})
print(response.status_code)

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred {http_err}")
    except Exception as err:
        print(f"Other Error occurred {err}")
    else:
        print('Success!')

### OTHER HTTP METHODS
requests.post('https://httpbin.org/post', data={'key':'value'}, timeout=5)
requests.put('https://httpbin.org/put', data={'key':'value'}, timeout=5)
requests.delete('https://httpbin.org/delete', timeout=5)
requests.head('https://httpbin.org/get', timeout=5)
requests.patch('https://httpbin.org/patch', data={'key':'value'}, timeout=5)
requests.options('https://httpbin.org/get', timeout=5)

import json

import requests

headers = {'Authorization' : 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJcdTA0MWZcdTA0MjBcdTA0MThcdTA0MWRcdTA0MjZcdTA0MTBcdTA0MTAiLCJ1c2VyTmFtZSI6Ilx1MDQxZlx1MDQ0MFx1MDQzOFx1MDQzZFx1MDQ0NiBcdTA0MTBcdTA0M2JcdTA0MzVcdTA0M2FcdTA0NDFcdTA0MzVcdTA0MzkgXHUwNDEwXHUwNDNiXHUwNDM1XHUwNDNhXHUwNDQxXHUwNDM1XHUwNDM1XHUwNDMyXHUwNDM4XHUwNDQ3IiwidXNlcklkIjoyMDAwMjkwOCwiYXV0aG9yaXRpZXMiOlt7ImF1dGhvcml0eSI6Ilx1MDQyMVx1MDQyMVx1MDQxZi4gXHUwNDFlXHUwNDMxXHUwNDQ5XHUwNDM4XHUwNDM5IFx1MDQzNFx1MDQzZVx1MDQ0MVx1MDQ0Mlx1MDQ0M1x1MDQzZiJ9XSwiaWF0IjoxNzA4ODg4NTE0LCJleHAiOjE3NDA0MjQ1MTR9.rAsMGGwTtLZgZV5TSu9tixsEsAY8IQwoqXmroWj9oW0jiz5HYqA4dDWZpw_PQiWYWAjjZ8OBm80pTWSKHQn0xg'}
response = requests.get('https://maps-api-dev.dp.pgk.ru/stations', headers=headers, verify=False)
print(json.dumps(response.json(), indent=4, ensure_ascii=False))

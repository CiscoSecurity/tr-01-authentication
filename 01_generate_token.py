import requests

import time

client_id = 'client-asdf12-34as-df12-34as-df1234asdf12'

client_password = 'asdf1234asdf1234asdf1234asdf1234asdf1234asdf1234asdf12'

url = 'https://visibility.amp.cisco.com/iroh/oauth2/token'

headers = {'Content-Type':'application/x-www-form-urlencoded', 'Accept':'application/json'}

payload = {'grant_type':'client_credentials'}

response = requests.post(url, headers=headers, auth=(client_id, client_password), data=payload)

print(response.json())

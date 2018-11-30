import requests
import json

access_token = 'eyJhbGciO....bPito5n5Q' # Truncated example

url = 'https://visibility.amp.cisco.com/iroh/iroh-inspect/inspect'

headers = {'Authorization':'Bearer {}'.format(access_token), 'Content-Type':'application/json', 'Accept':'application/json'}

observable = 'cisco.com'

inspect_payload = {'content':observable}

inspect_payload = json.dumps(inspect_payload)

response = requests.post(url, headers=headers, data=inspect_payload)

print(response.json())
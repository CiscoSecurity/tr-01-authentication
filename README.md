[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/Threat-Response "Gitter chat")

### Threat Response Authentication:

These scripts demonstrate the basics required to authenticate to the Threat Response APIs. 

Threat Response API endpoints require an ```Access Token``` for authentication. The process for authenticating to the the APIs is:

1. Creat an ```API Client``` [in the portal](https://visibility.amp.cisco.com/#/settings/oauth)
2. Use the ```API Client``` credentials to Generate an ```Access Token```
3. Use the ```Access Token``` to authenticate to the API endpoints

The ```/iroh/oauth2/token``` endpoint used to generate the ```Access Token``` uses basic auth using the ```API Client``` credentials.  
The ```Access Token``` is passed to the other endpoints as an HTTP header, eq. ```Authorization: Bearer <Access Token>```  
The ```Access Token``` is valid for a finite amount of time. Once the token expires a new token must be generated. 

### Before using you must update the following (where present):
- client_id
- client_password
- access_token

### Usage:
```
python 01_generate_token.py
```

### Example script output: 
#### 01_generate_token.py
```
python 01_generate_token.py
{'access_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwczpcL1wvc2NoZW1hcy5jaXNjby5jb21cL2lyb2hcL2lkZW50aXR5XC9jbGFpbXNcL3VzZXJcL2VtYWlsIjoidW5rbm93biBtYWlsIiwiaHR0cHM6XC9cL3NjaGVtYXMuY2lzY28uY29tXC9pcm9oXC9pZGVudGl0eVwvY2xhaW1zXC91c2VyXC9zY29wZXMiOlsiaXJvaC1hZG1pbiIsImludGVncmF0aW9uIiwicHJpdmF0ZS1pbnRlbCIsImluc3BlY3QiLCJpcm9oLWF1dGgiLCJjYXNlYm9vayIsImVucmljaCIsIm9hdXRoIiwiZ2xvYmFsLWludGVsIiwiY29sbGVjdCIsInJlc3BvbnNlIiwidWktc2V0dGluZ3MiXSwiZW1haWwiOiJ1bmtub3duIG1haWwiLCJzdWIiOiJtYXVnZXIiLCJpc3MiOiJJUk9IIEF1dGgiLCJodHRwczpcL1wvc2NoZW1hcy5jaXNjby5jb21cL2lyb2hcL2lkZW50aXR5XC9jbGFpbXNcL3Njb3BlcyI6WyJwcml2YXRlLWludGVsIiwiZW5yaWNoOnJlYWQiLCJjYXNlYm9vayIsImluc3BlY3Q6cmVhZCIsInJlc3BvbnNlIiwiZ2xvYmFsLWludGVsOnJlYWQiXSwiZXhwIjoxNTQzNjA5MzMyLCJodHRwczpcL1wvc2NoZW1hcy5jaXNjby5jb21cL2lyb2hcL2lkZW50aXR5XC9jbGFpbXNcL29hdXRoXC91c2VyXC9pZCI6Im1hdWdlciIsImh0dHBzOlwvXC9zY2hlbWFzLmNpc2NvLmNvbVwvaXJvaFwvaWRlbnRpdHlcL2NsYWltc1wvb3JnXC9pZCI6InRocmVhdGdyaWQ6MSIsImh0dHBzOlwvXC9zY2hlbWFzLmNpc2NvLmNvbVwvaXJvaFwvaWRlbnRpdHlcL2NsYWltc1wvb2F1dGhcL2dyYW50IjoiY2xpZW50LWNyZWRzIiwiaHR0cHM6XC9cL3NjaGVtYXMuY2lzY28uY29tXC9pcm9oXC9pZGVudGl0eVwvY2xhaW1zXC9vcmdcL25hbWUiOm51bGwsImp0aSI6IjdjZWJhZDlmLTNhOTUtNGY5MS1iMzc1LTAxOWQwMTk0M2M4MyIsIm5iZiI6MTU0MzYwODY3MiwiaHR0cHM6XC9cL3NjaGVtYXMuY2lzY28uY29tXC9pcm9oXC9pZGVudGl0eVwvY2xhaW1zXC9vYXV0aFwvc2NvcGVzIjpbInByaXZhdGUtaW50ZWwiLCJlbnJpY2g6cmVhZCIsImNhc2Vib29rIiwiaW5zcGVjdDpyZWFkIiwicmVzcG9uc2UiLCJnbG9iYWwtaW50ZWw6cmVhZCJdLCJodHRwczpcL1wvc2NoZW1hcy5jaXNjby5jb21cL2lyb2hcL2lkZW50aXR5XC9jbGFpbXNcL3VzZXJcL2lkIjoibWF1Z2VyIiwiaHR0cHM6XC9cL3NjaGVtYXMuY2lzY28uY29tXC9pcm9oXC9pZGVudGl0eVwvY2xhaW1zXC9vYXV0aFwvY2xpZW50XC9pZCI6ImNsaWVudC1jZTIyNmZiMC0wMGZhLTQ2ZTMtODc5Yy1iODM4MDU3ZDFhNTkiLCJodHRwczpcL1wvc2NoZW1hcy5jaXNjby5jb21cL2lyb2hcL2lkZW50aXR5XC9jbGFpbXNcL3ZlcnNpb24iOiIxIiwiaWF0IjoxNTQzNjA4NzMyLCJodHRwczpcL1wvc2NoZW1hcy5jaXNjby5jb21cL2lyb2hcL2lkZW50aXR5XC9jbGFpbXNcL29hdXRoXC9raW5kIjoiYWNjZXNzLXRva2VuIn0.CVABRYvp-IT-PAzsduyGEtU6Ft_ho7Z1NAJpevgqJjzox0k1ysCaq3p1orKTUSMhC-9Z6iFSeXaGwjiaacn7A-qL8q9sL575hZWuN4b2wRIl11gRslTdMNMy_XOVQyuuLZ_JruSBGjW-5Ja7XKxcuUuR9uqufdeial0FPqAPZ0vDTFuxmQojJQpjhGDezwCdCKsGs-TDk-3LXqQW2QQddP_v1kO4S9LmaBkZCyDe0BLjGoWmi_cGbivIrtNq6zEotZDK6ngqMqOkTxpguMx6CzaBjggK1abpEiaJn-Y8u4jeH_rXkd59zCpuoSQJd3sk3l5QsGnqddKs2bPito5n5Q', 'token_type': 'bearer', 'expires_in': 600, 'scope': 'private-intel enrich:read casebook inspect:read response global-intel:read'}
```

#### 02_use_token.py
```
python 02_use_token.py
[{'value': 'cisco.com', 'type': 'domain'}]
```

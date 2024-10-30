import requests
# Faz uma solicitação à API
response = requests.get('http://ipinfo.io/json')
data = response.json()
print(data)  # Mostra informações de localização

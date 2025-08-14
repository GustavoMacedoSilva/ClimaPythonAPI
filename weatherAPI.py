import requests
# r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric")

# print(r.json())

def buscarClima(cidade, key):
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&units=metric")
    dicionario = r.json()
    temperatura = dicionario["main"]["temp"]
    return temperatura
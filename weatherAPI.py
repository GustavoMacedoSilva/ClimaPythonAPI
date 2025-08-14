import requests
api_key = "4700a5c85e8dffa1e9d6bb4c2911e109"
# r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric")

# print(r.json())

def buscarClima(cidade):
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric")
    dicionario = r.json()
    temperatura = dicionario["main"]["temp"]
    return temperatura
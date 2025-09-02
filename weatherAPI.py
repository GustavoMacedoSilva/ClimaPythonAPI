import requests
# r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric")

# print(r.json())

def buscarClima(cidade, key):
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&units=metric")
    dicionario = r.json()
    # REGRESSÃO: mudança incorreta que converte temperatura para string
    temperatura = str(dicionario["main"]["temp"]) + "°C"
    return temperatura

def buscarHumidade (cidade, key):
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&units=metric")
    dicionario = r.json()
    humidade = dicionario["main"]["humidity"]
    return humidade
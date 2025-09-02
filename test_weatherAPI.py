import pytest
from unittest.mock import patch, Mock
from weatherAPI import buscarClima, buscarHumidade

# Respostas mockadas para casos positivos
mock_response_temp = {
    "main": {"temp": 25, "humidity": 60}
}
mock_response_temp2 = {
    "main": {"temp": 18, "humidity": 80}
}

# Respostas mockadas para casos negativos
mock_response_no_main = {}
mock_response_no_temp = {"main": {"humidity": 60}}
mock_response_no_humidity = {"main": {"temp": 25}}
mock_response_error = {"cod": 404, "message": "city not found"}

# Casos de teste positivos
@patch('weatherAPI.requests.get')
def test_buscarClima_cidade_valida(mock_get):
    mock_get.return_value.json.return_value = mock_response_temp
    assert buscarClima("Sao Paulo", "chave_valida") == 25

@patch('weatherAPI.requests.get')
def test_buscarClima_cidade_valida2(mock_get):
    mock_get.return_value.json.return_value = mock_response_temp2
    assert buscarClima("Rio de Janeiro", "chave_valida") == 18

@patch('weatherAPI.requests.get')
def test_buscarHumidade_cidade_valida(mock_get):
    mock_get.return_value.json.return_value = mock_response_temp
    assert buscarHumidade("Sao Paulo", "chave_valida") == 60

@patch('weatherAPI.requests.get')
def test_buscarHumidade_cidade_valida2(mock_get):
    mock_get.return_value.json.return_value = mock_response_temp2
    assert buscarHumidade("Rio de Janeiro", "chave_valida") == 80

@patch('weatherAPI.requests.get')
def test_buscarClima_temperatura_decimal(mock_get):
    mock_get.return_value.json.return_value = {"main": {"temp": 22.5, "humidity": 55}}
    assert buscarClima("Curitiba", "chave_valida") == 22.5

@patch('weatherAPI.requests.get')
def test_buscarHumidade_decimal(mock_get):
    mock_get.return_value.json.return_value = {"main": {"temp": 22.5, "humidity": 55.5}}
    assert buscarHumidade("Curitiba", "chave_valida") == 55.5

@patch('weatherAPI.requests.get')
def test_buscarClima_temperatura_zero(mock_get):
    mock_get.return_value.json.return_value = {"main": {"temp": 0, "humidity": 10}}
    assert buscarClima("CidadeZero", "chave_valida") == 0

@patch('weatherAPI.requests.get')
def test_buscarHumidade_zero(mock_get):
    mock_get.return_value.json.return_value = {"main": {"temp": 10, "humidity": 0}}
    assert buscarHumidade("CidadeZero", "chave_valida") == 0

@patch('weatherAPI.requests.get')
def test_buscarClima_temperatura_negativa(mock_get):
    mock_get.return_value.json.return_value = {"main": {"temp": -5, "humidity": 30}}
    assert buscarClima("CidadeFria", "chave_valida") == -5

@patch('weatherAPI.requests.get')
def test_buscarHumidade_alta(mock_get):
    mock_get.return_value.json.return_value = {"main": {"temp": 30, "humidity": 100}}
    assert buscarHumidade("CidadeUmida", "chave_valida") == 100

# Casos de teste negativos
@patch('weatherAPI.requests.get')
def test_buscarClima_sem_chave_main(mock_get):
    mock_get.return_value.json.return_value = mock_response_no_main
    with pytest.raises(KeyError):
        buscarClima("Sao Paulo", "chave_valida")

@patch('weatherAPI.requests.get')
def test_buscarClima_sem_chave_temp(mock_get):
    mock_get.return_value.json.return_value = mock_response_no_temp
    with pytest.raises(KeyError):
        buscarClima("Sao Paulo", "chave_valida")

@patch('weatherAPI.requests.get')
def test_buscarHumidade_sem_chave_main(mock_get):
    mock_get.return_value.json.return_value = mock_response_no_main
    with pytest.raises(KeyError):
        buscarHumidade("Sao Paulo", "chave_valida")

@patch('weatherAPI.requests.get')
def test_buscarHumidade_sem_chave_humidity(mock_get):
    mock_get.return_value.json.return_value = mock_response_no_humidity
    with pytest.raises(KeyError):
        buscarHumidade("Sao Paulo", "chave_valida")

@patch('weatherAPI.requests.get')
def test_buscarClima_cidade_invalida(mock_get):
    mock_get.return_value.json.return_value = mock_response_error
    with pytest.raises(KeyError):
        buscarClima("CidadeInvalida", "chave_valida")

@patch('weatherAPI.requests.get')
def test_buscarHumidade_cidade_invalida(mock_get):
    mock_get.return_value.json.return_value = mock_response_error
    with pytest.raises(KeyError):
        buscarHumidade("CidadeInvalida", "chave_valida")

@patch('weatherAPI.requests.get')
def test_buscarClima_chave_invalida(mock_get):
    mock_get.return_value.json.return_value = mock_response_error
    with pytest.raises(KeyError):
        buscarClima("Sao Paulo", "chave_invalida")

@patch('weatherAPI.requests.get')
def test_buscarHumidade_chave_invalida(mock_get):
    mock_get.return_value.json.return_value = mock_response_error
    with pytest.raises(KeyError):
        buscarHumidade("Sao Paulo", "chave_invalida")

@patch('weatherAPI.requests.get')
def test_buscarClima_resposta_vazia(mock_get):
    mock_get.return_value.json.return_value = {}
    with pytest.raises(KeyError):
        buscarClima("", "")

@patch('weatherAPI.requests.get')
def test_buscarHumidade_resposta_vazia(mock_get):
    mock_get.return_value.json.return_value = {}
    with pytest.raises(KeyError):
        buscarHumidade("", "")

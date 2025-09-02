# BuscaClima

Um aplicativo simples em Python que exibe o clima de uma cidade usando a API do [OpenWeatherMap](https://openweathermap.org/api). O projeto utiliza PyQt5 para a interface gráfica e `requests` para consumir a API.  

---

## Funcionalidades
- Consultar o clima de qualquer cidade digitada.
- Interface gráfica simples e intuitiva.
- Imagem de fundo incluída (`clima.png`).
- Executável standalone gerado com PyInstaller (`BuscaClima.exe`).

---

## Instalação

1. Clone o repositório:  
```bash
git clone https://github.com/GustavoMacedoSilva/ClimaPythonAPI.git
cd ClimaPython
```

2. Rodar o build automatizado (Windows):  
- Clique duas vezes no `build.bat` ou rode no terminal:  
```bat
build.bat
```

3. O executável `BuscaClima.exe` será criado na pasta `dist/`.

---

## Testes Unitários

Este projeto inclui uma suíte de testes unitários usando `pytest`. Os testes cobrem tanto casos positivos quanto negativos para as funções `buscarClima` e `buscarHumidade`.

### Executando os testes
```bash
pipenv install pytest  # Instalar pytest (se necessário)
pipenv run pytest test_weatherAPI.py -v  # Executar todos os testes
```

### Cobertura dos testes
- **10 casos positivos**: Testam o comportamento esperado com dados válidos
- **10 casos negativos**: Testam o tratamento de erros (chaves ausentes, respostas inválidas)

### Documentação de falhas
Se algum teste falhar devido a uma regressão, documente aqui:

#### Histórico de Falhas
*Nenhuma falha documentada ainda.*

---

## Dependências
- Python 3.13  
- [Pipenv](https://pipenv.pypa.io/) para gerenciamento de dependências  
- `requests`  
- `PyQt5`  

---

## Build do executável
O script `build.bat` automatiza:
- Instalação das dependências
- Limpeza de builds antigos
- Criação do executável GUI (`--windowed`) incluindo `clima.png`.

## Problema Merge
O problema foi criado no arquivo README mesmo, para solucionar eu dei um ``git pull origin main``, depois no VSCODE apareceu onde estava as mudanças e o que eu queria manter ou remover, resolvi manter a mudança e dei o commit

## Revert para commit anterior
Acabei esquecendo de colocar mensagem no commit anterior mas ele foi o revert para meu README antigo, usando o hash do commit.

---

## Licença
```
Este projeto é open-source e livre para uso educativo e pessoal.
```

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
git clone <URL_DO_REPO>
cd ClimaPython
```

2. Rodar o build automatizado (Windows):  
- Clique duas vezes no `build.bat` ou rode no terminal:  
```bat
build.bat
```

3. O executável `BuscaClima.exe` será criado na pasta `dist/`.

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

---

## Licença
Este projeto é open-source e livre para uso educativo e pessoal.
```
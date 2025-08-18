
# 🌦️ BuscaClima

Aplicativo em **Python** que exibe o clima atual de uma cidade usando a API do **OpenWeatherMap**.  
Interface gráfica com **PyQt5**, consumo de dados com **requests** e build automatizado do executável **Windows** com **PyInstaller**.

<p align="left">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-blue.svg">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.13-3776AB.svg">
  <img alt="GUI" src="https://img.shields.io/badge/GUI-PyQt5-41CD52.svg">
  <img alt="Build" src="https://img.shields.io/badge/Build-PyInstaller-FFDD00.svg">
</p>

---

## 📚 Sumário
- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração da API Key](#-configuração-da-api-key)
- [Executar em Desenvolvimento](#-executar-em-desenvolvimento)
- [Build do Executável](#-build-do-executável)
  - [Windows (com `build.bat`)](#windows-com-buildbat)
  - [Mac/Linux (manual)](#maclinux-manual)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Exemplo de Uso](#-exemplo-de-uso)
- [Screenshots](#-screenshots)
- [Troubleshooting](#-troubleshooting)
- [Roadmap](#-roadmap)
- [Como Contribuir](#-como-contribuir)
- [Licença](#-licença)
- [Agradecimentos](#-agradecimentos)
- [FAQ](#-faq)

---

## 👀 Visão Geral
O **BuscaClima** permite consultar rapidamente a temperatura e a descrição do clima de qualquer cidade.  
Foi pensado para ser simples de usar, fácil de modificar e direto para **estudo** ou **provas de conceito**.

---

## ✨ Funcionalidades
- 🔍 Busca do clima por nome da cidade.
- 🌡️ Exibe temperatura atual e descrição do clima (em **pt-BR**).
- 🖼️ Interface limpa com imagem de fundo (`clima.png`).
- 📦 Geração de executável standalone (`BuscaClima.exe`) via PyInstaller.

---

## ✅ Pré-requisitos
- **Python 3.13**
- **Pipenv** (para gerenciamento de dependências)  
  Instalação:
  ```bash
  pip install pipenv
  ```
- Conta no **OpenWeatherMap** para obter sua **API Key**:
  - Criar conta: https://home.openweathermap.org/users/sign_up

---

## 🛠️ Instalação

1) **Clonar o repositório**
```bash
git clone https://github.com/GustavoMacedoSilva/ClimaPythonAPI.git
cd ClimaPythonAPI
```

2) **Instalar dependências com Pipenv**
```bash
pipenv install
pipenv shell
```

> Dependências principais: `requests`, `PyQt5`, `pyinstaller`.

> Alternativa sem Pipenv (opcional):
> ```bash
> python -m venv .venv
> .venv\Scripts\activate   # Windows
> # ou
> source .venv/bin/activate  # macOS/Linux
> pip install -r requirements.txt
> ```

*(Se quiser usar `requirements.txt`, gere com `pip freeze > requirements.txt` após instalar.)*

---

## 🔐 Configuração da API Key

Você tem **duas opções** para configurar a API Key do OpenWeather:

### Opção A) Editar no código (rápida)
No arquivo `main.py`, substitua:
```python
API_KEY = "SUA_API_KEY_AQUI"
```
pela sua chave real.

### Opção B) Usar variável de ambiente (recomendada)
1) Defina a variável `OPENWEATHER_API_KEY` no seu sistema:
   - **Windows (CMD):**
     ```bat
     setx OPENWEATHER_API_KEY "SUA_CHAVE_AQUI"
     ```
     Feche e reabra o terminal após setar.
   - **PowerShell:**
     ```powershell
     [Environment]::SetEnvironmentVariable("OPENWEATHER_API_KEY","SUA_CHAVE_AQUI","User")
     ```
   - **macOS/Linux (bash/zsh):**
     ```bash
     echo 'export OPENWEATHER_API_KEY="SUA_CHAVE_AQUI"' >> ~/.bashrc
     # ou ~/.zshrc
     source ~/.bashrc
     ```

2) Ajuste o `main.py` para ler do ambiente (já suportado no exemplo do repositório melhorado, se não, adicione):
```python
import os
API_KEY = os.getenv("OPENWEATHER_API_KEY") or "SUA_API_KEY_AQUI"
```

---

## ▶️ Executar em Desenvolvimento
Com o ambiente ativo (`pipenv shell` ou `venv` ativada), rode:
```bash
python main.py
```

---

## 🧱 Build do Executável

### Windows (com `build.bat`)
O script **`build.bat`** automatiza:
- Instalação/checagem de dependências
- Limpeza de `build/` e `dist/`
- Geração do executável GUI com a imagem `clima.png` embutida

**Uso:**
- Clique duas vezes no `build.bat`  
  **ou**
- Pelo terminal:
  ```bat
  build.bat
  ```

**Saída esperada:**
```
dist/BuscaClima.exe
```

> **Dica:** Se estiver usando variável de ambiente para a API Key, o executável a lerá do ambiente do usuário onde for executado.

### macOS/Linux (manual)
No macOS/Linux o build é manual (exemplo):
```bash
pipenv run pyinstaller --onefile --windowed \
  --add-data "clima.png:." \
  main.py -n BuscaClima
```
O binário ficará em `dist/BuscaClima` (sem `.exe`).  
> Observação: o parâmetro de `--add-data` usa `:` no macOS/Linux e `;` no Windows.

---

## 🗂️ Estrutura do Projeto
```
ClimaPythonAPI/
├─ build.bat              # Script de build (Windows)
├─ clima.png              # Imagem de fundo da interface
├─ main.py                # Código principal do app
├─ Pipfile                # Pipenv (deps)
├─ README.md              # Este arquivo
└─ dist/                  # Onde o executável/binário é gerado
```

---

## 🧪 Exemplo de Uso
1. Abra o app.
2. Digite a cidade, ex.: `São Paulo`.
3. Clique em **Buscar Clima**.
4. Veja os resultados:
   - **Local**: Cidade, País
   - **Temperatura**: em °C
   - **Descrição**: em pt-BR (ex.: “Nublado”, “Céu limpo”)

---

## 📸 Screenshots
> Substitua os caminhos pelos seus arquivos reais.

- Tela inicial  
  `docs/screenshots/tela_inicial.png`

- Resultado de busca  
  `docs/screenshots/resultado_busca.png`

---

## 🛟 Troubleshooting

**1) “Cidade não encontrada”**  
- Verifique a grafia da cidade (ex.: “Rio de Janeiro”).
- Tente incluir país (ex.: `Paris,FR`).

**2) “Invalid API key” ou sem resultados**  
- Confirme se a **API Key** está correta e ativa (pode levar alguns minutos após criar).
- Se usar variável de ambiente, feche e reabra o terminal/sessão antes de rodar.

**3) Erro de rede/SSL**  
- Teste sua conexão.  
- Em ambientes corporativos, verifique proxy.  
- Atualize o `certifi`: `pip install -U certifi`.

**4) PyQt5 não abre no Linux (erro “xcb”)**  
- Instale dependências do sistema (Ubuntu/Debian):
  ```bash
  sudo apt-get update
  sudo apt-get install -y libxcb-xinerama0 libxkbcommon-x11-0
  ```

**5) Executável não abre em outra máquina (Windows)**  
- Verifique antivirus/SmartScreen.  
- Falta de runtimes do Windows pode afetar; atualize o sistema.

**6) Imagem não aparece**  
- Garanta que `clima.png` está no mesmo diretório do executável (ou foi embutida via `--add-data` corretamente).
- No macOS/Linux, lembre-se de trocar `;` por `:` no `--add-data`.

---

## 🗺️ Roadmap
- [ ] Exibir **sensação térmica**, **umidade** e **vento**  
- [ ] Suporte a **tema claro/escuro**  
- [ ] Histórico de buscas  
- [ ] Auto-completar cidades  
- [ ] Pipeline de CI para build automático

---

## 🤝 Como Contribuir
1) Faça um **fork** do repositório  
2) Crie uma branch para sua mudança:
```bash
git checkout -b feat/minha-melhoria
```
3) Faça commits claros:
```bash
git commit -m "feat(ui): adiciona botão de atualizar"
```
4) Envie a branch:
```bash
git push origin feat/minha-melhoria
```
5) Abra um **Pull Request** explicando as mudanças e, se possível, com screenshots.

> Dica: siga o padrão de commits *conventional commits* (`feat`, `fix`, `docs`, etc.).

---

## 📄 Licença
Este projeto é open-source e livre para **uso educativo e pessoal**.  
Você pode adaptar para seus estudos e demonstrações.

---

## 🙌 Agradecimentos
- [OpenWeatherMap](https://openweathermap.org/api) pelas APIs de clima.  
- Comunidade Python e PyQt5.

---

## ❓ FAQ

**1) Posso usar outra versão do Python?**  
O projeto foi configurado para **Python 3.13**. Versões 3.10+ costumam funcionar, mas mantenha as dependências alinhadas.

**2) O que preciso alterar para usar Fahrenheit?**  
No `main.py`, troque `units=metric` por `units=imperial` e ajuste os rótulos de °C para °F.

**3) Como mudo o idioma da descrição do clima?**  
Troque `lang=pt_br` por outro idioma suportado pela API (ex.: `en`, `es`).

**4) Posso rodar sem Pipenv?**  
Sim. Use `venv` e `pip install` normalmente (veja a seção de instalação).

---

> **Pronto para rodar!** Se quiser, abra uma issue com dúvidas ou sugestões.
```

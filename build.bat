@echo off
echo Instalando dependências...
pipenv install
pipenv install --dev pyinstaller

echo Limpando builds antigos...
rmdir /s /q build dist
del /q *.spec

echo Gerando executável GUI...
pipenv run pyinstaller --onefile --windowed --name "BuscaClima" --add-data "clima.png;." app.py

echo Build finalizado! O executável está na pasta dist\BuscaClima.exe
pause
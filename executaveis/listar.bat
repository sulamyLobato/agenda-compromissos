@echo off
echo Executando o comando PowerShell...
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:5000/compromissos' -Method GET"
pause

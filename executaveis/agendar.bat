@echo off
set /p titulo=Digite o título do compromisso: 
set /p data=Digite a data (AAAA-MM-DD): 
set /p hora=Digite a hora (HH:MM): 

echo Enviando dados para agendar compromisso...

powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:5000/compromisso' -Method POST -Body '{\"titulo\": \"%titulo%\", \"data\": \"%data%\", \"hora\": \"%hora%\"}' -ContentType 'application/json; charset=utf-8'"

pause

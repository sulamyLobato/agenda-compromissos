
@echo off
set /p titulo=Digite o título do compromisso a ser deletado: 

 

echo Deletando compromisso...

powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:5000/compromisso/%titulo%' -Method DELETE -Body '{\"titulo\": \"%titulo%\"}' -ContentType 'application/json; charset=utf-8'"

pause

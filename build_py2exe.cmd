@echo off
set PYTHON="C:\Python26\python.exe"

dist\dtella.exe --terminate

REM delete old directores
rmdir /s /q build
REM rmdir /s /q dist

%PYTHON% setup.py py2exe

pause

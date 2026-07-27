@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="LAPTOP-SHN6NQ4J" (taskkill /f /pid 30608)
if /i "%LOCALHOST%"=="LAPTOP-SHN6NQ4J" (taskkill /f /pid 27708)
if /i "%LOCALHOST%"=="LAPTOP-SHN6NQ4J" (taskkill /f /pid 17424)
if /i "%LOCALHOST%"=="LAPTOP-SHN6NQ4J" (taskkill /f /pid 28784)

del /F cleanup-ansys-LAPTOP-SHN6NQ4J-28784.bat

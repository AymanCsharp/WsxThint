@echo off
chcp 65001 >nul
title WsxThint Tool - Open Source Intelligence Tool
color 0A

echo.
echo ╔══════════════════════════════════════════════════════════════════════════════╗
echo ║                    WsxThint < Osint Tool >                                   ║
echo ║                    For Security Programmers and Ethical Hackers              ║
echo ╚══════════════════════════════════════════════════════════════════════════════╝
echo.

echo Checking requirements...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed! Please install Python 3.7+
    echo Download link: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python is installed
echo.

echo Installing requirements...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Warning: Some requirements failed to install
    echo The tool might work with limited functionality
    echo.
)

echo.
echo Starting the tool...
echo.
python osint_tool.py

echo.
echo Thank you for using OSINT Tool!
pause

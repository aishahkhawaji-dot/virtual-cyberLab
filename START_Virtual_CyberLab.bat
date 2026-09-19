@echo off
cd /d "%~dp0"
echo ========================================
echo      Virtual CyberLab - Starting
 echo ========================================
echo.
echo Installing required packages...
py -m pip install -r requirements.txt
if errorlevel 1 (
  echo.
  echo Installation failed. Check that Python is installed.
  pause
  exit /b 1
)
echo.
echo Launching Virtual CyberLab...
py -m streamlit run app.py
pause

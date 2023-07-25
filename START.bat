@echo off
color 01
mode con:cols=100 lines=20
@echo Your GPT4Docs is being fired .......!!!!!!
@echo If it asks for upgrade or downloads certain files for the first run don't panic.
@echo It runs fully offline,no data leakge, 1000% guaranty ...

xcopy %~dp0Offline_Files\.cache C:\Users\%username%\.cache /E /H /C /I /D /Y
xcopy %~dp0Offline_Files\.streamlit C:\Users\%username%\.streamlit /E /H /C /I /D /Y

streamlit run %~dp0main.py --server.port 10101

pause
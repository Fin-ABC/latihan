@echo off
:menu
echo == Menu ==
echo 1. Lihat List File
echo 2. Lihat IP
echo 3. Ping Github
echo 4. Keluar
set /p pilih=Pilih menu :

if %pilih%==1 goto list
if %pilih%==2 goto ip
if %pilih%==3 goto ping
if %pilih%==4 exit

goto menu

:ip
ipconfig
pause
goto menu

:list
dir
pause
goto menu

:ping
ping github.com
pause
goto menu

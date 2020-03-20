@echo off
:start
set /p dir=Enter the save path: 
set dir=%dir:/=\%
pushd %dir%
if /i not %dir%==%cd% goto :start
echo Save path: %cd%
:download
set /p input=Enter the video url: 
set input=%input:&=^^^&%
youtube-dl -F %input%
if errorlevel 1 goto :download
set /p code=Enter the formating number: 
youtube-dl -f %code% %input%
goto :download

@echo off
  
for /d %%a in (*) do (
    pushd "%%~a"
    for %%b in (*.txt) do type "%%~b">>"%%~a.tmp"
    ren "%%~a.tmp" "%%~a.txt"
    popd
)
pause

set CIRCUITPY_FLASH_PATH=F:
set CIRCUITPY_IMAGE_PATH=.\CircuitPyPartialImage
set ROBOCOPY_ARGS=/S /XD .git /COPYALL /XO

call :copy_cp_path lib\TerrainTronics %CIRCUITPY_IMAGE_PATH
call :copy_cp_file code.py


GOTO :eof

:copy_cp_path
robocopy %CIRCUITPY_FLASH_PATH%\%1 %CIRCUITPY_IMAGE_PATH%\%1 %ROBOCOPY_ARGS% 

exit /B


:copy_cp_file
robocopy %CIRCUITPY_FLASH_PATH% %CIRCUITPY_IMAGE_PATH% %1 
exit /B

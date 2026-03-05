@echo off
setlocal

:: Configuración
set IMAGE_NAME=test-rpi
set CONTAINER_NAME=mi-test-rpi

:: Lógica principal
if /i "%~1"=="build" goto build
if /i "%~1"=="run" goto run
if /i "%~1"=="dev" goto dev
if /i "%~1"=="help" goto help
if "%~1"=="" goto all
goto all

:build
echo --- Construyendo imagen %IMAGE_NAME% ---
docker build -t %IMAGE_NAME% .
goto :eof

:run
echo --- Ejecutando %IMAGE_NAME% ---
docker run --rm --name %CONTAINER_NAME% --memory="512m" --cpus="1.0" %IMAGE_NAME%
goto :eof

:dev
echo --- Modo Desarrollo: Montando volumen local ---
docker run --rm -v "%cd%:/app" --name %CONTAINER_NAME% --memory="512m" --cpus="1.0" %IMAGE_NAME%
goto :eof

:help
echo Uso: run.bat [opciones]
echo Opciones:
echo   build    Fuerza la reconstruccion de la imagen Docker
echo   run      Ejecuta el contenedor (usa la imagen actual)
echo   dev      Ejecuta montando el codigo local (ideal para desarrollo)
echo   all      Construye y ejecuta (por defecto)
goto :eof

:all
echo --- Construyendo y Ejecutando ---
docker build -t %IMAGE_NAME% .
if %ERRORLEVEL% EQU 0 (
    docker run --rm --name %CONTAINER_NAME% --memory="512m" --cpus="1.0" %IMAGE_NAME%
)
goto :eof

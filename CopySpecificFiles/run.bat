@echo off

if not exist venv (
    echo Creando ambiente virtual...
    python -m venv venv || (
        echo Error al crear el ambiente virtual.
        pause
        exit /b 1
    )
    echo Instalando dependencias...
    call venv/scripts/activate.bat || (
        echo Error al activar el ambiente virtual.
        pause
        exit /b 1
    )
    pip install -r requirements.txt || (
        echo Error al instalar las dependencias.
        pause
        exit /b 1
    )
)

echo Activando ambiente virtual...
call venv/scripts/activate.bat || (
    echo Error al activar el ambiente virtual.
    pause
    exit /b 1
)
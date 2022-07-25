echo off
echo Creando entorno en carpeta env...
python -m venv env

echo.
echo Activando entorno...
call env/Scripts/activate.bat

echo.
echo Instalando dependencias del proyecto...
pip install -r requirements.txt
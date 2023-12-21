# ONYZE TEST JUNIOR DEVELOPER

Este es el repositorio que incluye varios ejercicios asignados y un script FastAPI.

## Ejecutar Ejercicios 1 y 2 en Python
python exercise_1.py
python exercise_2.py



### Ejecutar ejercicio 3
El script FastAPI está ubicado en el módulo user_api. Asegúrate de tener las dependencias instaladas antes de ejecutarlo.

1. Instala dependencias
pip install -r user_api/requirements.txt
2. Ejecuta script fastAPI
uvicorn user_api.exercise_3:app --reload
3. Accede a la documentación generada automáticamente con Swagger
En las siguientes URLS puedes ver los endpoints creados y testearlos
http://127.0.0.1:8000/docs

o accede a la inderfaz de redocs

http://127.0.0.1:8000/redocs


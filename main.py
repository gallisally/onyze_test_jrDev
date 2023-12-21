import exercise_1,exercise_2,exercise_4,exercise_5
from exercise_1 import run_exercise_1
from exercise_2 import run_exercise_2
from user_api.exercise_3 import start_fastapi_server
from exercise_4 import run_exercise_4
from exercise_5 import run_exercise_5
import subprocess
from user_api import exercise_3
from abc import ABCMeta

def instalar_dependencias():
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

def mostrar_menu():
    menu = '''
***Este es le menú de los ejercicios realizados en el test. Elige uno e ingresa su numero correspondiente para ejecutarlo y comprobar su funcionamiento.  ***
1. Ejercicio 1: programacion orientada a objetos
2. Ejercicio 2: Algoritmia
3. Ejercicio 3: API REST
4. Ejercicio 4: SQL
5. Ejercicio 5: Blockchain
6. Salir
    '''
    print(menu)

def ejecutar_ejercicio(opcion):
    if opcion == 1:
        print("Ejecutando Ejercicio 1...")
        run_exercise_1()

    elif opcion == 2:
        print("Ejecutando Ejercicio 2...")
        run_exercise_2()

    elif opcion == 3:
        print("Ejecutando Ejercicio 3...")
        start_fastapi_server()

    elif opcion==4:
        print("Ejecutando Ejercicio 4...")
        run_exercise_4()

    elif opcion==5:
        print("Ejecutando Ejercicio 4...")
        run_exercise_5()

    elif opcion == 6:
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")
if __name__ == "__main__":
    while True:
        
        
        requirements=input('Antes debes de realizar las instalaciones correspondientes para hacer funcionar todo correctamente.\n Si no quieres realizarlas de forma manual marca "y", em caso contrario marca "n"')
        if requirements== "y":
            instalar_dependencias()
        elif requirements=="n":
            pass

        mostrar_menu()
        opcion_elegida = input("Selecciona una opción (1-6): ")

        if opcion_elegida.isdigit():
            opcion_elegida = int(opcion_elegida)
            if 1 <= opcion_elegida <= 6:
                ejecutar_ejercicio(opcion_elegida)
                if opcion_elegida == 6:
                    break
            else:
                print("Por favor, ingresa un número del 1 al 6.")
        else:
            print("Por favor, ingresa un número válid")

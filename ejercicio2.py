# Buenas prácticas
import os
os.system("cls")
# hoy ciclos y validar menus
alumno = {}
menu = str(input("""1.- Calcular promedio
2.- Ver resultados estadisticas
3.- Salir\n\nIngresa una opcion: """))

if menu =="1":
    while True:
        try: 
            os.system("cls")
            print("*Seccion calcular promedio*\n")
            alumno['nombre'] = str(input("Ingresa tu nombre: "))
            nota1 = float(input("Indica tu nota 1: "))
            nota2 = float(input("Indica tu nota 2: "))
            nota3 = float(input("Indica tu nota 3: "))
            promedio = nota1+nota2+nota3/3
            alumno["promedio"] = promedio
            print(alumno)
            if promedio > 4:
                print(f"Su promedio es {promedio}.")
                print("Aprobado.")
            else:
                print(f"Su promedio es {promedio}.")
                print("Reprobado.")
        except:
            print("Error yu.")
            os.system("pause")
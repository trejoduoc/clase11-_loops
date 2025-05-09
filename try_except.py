import os
os.system("cls")

while True:
   
    try:
        promedio = float(input("Ingrese promedio: "))
        estado = "Aprobado" if promedio >= 4 else "Reprobado"
        print(f"promedio = {promedio}, estado = {estado}\n")
        break
    except:
        print("Error, intente de nuevo")
        

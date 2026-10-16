""" Determinar si un aprendiz aprueba 
o desaprueba Algoritmia, sabiendo que aprobará si su promedio de tres 
calificaciones es mayor o igual a 70; reprueba 
en caso contrario. """
nota1 = float(input("ingrese la primera calificacion: "))
nota2 = float(input("ingrese la segunda calificacion: "))
nota3 = float(input("ingrese la tercera calificacion: "))

promedio = (nota1 + nota2 + nota3)/ 3

print("El promedio es:", promedio)

if promedio >= 70:
    print("el aprendiz aprueba Algoritmia")
else:
    print("el aprendiz desaprueba algoritmia")
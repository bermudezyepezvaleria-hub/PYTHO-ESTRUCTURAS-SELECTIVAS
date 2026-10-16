"""6.  Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente:
si el promedio obtenido por un alumno en el último periodo es mayor o igual que 4.0, 
se le hará un descuento del 30% sobre la pensión; si el promedio obtenido es menor que 4.0 
deberá pagar la pensión completa, la cual incluye el 10% de IVA. Obtener cuanto debe pagar un alumno. """

promedio = float(input("Ingrese el promedio del alumno: "))
pension = float(input("Ingrese el valor de la pension: "))

if promedio >= 4.5:
    descuento = pension * 0.30
    total = pension - descuento
    print("El alumno recibe un descuento del 30%")

elif promedio >= 4.0:
    descuento = pension * 0.15
    total = pension - descuento
    print("El alumno recibe un descuento del 15%")

else:
    descuento = 0
    iva = pension * 0.10
    total = pension + iva
    print("El alumno paga la pension completa mas el IVA")

print("Valor de la pension: $", pension)
print("Valor del descuento: $", descuento)
print("Total a pagar: $", total)

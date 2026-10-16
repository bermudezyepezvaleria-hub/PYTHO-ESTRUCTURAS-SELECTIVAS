"""6.  Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente:
si el promedio obtenido por un alumno en el último periodo es mayor o igual que 4.0, 
se le hará un descuento del 30% sobre la pensión; si el promedio obtenido es menor que 4.0 
deberá pagar la pensión completa, la cual incluye el 10% de IVA. Obtener cuanto debe pagar un alumno. """

promedio = float(input("Ingrese el promedio del alumno: "))
pension = float(input("Ingrese el valor de la pension: "))

if promedio >= 4.0:
    descuento = pension * 0.30
    iva = 0
    total = pension - descuento

else:
    descuento = 0
    iva = pension * 0.10
    total = pension + iva

print("Promedio:", promedio)
print("Valor de la pension: $", pension)
print("Descuento: $", descuento)
print("IVA: $", iva)
print("Total a pagar: $", total)

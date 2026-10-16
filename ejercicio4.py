"""4. En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo
de un color  que se escoge al azar. Si el color de la balota es rojo 
el descuento es del 15% sobre el total de la compra, la balota es verde 
el descuento es del 20%. Si  el color es diferente a los indicados no obtendrá descuento. 
 Imprimir el valor de la compra, el color de la balota, el descuento y el valor a pagar. """

import random

compra = float(input("Ingrese el valor de la compra: "))

color = random.choice(["rojo", "verde", "azul"])

if color == "rojo":
    descuento = compra * 0.15
elif color == "verde":
    descuento = compra * 0.20
else:
    descuento = 0

total = compra - descuento

print("Color de la balota:", color)
print("Valor de la compra: $", compra)
print("Descuento: $", descuento)
print("Valor a pagar: $", total)

""" Calcular el total a pagar por la compra de zapatillas. Si se compran tres  o más zapatillas 
se aplica un descuento del 20% sobre el total de la compra y si son menos de tres zapatillas un descuento
 del 10%. Mostrar en pantalla, el valor de la compra, el valor del descuento 
 y el valor a pagar una vez aplicado el descuento. """

cantidad = int(input("¿Cuantas zapatillas va a comprar? "))
precio = float(input("¿Cuanto cuesta cada zapatilla? "))


#Multiplicamos la cantidad por el precio de cada zapatilla.#
compra = cantidad * precio

# si >= la cantiad es mayor o igual a 3#
if cantidad >= 3:
    #Si se cumple, el descuento es del 20 %.#
    descuento = compra * 0.20

    #Si no se cumple, se aplica el 10 %.#
else:
    descuento = compra * 0.10

#Restamos el descuento al valor original de la compra.#
total_pagar = compra - descuento

print("Valor de la compra: $", compra)
print("Valor del descuento: $", descuento)
print("Total a pagar: $", total_pagar)

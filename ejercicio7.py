"""7. En una llantera se ha establecido una promoción de las llantas marca “Todo Terreno”, 
dicha promoción consiste en lo siguiente: Si se compran menos de cinco llantas el precio es de $300.000 
cada una, de $250.000 si se compran de cinco a 10 y de $200.000 si se compran más de 10. Obtener la 
cantidad de dinero que una persona tiene que pagar por cada una de las llantas que compre. """

cantidad = int(input("Ingrese la cantidad de llantas: "))

if cantidad < 5:
    precio = 300000
elif cantidad <= 10:
    precio = 250000
else:
    precio = 200000

total = cantidad * precio

print("Cantidad de llantas:", cantidad)
print("Precio por llanta: $", precio)
print("Total a pagar: $", total)

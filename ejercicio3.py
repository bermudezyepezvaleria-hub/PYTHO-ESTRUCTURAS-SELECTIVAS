""" Una empresa quiere hacer una compra de varias piezas de la misma clase a una fábrica de bolsos. La empresa, 
dependiendo del monto total de la compra, decidirá qué hacer para pagar al fabricante:  Si el monto
 total de la compra excede de $500 000 la empresa tendrá la capacidad de invertir de su propio
   dinero un 55% del monto de la compra, pedir prestado al banco un 30%
 y el resto lo pagará solicitando un crédito al fabricante.  Si el monto total de la compra
   no excede de $500 000 la empresa tendrá capacidad de invertir de su propio dinero un 70% y el restante 30% 
   lo pagará solicitando crédito al fabricante. El fabricante cobra por concepto de intereses un 20% 
   sobre la cantidad que se le pague a crédito. Imprimir el valor invertido de su propio dinero, el valor prestado al banco,
     y el valor del crédito solicitado al fabricante, según sea el caso. """

compra = float(input("Ingrese el monto total de la compra: "))

if compra > 500000:
    propio = compra * 0.55
    banco = compra * 0.30
    credito = compra * 0.15
    interes = 0

else:
    propio = compra * 0.70
    banco = 0
    credito = compra * 0.30
    interes = credito * 0.20

print("Dinero propio: $", propio)
print("Prestamo del banco: $", banco)
print("Credito del fabricante: $", credito)
print("Interes del credito: $", interes)
print("Total del credito con interes: $", credito + interes)

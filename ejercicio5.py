"""5. Calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico;
la fórmula que se aplica es:  cuando el sexo es femenino : núm. pulsaciones = (220 - edad)/10 
y si el sexo es masculino : núm. pulsaciones = (210 - edad)/10 """

edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (F o M): ").upper()

if sexo == "F":
    pulsaciones = (220 - edad) / 10
elif sexo == "M":
    pulsaciones = (210 - edad) / 10
else:
    pulsaciones = None
    print("Debe ingresar F o M.")

if pulsaciones is not None:
    print("Pulsaciones por cada 10 segundos:", pulsaciones)

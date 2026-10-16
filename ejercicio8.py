"""8. Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos,
 un médico determina si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina en la sangre, 
 de su edad y de su sexo. Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde,
   se determina su resultado como positivo y en caso contrario como negativo. La tabla en la que el médico se basa para
     obtener el resultado es la siguiente: EDAD NIVEL HEMOGLOBINA
       0 - 1 mes               13 - 26 g%
       > 1 y < = 6 meses       10 - 18 g% 
       > 6 y < = 12 meses      11 - 15 g% 
       > 1 y < = 5 años        11.5 - 15 g% 
       > 5 y < = 10 años       12.6 - 15.5 g% 
       > 10 y < = 15 años      13 - 15.5 g% 
       mujeres > 15 años       12 - 16 g% 
       hombres > 15 años       14 - 18 g% """

edad = float(input("Ingrese la edad en años: "))
sexo = input("Ingrese el sexo (F o M): ").upper()
hemoglobina = float(input("Ingrese el nivel de hemoglobina: "))

if edad >= 0 and edad <= 1/12:
    minimo = 13
elif edad <= 0.5 and edad > 1/12:
    minimo = 10
elif edad <= 1 and edad > 0.5:
    minimo = 11
elif edad <= 5 and edad > 1:
    minimo = 11.5
elif edad <= 10 and edad > 5:
    minimo = 12.6
elif edad <= 15 and edad > 10:
    minimo = 13
elif edad > 15 and sexo == "F":
    minimo = 12
elif edad > 15 and sexo == "M":
    minimo = 14
else:
    minimo = None

if minimo is None:
    print("Verifique la edad y el sexo ingresados.")
elif hemoglobina < minimo:
    print("Resultado positivo para anemia")
else:
    print("Resultado negativo para anemia")

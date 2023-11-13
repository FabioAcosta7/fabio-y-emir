contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
animal = input("Hay un animal a registrar? (si/no)")
if animal == "si":
  contador5 += 1
while animal == "si":
  edad = float(input("Ingrese la edad del animal:"))
  if edad < 2:
    contador1 += 1
  elif edad >= 2 and edad < 5:
    contador2 += 1
  elif edad >= 5 and edad < 10:
    contador3 += 1
  elif edad >= 10:
    contador4 += 1
  otro = input("hay otro animal a registrar?")
  if otro == "si":
    contador5 += 1
  if otro == "no":
    break
porcentaje1 = (contador1/contador5)*100
porcentaje2 = (contador2/contador5)*100
porcentaje3 = (contador3/contador5)*100
porcentaje4 = (contador4/contador5)*100

print("se registraron en total", contador5, "animales. Animales con menos de 2 anos de edad hay", contador1, "en porcentaje", porcentaje1, ".Animales entre 2 y 5 anos de edad hay", contador2, "en porcentaje", porcentaje2, ".Animales entre 5 y 10 anos de edad hay", contador3, "en porcentaje", porcentaje3, ".Animales con mas de 10 anos de edad hay", contador4, "en porcentaje", porcentaje4)

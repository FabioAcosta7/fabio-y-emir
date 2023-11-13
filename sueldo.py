vendedor = input("Hay un vendedor? (si/no)")
while vendedor == "si":
  nombre = input("Ingrese el nombre del vendedor:")
  salario = int(input("Ingrese el salario base:"))
  ventas = int(input("Ingrese la cantidad de ventas"))
  if ventas < 3500:
    salario_total = salario*1.07
  elif ventas > 3500 and ventas < 7000:
    salario_total = salario*1.1
  elif ventas > 7000:
    salario_total = salario*1.15
  print("El sueldo del vendedor", nombre, "es de", salario_total, "pesos")
  otro = input("Hay otro vendedor?")
  if otro == "no":
    break

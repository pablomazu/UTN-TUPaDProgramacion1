# 1-Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo")


# 2-Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla. 

nombre_usuario = input("Ingrese su nombre: ")
print(f"Hola, {nombre_usuario}!" )


# 3- Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

# 4- Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perimetro
radio_circulo = float(input("Ingrese el radio de un circulo: "))
area_circulo = 3.14 * (radio_circulo**2)
perimetro_circulo = 2 * 3.14 * radio_circulo
print(f"El area del circulo es {area_circulo} y su perimetro es {perimetro_circulo}")


# 5- Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Ingresa una cantidad de segundos: "))
horas = float((segundos / 60) /60)
print(f"Los {segundos} segundos ingresados equivalen a {round(horas)} horas")


# 6- Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
num = int(input("Ingrese un numero: "))
print (f"1 x {num} = {1*num}")
print(f"2 x {num} = {2*num}")
print(f"3 x {num} = {3*num}")
print(f"4 x {num} = {4*num}")
print(f"5 x {num} = {5*num}")
print(f"6 x {num} = {6*num}")
print(f"7 x {num} = {7*num}")
print(f"8 x {num} = {8*num}")
print(f"9 x {num} = {9*num}")
print(f"10 x {num} = {10*num}")


# 7- Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre 
# por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input("Ingrese un numero entero distinto a 0: "))
num2 = int(input("Ingrese otro numero distinto a 0: "))
suma = num1 + num2
div = num1 / num2
mult = num1 * num2
resta = num1 - num2
print(f"{num1} + {num2} = {suma}, {num1} - {num2} = {resta}, {num1} / {num2} = {int(div)}, {num1} * {num2} = {mult} ")


# 8- Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. 
peso_corporal = float(input("Ingrese su peso corporal: "))
altura = float(input("Ingrese su altura: "))
imc = peso_corporal / (altura * altura)
print(f"Su indice de masa corporal es: {imc}")


# 9- Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
grados_celsius = int(input("Ingrese una temperatura en celsius: "))
fahrenheit = (9.5 * grados_celsius + 32)
print(f"La temperatura en grados Fahrenheit es {fahrenheit}")


# 10- Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))
num3 = float(input("Ingrese otro numero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los numero es: {promedio}")
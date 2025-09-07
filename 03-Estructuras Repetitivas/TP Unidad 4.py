#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

"""cant_numeros = 101

for cont in range(1,cant_numeros):
    print(cont)
"""
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#   dígitos que contiene.
"""
num_entero = int(input("Ingrese un numero entero: "))
cont = 0
num_final = num_entero
while num_entero != 0:
    num_entero = num_entero // 10
    cont += 1

print(f"La cantidad de digitos que tiene {num_final} es {cont}")
"""
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#   dados por el usuario, excluyendo esos dos valores.

""" 
print("Ingrese un numero")
min_num = int(input())          #pido al usuario el numero minimo para empezar

print("Ingrese otro numero mayor al anterior")
max_num = int(input())          #Pido ahora el maximo    

sumatoria = 0                   

for cont in range(min_num+1,max_num):
    sumatoria = sumatoria + cont            #Cont siempre vale el número actual del rango que está recorriendo

print(f"La suma de todos los numero es {sumatoria}")
"""
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#   secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#   un 0.
"""
num = 1
sumatoria = 0

while num != 0:
    print("Ingrese un numero")
    num = int(input())
    sumatoria = sumatoria + num
print(f"Total acumulado: {sumatoria}")
"""

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9.
#   Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
num_aleatorio = 3
cont_intentos = 1

num = int(input("Adivine un numero entre 1 y 9: "))
while num != num_aleatorio:   
    num = int(input("Numero incorrecto, vuelva a ingresar un numero entre 1 y 9: "))
    cont_intentos += 1
print(f"Acertaste! el numero es {num_aleatorio}.Realizaste {cont_intentos} intentos")
"""

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#   entre 0 y 100, en orden decreciente.
"""
for i in range(100,-1, -2):
    print(i)
"""
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#   número entero positivo indicado por el usuario.
"""
num_positivo = int(input("Ingrese un numero positivo: "))
suma_total = 0

for i in range(0, num_positivo): #sin incluir el numero ingresado, sino seria num_positivo +1
    suma_total += i

print(f"La suma de los numeros comprendido entre 0 y {num_positivo} es {suma_total}")
"""
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#   programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#   negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#   menor, pero debe estar preparado para procesar 100 números con un solo cambio).

"""
cant_num = 5
num_positivos = 0
num_negativos = 0
num_pares = 0
num_impares = 0
num_neutro = 0

for i in range(cant_num):
    num_ingresado = int(input(f"Ingrese el numero {i+1}: "))
    if num_ingresado % 2 == 0:
        num_pares +=1
    else:
        num_impares +=1

    if num_ingresado != 0:
        if num_ingresado > 0:
            num_positivos += 1 
        else:
            num_negativos += 1
    else: num_neutro += 1
print(f"Ingresaste {num_impares} num impares, {num_pares} num pares, {num_negativos} num negativos, {num_positivos} num positivos y {num_neutro} numeros neutros.")
"""
#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#   media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debehola
#   poder procesar 100 números cambiando solo un valor).
"""
cant_num = 3
suma = 0
for i in range(cant_num):
    num_ingresados = int(input(f"Ingrese el numero {i+1}: "))
    suma += num_ingresados

media = suma / cant_num
print (f"La media de los num ingresado es {media}")  
"""
#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#    usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""
num_invertido = ""
num = str(input("Ingrese un numero: "))

for i in range(1,len(num)+1):
    num_invertido = num_invertido + num[-i]

print(f"El numero invertido es {num_invertido}.")
"""

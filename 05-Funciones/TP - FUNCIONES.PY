"""
def imprimir_hola_mundo():
    print("Hola mundo!")

imprimir_hola_mundo()

"""

"""
def saludar_usuario(nombre):
    print(f"Hola {nombre}!.")

nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)
"""

"""
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}. ")

nombre = input("Ingresa tu nombre: ")
apellido = input ("Ingresa tu apellido: ")
edad = input ("Ingresa tu edad: ")
residencia = input("Ingrese su lugar de residencia: ")

#llamo a la funcion con varios parametros
informacion_personal(nombre, apellido, edad, residencia)

"""

"""
def calcular_area_circulo(radio):
    area = 3.14 (radio ** 2)         #calculo del radio
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio #calculo del perimetro
    return perimetro

radio = float(input("Ingrese el radio de un circulo: "))
#Uso los mismo paramteros en dif funciones
print(f"El area del circulo es {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo {calcular_perimetro_circulo(radio)}")

"""

"""
def segundos_a_horas(segundos):
    horas = segundos / 3600     # divide por 3600 (1 hora = 3600 seg)
    return horas


segundos = int(input("Ingrese cantidad de segundos: "))

print(round(segundos_a_horas(segundos), 2))     # llama a la función y redondea a 2 decimales

"""
"""
def tabla_multiplicar(numero):

    for i in range(1,11):
        resultado_tabla = i * numero        # calcula la multiplicación
        print(f"{numero} * {i} = {resultado_tabla}") 

# pedir un número al usuario para luego llamar a la funcion
numero_usuario = int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))
tabla_multiplicar(numero_usuario) 

"""

"""
def operaciones_basicas(a, b):          
    resultado_suma = a + b                  
    resultado_resta = a - b
    resultado_division = a / b
    resultado_multiplicacion = a * b

    #retorno resultado en una tupla
    return(resultado_suma, resultado_resta, resultado_division, resultado_multiplicacion)

    #guardo los parametros en variables
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

#guardo el resultado de la funcion en una variable
resultados = operaciones_basicas(numero1, numero2)

#Accedo al indice de la tupla de la misma manera q una lista
print(f"{numero1} + {numero2} = {resultados[0]}")
print(f"{numero1} - {numero2} = {resultados[1]}")
print(f"{numero1} / {numero2} = {resultados[2]}")
print(f"{numero1} * {numero2} = {resultados[3]}")
"""


"""
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)          #calculo el indice de masa corporal

    return(imc)

#float para que validar el ingreso en decimales
kilos_peso = float(input(f"Ingrese su peso corporal en kilogramos (solo el numero): "))
metros_altura = float(input(f"Ingrese su altura en metros (solo el numero): "))

resultado_imc = calcular_imc(kilos_peso, metros_altura)

#round 2 para que solo muestro dos digitos luego de la coma
print(f"Su indice de masa corporal es: {round(resultado_imc, 2)}")


"""

"""
def celcius_a_fahrenheit(celcius):
    temp_fahren = (celcius * 9/5) + 32        #calculo la temperatura farenheit

    return(temp_fahren)

#Pido la temp en C° y llamo a la funcion
celcius = float(input(f"Ingrese la temperatura en Grados Celcius: "))

resultado = celcius_a_fahrenheit(celcius)


print(f"La conversion de {celcius} °C es: {resultado}")

"""

"""
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3      #calculo promedio

    return(promedio)

a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
c = float(input("Ingrese el tercer numero: "))

#guardo resultado en otra variable para el uso de buenas practicas
resultado_promedio = calcular_promedio(a, b, c)

print(f"El promedio de {a}, {b} y {c} es: {resultado_promedio}")

"""

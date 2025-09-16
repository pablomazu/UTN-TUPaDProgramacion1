
# 1)
# Crear una lista con las notas de 10 estudiantes.
# Mostrar la lista completa.
# Calcular y mostrar el promedio.
# Indicar la nota más alta y la más baja.
"""
lista_notas = [10, 7, 3, 8, 6, 6, 5, 7, 8, 8]           #Creo la lista

print("Nota de los estudiantes: ",lista_notas)          #Muestro lista

cantidad_notas = len(lista_notas)                       #Variables necesarias
suma = 0
nota_max = lista_notas[0]                               #Inicializo las notas en el primer valor
nota_min = lista_notas[0]

for indice_nota in range(cantidad_notas):               #For que repite segun la cantidad de notas(10)
    suma = suma + lista_notas[indice_nota]              #Sumo las notas en una lista
    
    if lista_notas[indice_nota] > nota_max:             #Condicional para encontrar la nota maxima
        nota_max = lista_notas[indice_nota]
    if lista_notas[indice_nota] < nota_min:             #Condicional para encontrar la nota minima
        nota_min = lista_notas[indice_nota]

promedio = suma/cantidad_notas                          #Saco promedio

print(f"El promedio de las notas es: {promedio}, la nota maxima es {nota_max}, y la minima es {nota_min}")
"""

# 2)
# Pedir al usuario que cargue 5 productos en una lista.
# Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# Preguntar al usuario qué producto desea eliminar y actualizar la lista.

"""
lista_productos = []
for i in range(5):
    productos = input(str(f"Ingrese el producto {i+1} : "))             #Pido ingresar productos
    lista_productos.append(productos)                                   #Lo agrego a la lista creada
print("Lista ordenada:", sorted(lista_productos))       

eliminar = input("Ingrese el producto que desea remover: ")             #Guardo el producto que desea eliminar
if eliminar in lista_productos:                                         #Si el producto existe lo elimino sino...
    lista_productos.remove(eliminar)
    print("Producto eliminado. Lista actualizada: ",lista_productos)
else:
    print("El producto no esta en la lista")
"""

# 3)
# Generar una lista con 15 números enteros al azar entre 1 y 100.
# Crear una lista con los pares y otra con los impares.
# Mostrar cuántos números tiene cada lista.

"""
import random                                                       #importo funcion que crea num random
lista_numero = [random.randint(1,100) for _ in range(15)]           #Creo la lista: numeros random del 1 a 100, en un for in range 15 (15 numeros)
print(lista_numero)

lista_pares = []                                                  #Inicializo las lista vacias
lista_impares = []

for i in range(15):                                             #For recorre cada numero para saber si es par o impar.
    if lista_numero[i] % 2 == 0:
        lista_pares.append(lista_numero[i])
    else:
        lista_impares.append(lista_numero[i])

print(len(lista_impares),len(lista_pares))
"""

# 4)
# Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# Crear una nueva lista sin elementos repetidos.
# Mostrar el resultado.
"""
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sin_repetir = []                                       # Lista para guarda datos sin repetir

cantidad_num = len(datos)

for indice in range(cantidad_num):                            # Bucle que analiza cada numero de datos
    encontrado = False                                        # Bandera False que asume que NO esta repetido cada numero
    for indice2 in range(len(datos_sin_repetir)):             # Bucle para buscar en la nueva lista
        if datos[indice] == datos_sin_repetir[indice2]:       # Si el numero esta en lista nueva encontrado = true y terminar (break)     
            encontrado = True                                               
            break                                             # Si no es el mismo numero se agregar ese numero en la lista nueva
    if encontrado == False:                                   
        datos_sin_repetir.append(datos[indice])
print(datos_sin_repetir)
"""

# 5)
# Crear una lista con los nombres de 8 estudiantes presentes en clase.
# Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# Mostrar la lista final actualizada.
"""
lista_nombres = []                          #Creo una lista vacia
nombre = ""                                 #Variable para guardar los nombres
completo = False                            #Bandera inicializada false

while completo == False:                    #mientras sea falso...
    respuesta = input("¿Desea agregar (A), o eliminar nuevos estudiantes (E)?").strip().upper()             # tranforma en mayuscula y elimina espacio vacio

    if respuesta == "A":                                                                    #si la respuesta es A : agregar nombre
        nombre = input("Agrege el nombre del estudiante: ").strip().upper()
        lista_nombres.append(nombre)                                                            #agrega el valor de variable nombre en la lista_nombres
        print(f"{nombre} fue agregado.")


    elif respuesta == "E":                                                                  #Sino si, la respuesta es "E": agregar el nombre a eliminar
        nombre = input("Ingrese el nombre a eliminar: ").strip().upper()

        if nombre in lista_nombres:
            lista_nombres.remove(nombre)                                                    #Si el nombre esta en lista, lo elimina.
            print(f"{nombre} fue eliminado.")
        else:
            print("El nombre ingresado no esta en la lista")

    if len(lista_nombres) == 8:                                                             #Si la lista contiene 8 valores (nombres) bandera = true. Termina el algoritmo
        completo = True

print(f"Lista final: {lista_nombres}")
"""

# 6)
# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha 
# (el último pasa a ser el primero).

# Paso 1: Guardá el último elemento en una variable temporal.

# Paso 2: Con un bucle, recorré desde el penúltimo elemento hasta el primero.

# Paso 3: En cada iteración, mové el elemento actual a la posición siguiente (derecha).

# Paso 4: Al final, asigná el elemento temporal (el último original) a la primera posición

"""

lista_num = [20,5,9,10,200,6,55]                    #creo la lista
n = len(lista_num)                                  #cantidad de num en lista
ultimo_num = lista_num[n-1]                         #Guardo el ultimo num 
print("Lista original", lista_num)

for i in range(n-1, 0, -1):                         #bucle que va desde el penultimo, hacia atras en -1
    lista_num[i] = lista_num[i-1]                   #Pisa los numeros con el anterior
lista_num[0] = ultimo_num                           #Remplazo el primero con el ultimo
print(lista_num)
"""

# 7)
# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# Calcular el promedio de las mínimas y el de las máximas.
# Mostrar en qué día se registró la mayor amplitud térmica.
"""
matriz_temperatura = [               #Matriz con 7 filas (dias) y 2 columna(max y min)                      
    [7,22],
    [10,16],
    [10,19],
    [6,18],
    [5,17],
    [6,19],
    [9,17]
    ]

matriz_dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]  #Matriz con los dias para mostrar luego

cantidad_dias = len(matriz_temperatura)     #Numero de cantidad de dias(7)


suma_min = 0
suma_max = 0                #Creo variables necesario e inicializo en 0
maxima_amplitud = 0

for i in range(cantidad_dias):               #For que repite la cantidad de dias(7)
    suma_min = suma_min + matriz_temperatura[i][0]     #Suma cada temperatura continuamente de la columna 0 (temp min)
    suma_max = suma_max + matriz_temperatura[i][1]     #Realiza lo mismo con la otra columna (temp max)
    
    amplitud = (matriz_temperatura[i][1] - matriz_temperatura[i][0])     #Resta cada temperatura max con la minima

    if amplitud > maxima_amplitud:      #Si es mayor que la anterior la guarda sino no
        maxima_amplitud = amplitud
        dia_amplitud = i                #Guarda el numero de iteracion (dia de la semana)

dia_amplitud = matriz_dias[i]           #Asigna el dia segun el numero de iteracion de la mayor amplitud

promedio_minima = suma_min / cantidad_dias          #Calcula promedios
promedio_maxima = suma_max / cantidad_dias

print(f"El promedio de las temperaturas minimas es: {promedio_minima}, y el de las maximas: {promedio_maxima}")
print(f"El dia con mayor amplitud termica fue: {dia_amplitud}, de {amplitud}°C")

"""
# 8)
# Crear una matriz con las notas de 5 estudiantes en 3 materias.

# Mostrar el promedio de cada estudiante.

# Mostrar el promedio de cada materia.

"""
estudiantes_notas = [                                           #Creo la matriz con notas (5x3)
    [5,7,8],
    [4,6,6],
    [8,9,10],
    [7,7,9],
    [8,7,8]
]
cantidad_estudiantes = len(estudiantes_notas)                   #Obtengo cantidad de estudiantes (5)
cantidad_materias = 3                                           
suma = 0                                                        #Inicializo variables necesarias
materia_1 = 0
materia_2 = 0
materia_3 = 0

for i in range(cantidad_estudiantes):                           #Creo dos for (uno para estudiantes y otro recorrer materias)
    suma = 0                                                    #Reinicio la variable suma en el bucle interno para que no acumule

    for n in range(cantidad_materias):
        suma = suma + estudiantes_notas[i][n]                   #Sumo las notas por estudiantes para poder sacar promedio
        promedio_estudiante = suma / cantidad_materias          #Calculo el promedio de las notas por estudiantes

    materia_1 = materia_1 + estudiantes_notas[i][0]             #Sumo las notas de las materias, por cada materia separada
    materia_2 = materia_2 + estudiantes_notas[i][1]
    materia_3 = materia_3 + estudiantes_notas[i][2]

    print(f"Promedio de estudiante {i+1}: {promedio_estudiante} ")

prom_nota1 = materia_1 / cantidad_estudiantes                   #Saco el promedio por cada materia
prom_nota2 = materia_2 / cantidad_estudiantes
prom_nota3 = materia_3 / cantidad_estudiantes

print(f"Promedio de materia 1: {prom_nota1}, materia 2: {prom_nota2}, materia 3: {prom_nota3}")

"""

#9)
# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).

# Inicializarlo con guiones "-" representando casillas vacías.

# Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".

# Mostrar el tablero después de cada jugada.

"""
ta_te_ti = []                           #creo lista vacia

for i in range(3):                      #bucles anidados: el exterior genera 3 filas, el interior le agrega a esas filas "-" y agrega las filas a la lista ta_te_ti
    fila = []
    for j in range(3):
        fila.append("-")
    ta_te_ti.append(fila)                   

for fila in ta_te_ti:                       #bucles anidados: por cada fila (3) en la matriz ta_te_ti: por cada celda in fila (3). (3x3)
    for celda in fila:                      #Celda toma el valor "-" temporalmente (es el valor de los elementos en fila)
        print(celda, end= " ")              #Mostrar celda ("-") y un espacio entre cada celda
    print()                                 #Print para que haga salto de linea

#variables de control
jugador = "X"
jugadas = 0

while jugadas < 9:                          #mientras jugadas sea menor a 9

    print(f"\nTurno del jugador {jugador}")     

    fila = int(input("Ingrese la fila (0-2)"))              #guardar fila y columna a jugar
    columna = int(input("Ingrese la fila (0-2)"))

    if fila < 0 or fila > 2 or columna < 0 or columna > 2:          #Si fila o columna no respetan es "espacio de juego"...
        print("Posicion fuera de rango")
        continue                                                    #volver a pedir la jugada sin perder el turno

    if ta_te_ti[fila][columna] == "-":                              #Condicional para verificar que no haya nada
        ta_te_ti[fila][columna] = jugador
        jugadas +=1                                                 #Sumo las jugadas para verificar que no haya mas de 9
    else:
        print("Casilla ocupada.Intente de nuevo")
        continue 

    for fila in ta_te_ti:
        for celda in fila:
            print(celda, end= " ")                                 #imprime la matriz
        print()
    
    if jugador == "X":                                             #Si jugador es X (quiere decir que jugo X), ahora juega 0
        jugador = "O"
    else:
        jugador = "X"


"""

# 10)
# Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# Mostrar el total vendido por cada producto.
# Mostrar el día con mayores ventas totales.
# Indicar cuál fue el producto más vendido en la semana.
"""

ventas = [
    [5, 3, 6, 8, 9, 2, 7],
    [2, 2, 5, 7, 6, 9, 5],              #Creo la matriz 4x7
    [4, 5, 3, 6, 5, 5, 10],
    [7, 5, 9, 6, 7, 8, 9]
]

#Mostrar el total vendido por cada producto.
totales_productos = []                       #Lista que me va a servir mas adelante
cantidad_dias = len(ventas[0])               #Creo variables necesarias
cantidad_productos = len(ventas)

for i in range(cantidad_productos):
    total_vendido = 0                       #Reinicio variable para que no se pise

    for j in range(cantidad_dias):
        total_vendido = total_vendido + ventas[i][j]            #Sumo las ventas en total
    totales_productos.append(total_vendido)                     #Agrego el numero de ventas totales en otra lista

    print(f"El producto {i+1} se vendio: {total_vendido} veces.")


# Mostrar el día con mayores ventas totales.
mayor_dia_ventas_totales = 0
dia_mayor= 0

for j in range(cantidad_dias):
    total_dia = 0

    for i in range(cantidad_productos):
        total_dia += ventas[i][j]                       #Sumo las ventas de los dias a "total_ventas"
    print(f"Total del dia {j+1}: {total_dia}")          #Lo muestro cada vez
    if total_dia > mayor_dia_ventas_totales:            #Si total_dia es mayor que... remplazo el valor
        mayor_dia_ventas_totales = total_dia
        dia_mayor = j                                   #Si entra en el IF, cuento el dia en una variable (el dia es el indice J)

print(f"\nEl dia con mayores ventas fue el dia {dia_mayor+1}, con un total de {mayor_dia_ventas_totales} ventas.")


# Indicar cuál fue el producto más vendido en la semana.
producto_mayor_vendido_sem = 0          
indice_mayor = 0
for i in range(cantidad_productos):                         #For que itera 4 veces
    if totales_productos[i] > producto_mayor_vendido_sem:   #Si la total_productos(Comparo cada iteracion en la lista antes creada con la variable nueva)
        producto_mayor_vendido_sem = totales_productos[i]      #Guardo si es mayor
        indice_mayor = i                                        #Guardo el indice donde el numero es mayor

print(f"El prodcuto mas vendido fue el {indice_mayor+1}, con {producto_mayor_vendido_sem} ventas en la semana")
"""
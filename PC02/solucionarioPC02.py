# Solucionario de PC02

# Problema 1: Encontrar números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700
print("Problema 1")
resultado = []
for x in range(1500, 2701):
    if x % 7 == 0 and x % 5 == 0:
        resultado.append(x)
print("Números divisibles por 7 y múltiplos de 5 entre 1500 y 2700:", resultado)

# Problema 2: Construir un patrón de asteriscos
print("\nProblema 2")
for i in range(1, 6):
    print("* " * i)
for i in range(4, 0, -1):
    print("* " * i)


# Problema 3: Ingresar números hasta que el usuario decida y contar pares e impares
print("\nProblema 3")
numeros = []
while True:
    continuar = input("¿Desea ingresar un número? (SI/NO): ").strip().lower()
    if continuar != 'si':
        break
    numero = int(input("Ingrese el número: "))
    numeros.append(numero)

pares = len([n for n in numeros if n % 2 == 0])
impares = len([n for n in numeros if n % 2 != 0])

print("Números ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)


# Problema 4: Generar un listado de alumnos y sus calificaciones
print("\nProblema 4")
alumnos = []
n = int(input("Ingrese la cantidad de alumnos: "))
for _ in range(n):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = [int(input(f"Ingrese la nota {i+1} del alumno {nombre}: ")) for i in range(3)]
    alumnos.append({"Alumno": nombre, "Notas": notas})

print("Listado de alumnos y sus notas:")
for alumno in alumnos:
    print(alumno)


# Problema 5: Verificar la cantidad de veces que un dígito aparece en un número
print("\nProblema 5")
numero = 15789000
digito = 0
cantidad = str(numero).count(str(digito))
print(f"Cantidad de veces que el dígito {digito} aparece en el número {numero}: {cantidad}")


# Problema 6: Obtener la serie de Fibonacci entre 0 y 50
print("\nProblema 6")
a, b = 0, 1
fibonacci = []
while a <= 50:
    fibonacci.append(a)
    a, b = b, a + b
print("Serie de Fibonacci entre 0 y 50:", fibonacci)


# Problema 7: Verificar si un número es primo
print("\nProblema 7")
numero = 29
if numero <= 1:
    es_primo = False
else:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
print("¿Es primo?", es_primo)


# Problema 8: Calcular el factorial de un número
print("\nProblema 8")
numero = 5
if numero == 0:
    factorial = 1
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
print("Factorial:", factorial)


# Problema 9: Eliminar vocales de una cadena de texto
print("\nProblema 9")
texto = "What's your name?"
vocales = "aeiouAEIOU"
resultado = ''.join([char for char in texto if char not in vocales])
print("Texto sin vocales:", resultado)


# Problema 10: Convertir fechas en formato estadounidense a formato AAAA-MM-DD
print("\nProblema 10")
fecha1 = "9/8/1636"
fecha2 = "Septiembre 8, 1636"
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def convertir_fecha(fecha):
    if '/' in fecha:
        mes, dia, anio = fecha.split('/')
        mes = f"{int(mes):02}"
        dia = f"{int(dia):02}"
    else:
        mes_texto, dia, anio = fecha.replace(",", "").split()
        mes = f"{meses.index(mes_texto) + 1:02}"
        dia = f"{int(dia):02}"
    print(f"Fecha en formato AAAA-MM-DD: {anio}-{mes}-{dia}")

convertir_fecha(fecha1)
convertir_fecha(fecha2)

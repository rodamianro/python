# Programa para calcular el promedio de las notas de unos estudiante
# utilizando diccionario y tuplas

# Inicializamos el grupo de estudiantes
grupo = {}

# Creamos un ciclo para ingresar los estudiantes y sus notas
while True:
    # Ingresamos el nombre del estudiante
    nombre = input(
        "Ingresa el nombre del estudiante (o exit para detenerse): ")
    # Si el nombre es 'exit' salimos del ciclo
    if nombre == 'exit':
        break
    # Ingresamos la calificación del estudiante
    calif = int(input("Ingresa la calificación del alumno (0-5): "))

    # Comprobamos si el estudiante ya esta registrado en el grupo
    if nombre in grupo:
        # En caso de estarlo agregamos la calificación  a la tupla de calificaciones
        grupo[nombre] += calif,
    else:
        # En caso contrario agregarmos al estudiante y su calificación
        grupo[nombre] = calif,

# Recorremos el diccionario de estudiantes
for estudiante, calificaciones in sorted(grupo.items()):
    # Creamos una variable para acumular las calificaciones
    promedio = 0
    # Recorremos las calificaciónes del estudiante
    for calificación in calificaciones:
        # Sumamos la calificación
        promedio += calificación
    # Mostramos el nombre del estudiante y su correspondiente promedio de calificaciones
    print(estudiante, ":", promedio/len(calificaciones))

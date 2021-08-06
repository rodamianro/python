# Leyendo elementos de una tupla
tupla = (1, 10, 100, 1000)
print("Primer elementos [0]:", tupla[0])
print("Ultimo elemento [-1]:", tupla[-1])
print("Rodaje [1:]:", tupla[1:])
print("Rodaja [:-2]:", tupla[:-2])
# Recorres una tupla
for elem in tupla:
    print("Elemento for:", elem)

# Uniendo dos tuplas
tupla1 = tupla + ("a", "b")
print("Union de tuplas:", tupla1)
# Multiplicando tuplas
tupla2 = tupla * 3
print("Multiplicación de tuplas:", tupla2)
# Cantidad de elementos en una tupla
cantidadElementos = len(tupla2)
print("Cantidad de elementos (len()):", cantidadElementos)
# Comprobar si un elemento existe en una tupla
print("Si existe el elemento con valor 10:", 10 in tupla)
# Comprobar si un elemento no existe en una tupla
print("No existe el elemento con valor 10:", 10 not in tupla)
# Intercambiar valores entre tuplas
var = 123
t1 = 1,
t2 = 2,
t3 = 3, var,
print("Tuplas originales: ", t1, t2, t3, sep=" - ")
t1, t2, t3 = t2, t3, t1
print("Tuplas intercambiadas: ", t1, t2, t3, sep=" - ")

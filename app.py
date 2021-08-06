# Diccionarios

# Crear diccionario
diccionario = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
numerosTelefono = {"jefe": 5551234567, "Suzy": 22657854310}
diccionarioVacio = {}

print("Diccionario: ", diccionario)
print("Números de telefono:", numerosTelefono)
print("Diccionario vacio:", diccionarioVacio)

# Obtener los valores de un diccionario
print("Obteniendo el valor con la clave gato:", diccionario["gato"])
print("Obteniendo el valor con la clave Susy:", numerosTelefono["Suzy"])

# Recorriendo un diccionario
# Método keys()
print("Diccionario con el método keys()")
for key in diccionario.keys():
    print(key)

# Método item()
print("Diccionario con el método item()")
for clave, valor in diccionario.items():
    print(clave, '->', valor)

# Método values()
print("Diccionario con el método values()")
for valor in diccionario.values():
    print(valor)

# Ordenar diccionario
print("Diccionario ordenado")
for key in sorted(diccionario.keys()):
    print(key, '->', diccionario[key])

# Modificar el valor de una clave
diccionario["gato"] = 'minou'
print("Diccionario modificando un valor:", diccionario)

# Agregar un nuevo conjunto de clave-valor
diccionario["cisne"] = "cygne"
diccionario.update({"pato": "canard"})
print("Diccionario agregando una nueva clave-valor:", diccionario)

# Eliminar un elemento de un diccionario
del diccionario["perro"]
diccionario.popitem()
print("Diccionario despues de eliminar la clave perro y el ultimo elemento:", diccionario)

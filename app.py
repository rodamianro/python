def esUnTriangulo(a, b, c):
    """Indica si una combinación de 3 lados pueden formar un triangulo.

    Para que 3 lados puedan construir un triangulo la suma de dos lados debe ser mayor o igual a lado restante
    y esto para todos los lados.
    Retorna True o False dependiendo de si los valores de los lados pueden o no formar un triangulo

    Parámetros:

        a,b,c -- Valores de cada lado

    """
    return a+b > c and a+c > b and b+c > a


def esUnTrianguloRectangulo(a, b, c):
    """Indica si un triángulo es un triángulo rectángulo

    Para comprobar si un triángulo es un triángulo rectángulo se aplica el teorema de pitágoras que dice:
    c**2 = a**2 + b**2
    Si se cumple que la hipotenusa al cuadrado es igual a la suma de los catetos, cada uno al cuadrado el triángulo
    es un triángulo rectángulo

    Parámetros:
        a,b,c -- Valor de cada lado

    """
    if not esUnTriangulo(a, b, c):
        False
    if c > a and c > b:
        return c**2 == a**2+b**2
    if a > b and a > c:
        return a**2 == b**2+c**2
    if b > a and b > c:
        return b**2 == a**2+c**2


def heron(a, b, c):
    """Calcula el área de un triángulo conociendo las longitudes de sus lados

    Pámatros:
        a,b,c -- Lados del triángulo

    Devuelve el campo de un triangulo que se calcula de las formulas:

        s = (a+b+c)/2

        A = (s(s-a)(s-b)(s-c))**0.5    

    """
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5


# Calcula el área de un triángulo
def areaTriangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        None
    else:
        return heron(a, b, c)


# Prueba de las funciónes
#print(esUnTriangulo(1, 1, 1))
#print(esUnTriangulo(1, 1, 3))
a = 5
b = 3
c = 4
if esUnTriangulo(a, b, c):
    print("Felicidades, puede ser un triángulo.")
else:
    print("Lo siento, no puede ser un triángulo.")

if esUnTrianguloRectangulo(a, b, c):
    print("Felicidades, es un triángulo rectángulo.")
else:
    print("Lo siento, no puede es un triángulo rectángulo.")

print(areaTriangulo(a, b, c))

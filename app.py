def factorial(numero):
    """Calcula el factorial de un número

    Parámetros:

        numero -- El numero del cual se le quiere sacar el factorial

    Devuelve el total del factorial de un número

    """
    if numero < 0:
        return None
    resultado = 1
    for i in range(numero):
        resultado *= i+1
    return resultado


def factorialRecursiva(numero):
    """Calcula el factorial de un número de forma recursiva

    Parámetros:

        numero -- El numero del cual se le quiere sacar el factorial

    Devuelve el total del factorial de un número

    """
    if numero < 0:
        return None
    if numero < 2:
        return 1
    return numero * factorialRecursiva(numero-1)


def fibonacci(n):
    """Calcula el valor correspondiente a la iteración de la serie de fibonacci

    Parámetros:

        n -- Número de la iteración de la cual se quiere saber el valor

    Devuelve el valor correpondiente a la iteración indicada

    """
    if n < 1:
        return None
    if n < 3:
        return 1
    elemento1 = elemento2 = 1
    sum = 0
    for i in range(3, n+1):
        sum = elemento1+elemento2
        elemento1, elemento2 = elemento2, sum
    return sum


def fibonacciRecursiva(n):
    """Calcula el valor correspondiente a la iteración de la serie de fibonacci de forma recursiva

    Parámetros:

        n -- Número de la iteración de la cual se quiere saber el valor

    Devuelve el valor correpondiente a la iteración indicada

    """
    if n < 1:
        return None
    if n < 3:
        return 1
    return fibonacciRecursiva(n-1)+fibonacciRecursiva(n-2)


for n in range(1, 6):  # probando
    print(n, factorialRecursiva(n))

for n in range(1, 10):  # probando
    print(n, "->", fibonacciRecursiva(n))

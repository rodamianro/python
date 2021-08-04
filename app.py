def imc(peso, altura):
    """Calcula el índice de masa corporal.

    Devuelve el valor del indice de masa corporal que resulta de la operación:

        peso/altura ** 2

    Parámetros:

        peso -- El peso en kilogramos de una persona

        altura -- La altura en metros de una persona

    Excepciones:
    None -- Si (altura < 1 o altura > 2.5)
    None -- Si (peso < 20 o peso > 200) 
    """

    # Si una línea de código termina con \ python entiende que la línea contiua en la siguiente
    if altura < 1 or altura > 2.5 or \
            peso < 20 or peso > 200:
        return None
    return peso/altura ** 2


def libraToKilogramos(valor):
    """Convierte libras a kilogramos

    Retorna el valor ingresado que corresponde a las libras en su equivalente en kilogramos donde:

        1 libra = 0.45359237 kilogramos

    Parámetros:

        valor -- Es el valor de las libras que se quieren convertir 

    """
    return valor * 0.45359237


def piespulgadasToMetros(pie, pulgada=0):
    """Convierte de pies con pulgadas a metros

    Devuelve el valor correpondiente al hacer la converción de pies pulgadas a metros donde:

        1 pie = 0.3048m y
        1 pulgada = 0.0254m

    Parámetros:

        pie -- Cantidad de pies a convertir

        pulgada -- Cantidad de pulgadas a sumarle a los pies

    """
    return pie * 0.3048 + pulgada * 0.0254

# Pruebas de los funciones
#print(imc(20, 1))
#print(libraToKilogramos(1))
#print(piespulgadasToMetros(6,0))

print(imc(peso=libraToKilogramos(176), altura= piespulgadasToMetros(5,7)))


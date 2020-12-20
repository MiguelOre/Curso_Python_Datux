# 1. Importar librerias
import os

# 2. Asignar valores de constantes

# 3. Funciones y/o Clases

def sumar(a,b):
    return a + b

def resta(a,b, modo=True):
    """
    Funcion que realiza la resta de dos numeros
    """
    if modo:
        return a - b
    else:
        return b - a

def multiplicar(a,b):
    """
    Funcion que realiza la multiplicacion de dos numeros
    
    Parameters
    ----------
    a : float
        Valor numerico `a`.
    b : float
        Valor numerico `b`

    Returns
    -------
    float
    Resultado de la multiplicacion de: `a` * `b`
    """
    return a * b

def division(a,b):
    """
    Retorna la division a / b
    """
    return a/b

# 4. Mi programa principal
if __name__ == "__main__":
    # entrada de datos
    x = float(input('Ingrese el primer numero: '))
    y = float(input('Ingrese el segundo numero: '))
    # calculos
    s = sumar(x, y)
    r = resta(x,y,False)
    m = multiplicar(4, 6)
    print(f'El valor de la suma de los datos es {s}')
    print('El valor de la resta de los datos es {}'.format(r))
    print(f'El resultado de la multiplicacion es {m}')
    # pausar el sistema
    os.system('pause')
# 1. importando librerias
import operaciones

# importo libreria 'potencia' que se encuentra en carpeta funciones
from funciones import potencia

from mas_funciones import hola

# programa principal
if __name__ == "__main__":
    
    d = operaciones.division(12, 4)    
    p = potencia.potenciacion(7,2)

    hola.hola()
    
    print(f'el valor de la division de {12} / {4} es: {d}')
    print(f'el valor de 7 a la 2 es {p}')
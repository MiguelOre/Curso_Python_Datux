# 1. importacion de librerias


# 2. creacion de funciones  y/o clases
def par_impar(number):
    if (number % 2 == 0):
        print(f"El numero {number} es par")
    else:
        print(f"El numero {number} es impar")

# 3. ejecucion de programa principal
while True:
    try:
        number = int(input("Ingrese un numero: "))
        break
    except:
        print('valor ingresado no corresponde a un numero entero')

par_impar(number)








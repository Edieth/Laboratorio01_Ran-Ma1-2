import locale
locale.setlocale(locale.LC_ALL, "es")

from Productos import Productos
import sys
Prod= Productos
num = 0
def salir():
    print("¿Desea comprar un producto más?")
    num1 = int(input("1-Sí      2-No"))
    if num1 == 1:
        num = 0
    elif num1 == 2:
        print("¡Gracias por su compra!")
        sys.exit()

while num != 5 :
    print("------Menú--------\n1-Bebidas frías\n2-Bebidas calientes\n3-Postres\n4-Productos con alcohol\n5-Salir del menú")

    num = int(input("Ingrese el número según la opción deseada"))
    if num == 1 :
        print("--------Menú de bebidas frías------")
        print("1-Café Affogato\n2-Café con hielo\n3-Café Frappuccino\n4-Café tropical")
        opc = int(input("¿Cuál bebida fría desea llevar?"))

        if opc == 1:
            for i, contar in enumerate(Prod.Affogato)
            print(Prod.Affogato)
            salir()
        elif opc == 2:
            print(Prod.Hielo)
            salir()
        elif opc == 3:
            print(Prod.Frappuccino)
            salir()
        elif opc == 4:
            print(Prod.Tropical)
            salir()
        else:
            print("Opción invalida, intente de nuevo")

    elif num == 2:
        opc1 = int(input("Digite el número correspondiente a la bebida caliente deseada:\n"
                    "1-Café largo\n2-Café con leche\n3-Café cortado\n4-Cappuccino\n5-Café latte"))
        if opc1 == 1:
            print(Prod.Largo)
            salir()
        elif opc1 == 2:
            print(Prod.Leche)
            salir()
        elif opc1 == 3:
            print(Prod.Cortado)
            salir()
        elif opc1 == 4:
            print(Prod.Cappuccino)
            salir()
        elif opc1 == 5:
            print(Prod.Latte)
            salir()
        else:
            print("Opción invalida, intente de nuevo")


    if num == 3:
        print("--------Menú de postres------")
        print("1-Panellets\n2-Hojaldre\n3-Tiramisu con alcohol**")
        opc2 = int(input("¿Cuál postre desea llevar?"))

        if opc2 == 1:
            print(Prod.Panellets)
            salir()
        elif opc2 == 2:
            print(Prod.Hojaldre)
            salir()
        elif opc2 == 3:
            print(Prod.Tiramisu)
            salir()
        else:
            print("Opción invalida, intente de nuevo")

    if num == 4:
        opc3 = int(input("Digite el número correspondiente a la bebida de café con alcohol deseada:\n"
                    "1-Café Carajillo\n2-Café Caribeño\n3-Café Irlandés"))

        if opc3 == 1:
            print(Prod.Carajillo)
            salir()
        elif opc3 == 2:
            print(Prod.Caribeno)
            salir()
        elif opc3 == 3:
            print(Prod.Irlandes)
            salir()
        else:
            print("Opción invalida, intente de nuevo")
    else:
        print("Opción invalida, intente de nuevo")
import funciones as fn

while True:
    print("TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE")
    print("1.- Comprar entrada a “los Fortificados.")
    print("2.- Comprar entrada a “los Iluminados.")
    print("3.- Stock de entradas para ambos conciertos.")
    print("4. Salir")

    opc = int(input("Ingrese opción: "))

    if opc == 1:
        fn.comprar_entradas_Fortificados()
    elif opc == 2:
        fn.comprar_entradas_iluminados()
    elif opc == 3:
        fn.stock_entradas()
    elif opc == 4:
        print("Programa terminado...")
    else:
        print("Debe ingresar una opción válida!!")
compradores_fortificados = {}
compradores_iluminados = {}

entradas_fortificados = [500]
entradas_iluminados = [500]


def comprar_entradas_Fortificados():
    entrada = False
    nom = input("Ingrese nombre de comprador: ").lower()
    for x in compradores_fortificados:
        if nom not in compradores_fortificados:
            nom.append(x)
    else:
         print("Este nombre ya esta registrado")
         
    tip_entrada = input("Ingrese tipo de entrada (G/V): ").lower()
    if tip_entrada != "G"or"V":
        print("Esta opcion no es valida")
    else:
        pass
    codigo = input("Ingrese código de confirmación: ").isdigit()
    if len(codigo)<6 and " " in codigo:
        print("Código no válido. Intente otra vez.")
    else:
        print("Código validado.")
        entrada = True
        if entrada == True:
            print("¡Entrada registrada con éxito para “los Fortificados”!")
            entradas_fortificados = entradas_fortificados - 1

def comprar_entradas_iluminados():
    entrada2 = False
    nombre = input("Ingrese nombre de comprador: ").lower()
    for i in compradores_iluminados():
        if nombre not in compradores_iluminados:
            nombre.append(i)
        else:
            print("Este nombre ya esta registrado")

    tipo_entrada = input("Ingrese tipo de entrada (CV/PAL): ").lower()
    if tipo_entrada == "CV" or tipo_entrada == "PAL":
        compradores_iluminados(tipo_entrada[tipo_entrada])
    else:
        print("Esta opcion no es valida")
    
    codigo = input("Ingrese código de confirmación: ")
    if len(codigo) <5 and " " in codigo:
        print("código no válido. Intente otra vez.")
        entrada2 = True
        if entrada2 == True:
            print("¡Entrada registrada con éxito para “los Fortificados”!")
            entradas_iluminados = entradas_iluminados - 1

def stock_entradas():
    print(f"Entradas disponibles para los Fortificados:", entradas_fortificados)
    print(f"Entradas disponibles para “los Iluminados”: ", entradas_iluminados)
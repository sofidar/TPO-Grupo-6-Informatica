def leervendedor():
    # Asegura que el número de vendedor sea positivo
    num_vendedor = int(input("Número vendedor? (-1 para terminar): "))
    while num_vendedor != -1 and num_vendedor < 1:
        print("Vendedor inválido, por favor ingrese un número de vendedor positivo")
        num_vendedor = int(input("Número vendedor? (-1 para terminar): "))

    return num_vendedor

def ingresar_datos():
    # Crea listas para cada tipo de dato
    vendedores = []
    vendedor = leervendedor()
    ventas = []
    cantidades = []
    ventas_individuales = []
    
    # Añade cada tipo de dato en bucle
    while vendedor != -1:
        valor_venta = float(input("Importe de la venta? "))
        ventas_individuales.append((vendedor, valor_venta))

        encontrado = False # Verifica si un vendedor se encuentra ya en la lista
        for i in range(len(vendedores)):
            if vendedores[i] == vendedor:
                ventas[i] = ventas[i] + valor_venta
                cantidades[i] = cantidades[i] + 1
                encontrado = True

        if encontrado==False:
            vendedores.append(vendedor)
            ventas.append(valor_venta)
            cantidades.append(1)

        vendedor = leervendedor()

    return vendedores, ventas, cantidades, ventas_individuales

def ordenar(vendedores, ventas, cantidades):
    # Ordena a los vendedores segun las ventas totales, de mayor a menor
    for i in range(len(ventas)):
        for j in range(i + 1, len(ventas)):
            if ventas[j] > ventas[i]:
                vendedores[i], vendedores[j] = vendedores[j], vendedores[i]
                ventas[i], ventas[j] = ventas[j], ventas[i]
                cantidades[i], cantidades[j] = cantidades[j], cantidades[i]

    return vendedores, ventas, cantidades

def busqueda_mayor_cantidad(cantidades):
    # Busca al vendedor con la mayor cantidad de ventas
    mayor_cantidad = 0
    indice_mayor = 0
    for i in range(len(cantidades)):
        if cantidades[i] > mayor_cantidad:
            mayor_cantidad = cantidades[i]
            indice_mayor = i

    return indice_mayor

def busqueda_mayor_venta(ventas_individuales):
    # Busca la venta de mayor valor y guarda el numero de su vendedor
    mayor_venta = 0
    vendedor_mayor_venta = 0
    for num_vendedor, valor_venta in ventas_individuales:
        if valor_venta > mayor_venta:
            mayor_venta = valor_venta
            vendedor_mayor_venta = num_vendedor

    return vendedor_mayor_venta, mayor_venta

def imprimir_resultados(vendedores,ventas,cantidades,ventas_individuales):
    # Imprime los resultados pedidos en la consigna
    print("\nVentas totales por vendedor (de mayor a menor) y promedios:\n")
    for i in range(len(vendedores)):
        promedio = ventas[i] / cantidades[i]
        print("Vendedor número:",vendedores[i],"Ventas $",ventas[i],"  Promedio por venta:",promedio,"\n")

    indice_mayor = busqueda_mayor_cantidad(cantidades)
    print("El vendedor con la mayor cantidad de ventas es el número",vendedores[indice_mayor],"con",cantidades[indice_mayor],"ventas\n")

    vendedor_mayor_venta, mayor_venta = busqueda_mayor_venta(ventas_individuales)
    print("La mayor venta realizada es de $",mayor_venta,"por el vendedor número",vendedor_mayor_venta)


# Programa principal

vendedores, ventas, cantidades, ventas_individuales = ingresar_datos()
vendedores, ventas, cantidades = ordenar(vendedores, ventas, cantidades)
imprimir_resultados(vendedores, ventas, cantidades, ventas_individuales)

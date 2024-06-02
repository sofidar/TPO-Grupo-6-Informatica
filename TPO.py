#Una empresa cuenta con un plantel de vendedores, numerados con valores positivos arbitrarios. Por cada venta realizada se ingresa por teclado el número de vendedor y el importe
#de la misma, donde un número de vendedor -1 indica el final de los datos. Realizar un programa para imprimir:
#· Total vendido por cada vendedor, ordenado de mayor a menor según el total vendido.
#· Importe de la venta promedio por vendedor.
#· Número de vendedor con mayor cantidad de ventas.
#· Importe y número de vendedor correspondiente a la mayor venta realizada.
#La cantidad de vendedores no se conoce. Este dato deberá deducirse se las ventas ingresadas.

#una fucnión que ingrese datos (las  listas)
#una función que sea el método de inserción
#una función que de total vendido por vendedor
#función de promedio de ventas x vendedor
# función del vendedor con mayor cantidad de ventas --> buscar 
#función de mayor venta realizada --> buscar el mayor valor de la lista de ventas
    
def leervendedor():
    # Asegura que el número de vendedor sea positivo
    num_vendedor = int(input("Número vendedor? (-1 para terminar): "))
    while num_vendedor != -1 and num_vendedor < 1:
        print("*Vendedor inválido*")
        num_vendedor = int(input("Número vendedor? (-1 para terminar): "))
    return num_vendedor

def ingresar_datos():
    # Ingresa el valor de las ventas de cada vendedor
    ventas = [0]  # Inicia la lista con un elemento para el vendedor 0
    num_ventas = [0]  # Inicializa la lista con un elemento para contar las ventas del vendedor 0
    promedios = []
    vendedor = leervendedor()
    while vendedor != -1:
        importe = float(input("Importe de la venta? "))
        # Asegurarnos de que la lista de ventas tenga suficientes elementos para el nuevo vendedor
        while len(ventas) <= vendedor:
            ventas.append(0)
            num_ventas.append(0)
        ventas[vendedor] = ventas[vendedor] + importe
        num_ventas[vendedor] = num_ventas[vendedor] + 1
        vendedor = leervendedor()

    for i in range(1, len(ventas)):
        if num_ventas[i] > 0:
            promedio = ventas[i] / num_ventas[i]
            promedios.append(promedio)
            print("El vendedor", i, "vendió $", ventas[i]," en total con un promedio de $",promedio," por venta.")
    return promedios, ventas

def metododeinsercion(lista, referencias):
    # Ordena una lista mediante el método de inserción
    for i in range(1, len(lista)):
        aux = lista[i]
        aux_ref = referencias[i]
        j = i
        while j > 0 and lista[j - 1] > aux:
            lista[j] = lista[j - 1]
            referencias[j] = referencias[j - 1]
            j -= 1
        lista[j] = aux
        referencias[j] = aux_ref
    return lista, referencias

def inversorlista(lista):
    listaInvertida = []
    for i in range(len(lista) -1, -1, -1):
        listaInvertida.append(lista[i])
    return listaInvertida

# Programa principal
promedios, ventas = ingresar_datos()
referencias = list(range(len(ventas) + 1))  # Referencias a los vendedores


ventas_ordenadas, referencias_ordenadas = metododeinsercion(ventas, referencias)
ventas_ordenadas_desc = inversorlista(ventas_ordenadas)
referencias_ordenadas_desc = inversorlista(referencias_ordenadas)

print("Ventas totales ordenadas de menor a mayor:")
for i in range(len(ventas_ordenadas)):
    print("Vendedor", referencias_ordenadas[i]," Total $",ventas_ordenadas[i])

print("Ventas totales ordenadas de mayor a menor:")
for i in range(len(ventas_ordenadas_desc)):
    print("Vendedor ",referencias_ordenadas_desc[i]," Total $",ventas_ordenadas_desc[i])

